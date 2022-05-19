import datetime
import json
import os
import uuid
from typing import Optional
from urllib.parse import urljoin, urlparse

import aiofiles
import pyotp
from flask import Blueprint, abort, flash, jsonify, redirect, render_template, request
from flask_login import current_user, login_user, logout_user
from flask_nav.elements import Navbar, Subgroup, View
from flask_wtf import FlaskForm
from flask_wtf.csrf import generate_csrf
from PIL import Image
from werkzeug.routing import BaseConverter
from wtforms import (
    BooleanField,
    EmailField,
    FileField,
    HiddenField,
    IntegerField,
    PasswordField,
    RadioField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
    validators,
)
from wtforms.widgets import PasswordInput

from app import app, celery, csrf, login_manager, nav, redisConn, user_images
from app.core.config import settings
from app.core.logger import log
from app.models import User
from app.services import (
    account_service,
    accounting_service,
    admin_preference_service,
    admin_service,
    api_service,
    billing_service,
    information_service,
    keyword_service,
    network_service,
    report_service,
    setting_service,
    shortcode_service,
    sms_service,
    user_service,
)
from app.services.api.user import models
from app.utils import Struct, admin_required, choices, getIP, getSetting, validateMSISDN
from app.utils.email import ts, user_activate, user_password_reset
from app.utils.ext_fields import AttribSelectField
from app.utils.utils import login_required, url_for

nav.register_element(
    "admins",
    Navbar(
        "Administration",
        View(
            {"name": "Dashboard", "icon": "fas fa-home"},
            "base.dashboard",
        ),
        Subgroup(
            {"name": "Accounts", "id": "accounts", "top": True},
            View(
                {
                    "name": "Corporate Accounts",
                    "icon": "fas fa-user-tag",
                },
                "accounts.business",
            ),
            View(
                {
                    "name": "Individual Accounts",
                    "icon": "fas fa-user-cog",
                },
                "accounts.individuals",
            ),
            View(
                {
                    "name": "System Administrators",
                    "icon": "fas fa-user-shield",
                },
                "accounts.staff",
            ),
        ),
        Subgroup(
            {"name": "Reports", "id": "reports", "top": True},
            View(
                {"name": "Audit Trail", "icon": "fas fa-stream"},
                "reports.audit",
            ),
        ),
        Subgroup(
            {"name": "System Settings", "id": "settings", "top": True},
            View(
                {"name": "Email Setup", "icon": "fas fa-envelope"},
                "system.emailSettings",
            ),
            View(
                {
                    "name": "Terms & Conditions",
                    "icon": "fas fa-bars",
                },
                "system.terms",
            ),
        ),
    ),
)


class LoginForm(FlaskForm):
    method = SelectField(
        "Login By", choices=[("email", "Email Address"), ("msisdn", "Phone Number")]
    )
    value = StringField("Email Address")
    password = PasswordField(
        "Password",
        widget=PasswordInput(hide_value=False),
        validators=[
            validators.DataRequired("Please enter your password"),
        ],
    )
    remember = BooleanField("Remember Me?")


class ResetForm(FlaskForm):
    method = SelectField(
        "Send OTP to", choices=[("email", "Email Address"), ("msisdn", "Phone Number")]
    )
    value = StringField("Email Address")
    otp = IntegerField("OTP")
    forgot_submit = SubmitField("Submit")


class PasswordForm(FlaskForm):
    password = PasswordField(
        "New Password",
        widget=PasswordInput(hide_value=True),
        validators=[validators.DataRequired()],
    )
    password2 = PasswordField(
        "New Password (Repeat)",
        widget=PasswordInput(hide_value=True),
        validators=[validators.DataRequired()],
    )
    save_btn = SubmitField("Save Changes")


class FloatForm(FlaskForm):
    id = HiddenField("ID")
    fdate = StringField("Date", validators=[validators.DataRequired()])
    network_id = SelectField("Network", validators=[validators.DataRequired()])
    amount = IntegerField("Amount", validators=[validators.DataRequired()])
    notes = TextAreaField("Notes", validators=[validators.DataRequired()])
    save_btn = SubmitField("Save Changes")


class ProfileForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    msisdn = StringField("Telephone")
    email = EmailField("Email")
    gender = RadioField("Gender", choices=[("M", "Male"), ("F", "Female")])
    dob = StringField("Date of Birth")
    avatar = FileField("Avatar")

    save_btn = SubmitField("Save Changes")


class ProfilePasswordForm(FlaskForm):
    old_password = PasswordField(
        "Current Password",
        widget=PasswordInput(hide_value=True),
        validators=[
            validators.DataRequired("Please enter your password"),
        ],
    )
    password = PasswordField(
        "Set New Password",
        widget=PasswordInput(hide_value=True),
        validators=[
            validators.DataRequired("Please enter your password"),
        ],
    )
    password_confirm = PasswordField(
        "Confirm Password",
        widget=PasswordInput(hide_value=True),
        validators=[
            validators.DataRequired("Please enter your password"),
        ],
    )

    save_btn = SubmitField("Save Changes")


class TopupForm(FlaskForm):
    is_company = SelectField(
        "Type",
        choices=[
            ("", "Select"),
            ("True", "Company"),
            ("False", "Individual"),
        ],
    )
    account_id = AttribSelectField("Account", validators=[validators.DataRequired()])
    topup_type_id = SelectField("Topup Type", validators=[validators.DataRequired()])
    credits = IntegerField("Credits", validators=[validators.DataRequired()])
    notes = TextAreaField("Notes")
    save_btn = SubmitField("Save Changes")


class NetworkCostForm(FlaskForm):
    id = HiddenField("ID")
    billing_id = HiddenField("Billing ID")
    name = StringField("Name", validators=[validators.DataRequired()])
    country_id = SelectField("Country&sup1;")
    prefixes = StringField("Prefixes&sup1;")
    network_id = SelectField("Outgoing Network", validators=[validators.DataRequired()])
    cost = IntegerField("Cost", validators=[validators.DataRequired()])
    save_btn = SubmitField("Save Changes")


class SetPasswordForm(FlaskForm):
    id = HiddenField("ID")
    code = HiddenField("Code")
    password = PasswordField("Set New Password")
    password_confirm = PasswordField("Confirm Password")


class MTForm(FlaskForm):
    account_id = SelectField("Account")
    from_date = StringField("From")
    to_date = StringField("To")


base_bp = Blueprint("base", __name__)


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "dict"):
            return obj.dict()
        elif isinstance(obj, uuid.UUID):
            return str(obj)
        elif isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)


app.url_map.converters["regex"] = RegexConverter


@login_manager.user_loader
def user_loader(id):
    try:
        # First check the cache
        r = redisConn.hget("user", str(id))
        if r:
            data = json.loads(r)
        else:
            _user = admin_service.get_sync(id)
            log.debug(_user)
            data = _user["data"]
            redisConn.hset(
                "user", str(data["id"]), json.dumps(data, cls=ComplexEncoder)
            )

        log.debug(f"data=> {data}")
        data = models.Admin.parse_obj(data)
        r = User(data)
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash("You must be logged in to view that page.", "danger")
    next = url_for(request.endpoint, **request.view_args)
    return redirect(url_for("base.index", next=next))


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ("http", "https") and ref_url.netloc == test_url.netloc


@base_bp.route("/tools/_refresh_csrf/", methods=["GET"])
@login_required()
@csrf.exempt
def csrf_refresh():
    token = generate_csrf()
    return jsonify(token)


@base_bp.route("/", methods=["GET", "POST"])
@csrf.exempt
async def index():
    if current_user.is_authenticated:
        next = request.args.get("next")
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return abort(400)

        return redirect(next or url_for("base.dashboard"))

    form = LoginForm()
    form2 = ResetForm()
    if request.method == "GET":
        return render_template("index.djhtml", form=form, form2=form2)

    remember = True if form.remember.data == "on" else False
    _user = await admin_service.login(
        method=form.method.data, value=form.value.data, password=form.password.data
    )
    if _user.success:
        redisConn.hset(
            "user",
            str(_user.data.id),
            json.dumps(_user.data.dict(), cls=ComplexEncoder),
        )

        u = User(_user.data)
        if not u.active:
            flash("This user has not been activated", "danger")
            return render_template("index.djhtml", form=form, form2=form2)

        login_user(u, remember=remember)
        next = request.args.get("next")
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return abort(400)

        return redirect(next or url_for("base.dashboard"))
    else:
        flash(_user.message, "danger")

    return render_template("index.djhtml", form=form, form2=form2)


@base_bp.route("/dashboard")
@login_required()
async def dashboard():
    log.debug(current_user.__dict__)
    """Admin dashboard."""
    try:
        accounts = await account_service.list()
        networks = await network_service.list()
        log.debug(networks)
        shortcodes = await shortcode_service.list()

        rows = redisConn.hgetall("networkbilling")

        networkbilling = [
            (f"networkbilling-{k}", json.loads(v)) for k, v in rows.items()
        ]

        return render_template(
            "dashboard.djhtml",
            networks=networks.data,
            accounts=accounts.data,
            shortcodes=shortcodes.data,
            networkbilling=dict(networkbilling),
        )
    except Exception as e:
        log.error(e, exc_info=True)
        return ""


@base_bp.route("/logout")
async def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for(".index"))


@base_bp.route("/forgot", methods=["POST"])
async def forgot():
    """Forgot Password."""

    params = request.values
    method = params.get("forgot_method", None)
    value = params.get("forgot_value", None)

    if method == "email":
        _user = await admin_service.check_msisdn(value)
    else:
        _user = await admin_service.check_msisdn(value)

    if _user.success:
        user_password_reset(_user.data.id, _user.data.email, _user.data.name)
        return {"success": True}

    return {"success": False, "message": "Unknown email or telephone number"}


@base_bp.route("/check-email", methods=["POST"])
async def check_email():
    params = request.values
    email = params.email
    u = await admin_service.check_email(email)

    return {"valid": u.success}


@base_bp.route("/check-password", methods=["POST"])
async def check_password():
    params = request.values
    password = params.password
    u = await admin_service.check_password(password)

    return {"valid": u.success}


@base_bp.route("/signup", methods=["POST"])
async def signup():
    """Signup."""
    params = request.values
    email = params.get("email", None)
    password = params.get("password", None)
    name = params.get("name", None)

    u = await admin_service.register(
        name=name, email=email, password=password, role="client"
    )

    if not u.success:
        return {
            "success": False,
            "message": "Failed to register your account. Please contact a system administrator",
        }
    elif u.get("message", None):
        return {"success": False, "message": u.message}
    else:
        user_activate(u.data.id, email, name, password)

        return {"success": True}

    return u


@base_bp.route("/confirm/<token>")
async def confirm_email(token):
    try:
        id = ts.loads(token, salt="email-confirm-key", max_age=86400)
    except Exception:
        abort(404)

    u = await admin_service.get(id)
    if u and u.success:
        await admin_service.enable(id)
        flash("Successfully confirmed your email. Please login", "success")
        return redirect(url_for(".index"))
    else:
        return {}, 400


@base_bp.route("/reset/<token>", methods=["GET", "POST"])
async def reset_password_token(token):
    form = PasswordForm()
    try:
        id = ts.loads(token, salt="password-reset-key", max_age=86400)
    except Exception:
        flash("Invalid/Expired token supplied.", "danger")
        return redirect(url_for(".index"))

    try:
        u = json.loads(redisConn.get(token))
    except Exception:
        flash("Invalid/Expired token supplied.", "danger")
        return redirect(url_for(".index"))

    if request.method == "POST":
        if form.password.data == "" or form.password2.data == "":
            flash("Please enter a password and its confirmation", "danger")
        elif form.password.data != form.password2.data:
            flash("Please enter a password and its confirmation", "danger")
        else:
            r = await admin_service.set_password(id, form.password.data)
            if r.success:
                # Delete the token from the database
                redisConn.delete(token)
                flash("Password successfully reset. Please login", "success")
                return redirect(url_for(".index"))
            else:
                flash(r.message, "danger")

    return render_template(
        "reset.djhtml",
        username=u["username"],
        email=u["email"],
        token=token,
        form=form,
        title="Reset Password",
    )


@base_bp.route("/password")
async def changePassword():
    return render_template("change_password.djhtml")


@base_bp.route("/float")
@admin_required()
async def float():
    """Admin float."""
    try:
        rows = await accounting_service.networkfloat_list()

        floats = [f.dict() for f in rows.data]
        for f in floats:
            d = await admin_service.get(f["user_id"])
            f["user"] = d.data

        log.debug(floats)

        return render_template("float.djhtml", floats=floats)
    except Exception as e:
        log.error(e)


@base_bp.route("/float/<int:id>/edit", methods=["GET", "POST"])
@admin_required()
async def floatEdit(id):
    """Edit Float"""
    form = FloatForm()
    form.id.data = id
    form.network_id.choices = await choices.networks()

    if form.validate_on_submit():
        # Save form
        if id > 0:
            r = await accounting_service.networkfloat_update(
                id,
                form.fdate.data,
                form.network_id.data,
                form.amount.data,
                form.notes.data,
                current_user.id,
            )
        else:
            r = await accounting_service.networkfloat_add(
                form.fdate.data,
                form.network_id.data,
                form.amount.data,
                form.notes.data,
                current_user.id,
            )

        return r.dict()
    elif request.method == "POST":
        log.debug(form.errors)
        return {"success": False, "message": "Failed to validate form"}

    return render_template("float_edit.djhtml", form=form)


@base_bp.route("/float/remove", methods=["POST"])
@admin_required()
async def floatRemove():
    """Remove Float"""
    id = request.values.get("id")
    r = await accounting_service.networkfloat_delete(id)
    return r.dict()


@base_bp.route("/topup/json", methods=["POST"])
@admin_required()
async def topupJSON():
    """List Topups"""
    params = dict(request.values)
    topups = await accounting_service.topup_list(params)
    return topups


@base_bp.route("/topup")
@admin_required()
async def topup():
    """Admin topup."""
    log.debug("******** MARK")
    accounts = await account_service.list()
    topup_types = await accounting_service.list_topup_types()
    log.debug("******** MARK")
    return render_template(
        "topup.djhtml", accounts=accounts.data, topup_types=topup_types.data
    )


@base_bp.route("/topup/add", methods=["GET", "POST"])
@admin_required()
async def topupAdd():
    """Edit Topup"""
    form = TopupForm()
    form.account_id.choices = await choices.accounts_chained()
    form.topup_type_id.choices = await choices.topup_types()

    log.debug(form.credits.data)
    if form.validate_on_submit():
        # Save form
        r = await accounting_service.topup_add(
            account_id=form.account_id.data,
            topup_type_id=form.topup_type_id.data,
            credits=form.credits.data,
            notes=form.notes.data,
            user_id=current_user.id,
        )
        log.debug(r)
        return r.dict()
    elif request.method == "POST":
        return {"success": False, "message": str(form.errors)}

    accounts = await account_service.list()
    return render_template("topup_edit.djhtml", form=form, accounts=accounts.data)


@base_bp.route("/topup/reverse", methods=["POST"])
@admin_required()
async def topupReverse():
    """Reverse Topup"""
    id = request.values.get("id")
    r = await accounting_service.topup_reverse(id)
    return r.dict()


@base_bp.route("/billing", methods=["POST"])
@admin_required()
async def billingAdd():
    """Billing addition"""
    r = await billing_service.add(request.values["name"])
    return r.dict()


@base_bp.route("/billing/delete", methods=["POST"])
@admin_required()
async def billingDelete():
    """Billing deletion"""
    r = await billing_service.delete(request.values.get("id"))
    return r.dict()


@base_bp.route("/billing")
@admin_required()
async def billing():
    """Billing management"""
    id = request.values.get("id", None)
    billings = await billing_service.list()

    billing = None
    for r in billings.data:
        if r.id == id:
            billing = r

    if not billing:
        billing = billings.data[0]

    billing = billing.dict()

    for network in billing["networks"]:
        if network["name"] != "OTHER":
            c = await information_service.country(network["country_id"])
            network["country"] = c.data.name
            network["network_prefixes"] = ",".join(
                [x["name"] for x in network["prefixes"]]
            )
        else:
            network["country"] = "N/A"
            network["network_prefixes"] = ""

    return render_template(
        "billing_plan.djhtml", current_billing=billing, billings=billings.data
    )


@base_bp.route("/billing/<string:billing_id>/change", methods=["POST"])
@admin_required()
async def networkCostChange(billing_id):
    if request.values["action"] == "delete":
        r = await billing_service.network_delete(request.values["id"])
        return r.dict()

    return {"success": False, "message": "Invalid action specified"}


@base_bp.route("/billing/<string:billing_id>/cost", methods=["POST", "GET"])
@base_bp.route("/billing/<string:billing_id>/cost/<int:id>", methods=["POST", "GET"])
@admin_required()
async def networkCostEdit(billing_id, id=None):
    form = NetworkCostForm()
    form.billing_id.data = billing_id
    form.country_id.choices = await choices.countries_simple()
    form.network_id.choices = await choices.networks()

    if request.method == "GET":
        try:
            if id:
                row = await billing_service.network_get(id)
                cost = row.data.dict()
                form = NetworkCostForm(obj=Struct(**cost))
                form.country_id.choices = await choices.countries_simple()
                form.network_id.choices = await choices.networks()
                form.prefixes.data = ",".join([x["name"] for x in cost["prefixes"]])

            return render_template("billing_network_edit.djhtml", form=form)
        except Exception as e:
            log.error(e, exc_info=True)

    if form.validate_on_submit():
        if id:
            # Save cost
            r = await billing_service.network_update(
                id,
                name=form.name.data,
                billing_id=form.billing_id.data,
                country_id=form.country_id.data,
                network_id=form.network_id.data,
                prefixes=form.prefixes.data.split(","),
                cost=form.cost.data,
            )
        else:
            # Save cost
            r = await billing_service.network_add(
                name=form.name.data,
                billing_id=form.billing_id.data,
                country_id=form.country_id.data,
                network_id=form.network_id.data,
                prefixes=form.prefixes.data.split(","),
                cost=form.cost.data,
            )
        return r.dict()
    else:
        return {"success": False, "message": form.errors}


@base_bp.route("/graph/mo")
@csrf.exempt
async def moGraph():
    params = dict(request.values)
    r = await report_service.moGraph(params)
    return r


@base_bp.route("/graph/mt")
@csrf.exempt
async def mtGraph():
    params = dict(request.values)
    r = await report_service.mtGraph(params)
    return r


@base_bp.route("/graph/mt/json", methods=["POST"])
@admin_required()
async def mtJSON():
    params = dict(request.values)
    r = await report_service.mtJSON(params)
    return r


@base_bp.route("/graph/mo/json", methods=["POST"])
@admin_required()
async def moJSON():
    params = dict(request.values)
    r = await report_service.moJSON(params)
    return r


@base_bp.route("/email", methods=["POST", "GET"])
@admin_required()
async def emailSettings():
    """Email Settings"""
    if request.method == "POST":
        params = dict(request.values)
        log.debug(params)

        for k, v in request.values.items():
            log.debug(f"{k} => {v}")
            if k[:5] == "EMAIL":
                await setting_service.update(k, v)

    settings = await setting_service.list()
    log.debug(settings)
    return render_template("settings.djhtml", settings=settings.data)


@base_bp.route("/set-preference", methods=["POST"])
async def set_preference():
    valid_prefs = ["DARK_MODE"]
    params = dict(request.values)

    if params.get("name", None) in valid_prefs:
        r = await admin_preference_service.set(
            current_user.id, name=params.get("name"), value=params.get("value")
        )
        _user = await admin_service.get(current_user.id)

        data = _user.data.dict()
        redisConn.hset("user", str(data["id"]), json.dumps(data, cls=ComplexEncoder))

    return {"success": True}


async def saveFile(in_file, filename):
    out_file_path = f"/data/kyc/profile-{filename}"
    out_thumb_path = f"/data/kyc/profile-{filename}-thumb"
    async with aiofiles.open(out_file_path, "wb") as out_file:
        while content := await in_file.read(1024):  # async read chunk
            await out_file.write(content)  # async write chunk

    try:
        im = Image.open(out_file_path)
        im.thumbnail((256, 256), Image.ANTIALIAS)
        im.save(out_thumb_path, "PNG")
    except IOError:
        log.info("cannot create thumbnail for '%s'" % out_file_path)


@base_bp.route("/profile", methods=["POST", "GET"])
@login_required()
async def profile():
    form = ProfileForm()

    if form.validate_on_submit():
        #  # Upload image
        _user = await admin_service.update(
            current_user.id,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            msisdn=form.msisdn.data,
            dob=form.dob.data,
            gender=form.gender.data,
        )
        if "avatar" in request.files:
            log.debug(request.files["avatar"])
            name = f"{current_user.id}.jpg"
            thumbnail = f"{current_user.id}_100x100_fit_90.jpg"
            try:
                r = user_images.save(request.files["avatar"], name=name)
                log.debug(r)
                if os.path.exists(f'{app.config["THUMBNAIL_MEDIA_ROOT"]}/{thumbnail}'):
                    os.remove(f'{app.config["THUMBNAIL_MEDIA_ROOT"]}/{thumbnail}')
            except Exception as e:
                log.error(e, exc_info=True)
                pass

        if _user.success:
            current_user.name = f"{form.first_name.data} {form.last_name.data}"
            current_user.msisdn = form.msisdn.data
            current_user.email = form.email.data
            flash("Successfully saved changes", "success")
        else:
            flash(r.message, "danger")

    else:
        _user = await admin_service.get(current_user.id)

    if not _user.success:
        log.error(_user.dict())
        return (
            render_template(
                "errors/500.djhtml",
                detail="System Error",
            ),
            500,
        )

    log.debug(_user.data)
    form.first_name.data = _user.data.first_name
    form.last_name.data = _user.data.last_name
    form.msisdn.data = _user.data.msisdn
    form.email.data = _user.data.email
    form.dob.data = _user.data.dob
    form.gender.data = _user.data.gender

    return render_template("profile.djhtml", form=form)


@base_bp.route("/profile/password", methods=["POST", "GET"])
@login_required()
async def profile_password():
    form = ProfilePasswordForm()

    if form.validate_on_submit():
        await admin_service.update_password(
            current_user.id, password=form.password.data
        )

    return render_template(
        "profile_password.djhtml",
        form=form,
    )


async def check_msisdn(
    msisdn: str = None, id: Optional[str] = None, country_id: Optional[str] = None
):
    msisdn_parsed = validateMSISDN(msisdn, country_id)

    if not msisdn_parsed:
        return {
            "valid": False,
            "message": "The phone number is not valid for the selected country",
        }

    r = await admin_service.check_msisdn(msisdn_parsed)

    log.debug(r)
    if r.success and str(r.data.id) != id:
        return {"valid": False}

    return {"valid": True}


@base_bp.route("/check-msisdn")
async def check_msisdn_admin():
    msisdn = request.values.get("msisdn", None)
    id = request.values.get("id", None)
    country_id = request.values.get("country_id", None)

    return check_msisdn(msisdn, id, country_id)


@base_bp.route("/check-msisdn-user")
async def check_msisdn_user():
    msisdn = request.values.get("msisdn", None)
    id = request.values.get("id", None)
    country_id = request.values.get("country_id", None)

    msisdn_parsed = validateMSISDN(msisdn, country_id)

    if not msisdn_parsed:
        return {
            "valid": False,
            "message": "The phone number is not valid for the selected country",
        }

    r = await user_service.check_msisdn(msisdn_parsed)

    if r.success and str(r.data.kyc_id) != id:
        return {"valid": False}

    return {"valid": True}


@base_bp.route("/check-keyword")
async def check_keyword():
    keyword = request.values.get("keyword", None)
    id = request.values.get("id", None)
    account_id = request.values.get("account_id", None)

    if not account_id:
        account_id = None

    r = await keyword_service.check(keyword, account_id)

    log.debug(r)
    if r.success and str(r.data.id) != id:
        return {"valid": False}

    return {"valid": True}


@base_bp.route("/reset", methods=["POST", "GET"])
async def reset():
    form = ResetForm()

    if form.validate_on_submit():
        # Lookup the OTP
        hasError = False
        otp = redisConn.get(f"reset-{form.otp.data}")
        if not otp:
            hasError = True
            log.info("no such code")
            flash("Invalid OTP provided", "danger")
        else:
            data = json.loads(otp)
            if data["value"] != form.value.data:
                hasError = True
                log.info("invalid code")
                flash("Invalid OTP provided", "danger")

        if not hasError:
            pform = SetPasswordForm()
            pform.id.data = data["id"]
            pform.code.data = form.otp.data
            return render_template(
                "password-reset.djhtml",
                form=pform,
                user=data,
                code=form.otp.data,
            )

    return render_template("forgot-password.djhtml", form=form)


@base_bp.route("/set-password", methods=["POST"])
async def resetConfirm():
    form = SetPasswordForm()
    messages = []

    if form.validate_on_submit():
        log.debug(f"{form.id.data}, {form.password.data}")
        u = await admin_service.set_password(form.id.data, form.password.data)
        if u.success:
            return {"success": True}
        else:
            return {"success": False, "message": u.message}
    elif form.errors:
        return {"success": False, "message": [v for k, v in form.errors.items()]}

    return {"success": False, "message": "System Error"}


@base_bp.route("/send-otp", methods=["POST"])
async def sendOTP():
    form = ResetForm()

    def myconverter(o):
        if isinstance(o, datetime.datetime) or isinstance(o, uuid.UUID):
            return o.__str__()

    async def setCode(value, data):
        # Generate a verification code
        secret = pyotp.random_base32()
        hotp = pyotp.HOTP(secret)
        code = hotp.at(0)

        data = dict(data)
        data["value"] = value
        log.debug(data)
        redisConn.set(f"reset-{code}", json.dumps(data, default=myconverter))
        redisConn.expire(f"reset-{code}", 300)

        return code

    if form.method.data == "email":
        u = await admin_service.check_email(form.value.data)
        log.debug(u)
        if u.success and u.data:
            code = await setCode(form.value.data, u.data)
            # Generate reset link
            reset_html = render_template(
                "email/reset.djhtml",
                user=u.data,
                code=code,
            )

            celery.send_task(
                "email.send_email",
                kwargs={
                    "to": [form.value.data],
                    "subject": f"{getSetting('GLOBAL_COMPANY_SHORTNAME')} SMS Gateway Admin Portal - OTP",
                    "message": reset_html,
                },
                queue="email",
            )

            return {"success": True}
        else:
            return {
                "success": False,
                "message": "This email address does not exist in the system",
            }
    elif form.method.data == "msisdn":
        u = await admin_service.check_msisdn(form.value.data)
        if u.success and u.data:
            code = await setCode(form.value.data, u.data)
            api = await api_service.get(settings.APIKEY)
            if not api.success:
                return {
                    "success": False,
                    "message": "Cannot send OTPs a the moment. Please contact a system administrator",
                }

            user = {
                "api_id": settings.APIKEY,
                "account_id": api.data.account_id,
                "ip": getIP(),
            }
            r = await sms_service.send(
                user,
                sender_id=getSetting("GLOBAL_SMS_SENDER"),
                msisdn=form.value.data,
                message=f"Your OTP for resetting your password on the {getSetting('GLOBAL_COMPANY_SHORTNAME')} SMS Gateway Admin Portal is {code}. This code expires in 5 minutes",
            )

            return {"success": True}

    return {"success": False, "message": "Unknown error. Please try again"}
