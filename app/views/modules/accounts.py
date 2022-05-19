from uuid import UUID

import httpx
import phonenumbers
from flask import Blueprint, flash, render_template, request, send_from_directory
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import (
    BooleanField,
    HiddenField,
    IntegerField,
    PasswordField,
    RadioField,
    SelectField,
    SelectMultipleField,
    StringField,
    SubmitField,
    TextAreaField,
    validators,
)

from app.core.config import settings
from app.core.logger import log
from app.services import (
    account_service,
    accounting_service,
    admin_group_service,
    admin_service,
    api_service,
    document_type_service,
    group_service,
    information_service,
    kyc_service,
    user_service,
)
from app.utils import admin_required, choices, validateMSISDN
from app.utils.ext_fields import AttribSelectField

accounts_bp = Blueprint("accounts", __name__)


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


class IndividualAccountForm(FlaskForm):
    id = HiddenField("ID")
    password = PasswordField("Password", validators=[validators.Optional()])
    dob = StringField("Date of Birth", validators=[validators.DataRequired()])
    tin = StringField("TIN", validators=[validators.DataRequired()])
    first_name = StringField("First Name", validators=[validators.DataRequired()])
    last_name = StringField("Last Name", validators=[validators.DataRequired()])
    email_1 = StringField("Email", validators=[validators.DataRequired()])
    msisdn_1 = StringField("Mobile Number", validators=[validators.Optional()])
    account_group_id = SelectField("User Group", validators=[validators.DataRequired()])
    gender = RadioField(
        "Gender",
        choices=[("M", "Male"), ("F", "Female")],
        default="F",
        validators=[validators.DataRequired()],
    )
    country_id = AttribSelectField("Country", validators=[validators.DataRequired()])
    billing_id = SelectField("Billing Plan", validators=[validators.DataRequired()])
    active = RadioField(
        "Status",
        choices=[(0, "Inactive"), (1, "Active")],
        default=0,
        coerce=int,
        validators=[validators.DataRequired()],
    )
    activation_email = BooleanField("Send Activation Email")
    warning_level = IntegerField("Warning Level")
    warning_email = StringField("Warning Email(s)")


class StaffForm(FlaskForm):
    id = HiddenField("ID")
    first_name = StringField("First Name", validators=[validators.DataRequired()])
    last_name = StringField("Last Name", validators=[validators.DataRequired()])
    dob = StringField("Date of Birth")
    gender = RadioField(
        "Gender",
        choices=[("M", "Male"), ("F", "Female")],
        default="F",
    )
    country_id = AttribSelectField("Country", validators=[validators.DataRequired()])
    msisdn = StringField("Mobile Number", validators=[validators.Optional()])
    email = StringField("Email", validators=[validators.DataRequired()])
    password = PasswordField("Password", validators=[validators.Optional()])
    admin_group_id = SelectField("Group", validators=[validators.DataRequired()])
    activation_email = BooleanField("Send Activation Email")


class KYCDocumentForm(FlaskForm):
    id = HiddenField("ID")
    document = FileField("Document", validators=[validators.DataRequired()])
    save_btn = SubmitField("Save Document")


class KYCDocumentIndividualForm(FlaskForm):
    id = HiddenField("ID")
    document_type_id = SelectField("Document Type")
    document = FileField("Document", validators=[validators.DataRequired()])
    save_btn = SubmitField("Save Document")


class BusinessAccountForm(FlaskForm):
    id = HiddenField("ID")
    business_name = StringField("Name", validators=[validators.DataRequired()])
    country_id = AttribSelectField("Country", validators=[validators.DataRequired()])
    email_1 = StringField("Company Email", validators=[validators.Optional()])
    msisdn_1 = StringField("Company Telephone", validators=[validators.Optional()])
    address = TextAreaField("Address", validators=[validators.DataRequired()])
    tin = StringField("TIN", validators=[validators.DataRequired()])
    billing_id = SelectField("Billing Plan", validators=[validators.DataRequired()])
    active = RadioField(
        "Active?",
        choices=[(0, "No"), (1, "Yes")],
        default=0,
        coerce=int,
        validators=[validators.DataRequired()],
    )
    warning_level = IntegerField("Warning Level")
    warning_email = StringField("Warning Email(s)")


class BusinessUserForm(FlaskForm):
    id = HiddenField("ID")
    password = PasswordField("Password", validators=[validators.Optional()])
    dob = StringField("Date of Birth")
    first_name = StringField("First Name", validators=[validators.DataRequired()])
    last_name = StringField("Last Name", validators=[validators.DataRequired()])
    country_id = AttribSelectField("Country", validators=[validators.DataRequired()])
    email_1 = StringField("Email", validators=[validators.DataRequired()])
    msisdn_1 = StringField("Mobile", validators=[validators.Optional()])
    account_group_id = SelectField("User Group", validators=[validators.DataRequired()])
    gender = RadioField(
        "Gender",
        choices=[("M", "Male"), ("F", "Female")],
        default="F",
        validators=[validators.DataRequired()],
    )


class AdminUserForm(FlaskForm):
    id = HiddenField("ID")
    password = PasswordField("Password", validators=[validators.Optional()])
    name = StringField("Name", validators=[validators.DataRequired()])
    email = StringField("Email", validators=[validators.DataRequired()])
    msisdn_1 = StringField("Mobile Number", validators=[validators.Optional()])
    msisdn_2 = StringField("Mobile Number", validators=[validators.Optional()])


class GroupForm(FlaskForm):
    id = HiddenField("ID")
    name = StringField("Name", validators=[validators.DataRequired()])
    roles = SelectMultipleField("Roles", validators=[validators.DataRequired()])
    save_btn = SubmitField("Save Changes")


@accounts_bp.route("/business/json", methods=["POST"])
@admin_required()
@admin_required()
async def businessJSON():
    """List Business Accounts"""
    params = dict(request.values)
    accounts = await account_service.search(params)
    return accounts


@accounts_bp.route("/business", methods=["GET", "POST"])
@admin_required()
async def business():
    """Business Accounts"""
    countries = await information_service.country_list()
    billing_plans = await accounting_service.billing_list()
    return render_template(
        "accounts/business.djhtml",
        countries=countries.data,
        billing_plans=billing_plans.data,
    )


@accounts_bp.route("/business/edit", methods=["GET", "POST"])
@admin_required()
async def businessEdit():
    """Edit Business Accounts"""
    params = request.values
    id = params.get("id", None)

    try:
        form = BusinessAccountForm()
        form.id.data = id
        form.country_id.choices = await choices.countries()
        form.billing_id.choices = await choices.billing_plans()
    except Exception as e:
        log.error(e)

    if request.method == "POST":
        if id:
            log.debug(f"**** {form.active.data}")
            if form.msisdn_1.data:
                msisdn_1 = phonenumbers.parse(form.msisdn_1.data, form.country_id.data)
            else:
                msisdn_1 = None

            r = await account_service.update(
                form.id.data,
                business_name=form.business_name.data,
                tin=form.tin.data,
                country_id=form.country_id.data,
                billing_id=form.billing_id.data,
                address_1=form.address.data,
                msisdn_1=phonenumbers.format_number(
                    msisdn_1, phonenumbers.PhoneNumberFormat.E164
                )
                if msisdn_1
                else None,
                email_1=form.email_1.data,
                active=True if form.active.data == 1 else False,
                warning_level=form.warning_level.data,
                warning_email=form.warning_email.data,
                queue="normal",
                dob=None,
                gender=None,
                is_company=True,
            )
        else:
            r = await account_service.add(
                business_name=form.business_name.data,
                tin=form.tin.data,
                country_id=form.country_id.data,
                billing_id=form.billing_id.data,
                address_1=form.address.data,
                msisdn_1=phonenumbers.format_number(
                    msisdn_1, phonenumbers.PhoneNumberFormat.E164
                )
                if msisdn_1
                else None,
                email_1=form.email_1.data,
                active=True if form.active.data == 1 else False,
                warning_level=form.warning_level.data,
                warning_email=form.warning_email.data,
                queue="normal",
                dob=None,
                gender=None,
                is_company=True,
            )
        return r.dict()

    if id:
        try:
            _account = await account_service.get(id)
            _account = _account.data
            form.business_name.data = _account.kyc.business_name
            form.country_id.data = _account.kyc.country_id
            form.address.data = _account.kyc.address_1
            form.tin.data = _account.kyc.tin
            form.billing_id.data = _account.billing_id
            form.warning_level.data = _account.warning_level
            form.warning_email.data = _account.warning_email
            form.active.data = 1 if _account.active else 0
        except Exception as e:
            log.error(e, exc_info=True)
        try:
            form.msisdn_1.data = _account.kyc.msisdns[0].id
        except Exception:
            pass

        try:
            form.email_1.data = _account.kyc.emails[0].id
        except Exception:
            pass

    return render_template("accounts/business_edit.djhtml", form=form)


@accounts_bp.route("/individual/json", methods=["POST"])
@admin_required()
async def individualsJSON():
    """List Individual Individuals"""
    params = dict(request.values)
    individuals = await account_service.search_individual(params)
    return individuals


@accounts_bp.route("/individual", methods=["GET", "POST"])
@admin_required()
async def individuals():
    """Individual Individuals"""
    countries = await information_service.country_list()
    billing_plans = await accounting_service.billing_list()
    return render_template(
        "accounts/individual.djhtml",
        countries=countries.data,
        billing_plans=billing_plans.data,
    )


@accounts_bp.route("/individual/edit", methods=["GET", "POST"])
@admin_required()
async def individualEdit():
    """Edit Individual Accounts"""
    params = request.values
    id = params.get("id", None)

    form = IndividualAccountForm()
    form.id.data = id
    form.country_id.choices = await choices.countries()
    form.billing_id.choices = await choices.billing_plans()

    if request.method == "POST":
        msisdn_1 = phonenumbers.parse(form.msisdn_1.data, form.country_id.data)
        if id:
            try:
                r = await account_service.update(
                    form.id.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    tin=None,
                    country_id=form.country_id.data,
                    billing_id=form.billing_id.data,
                    address_1=None,
                    msisdn_1=phonenumbers.format_number(
                        msisdn_1, phonenumbers.PhoneNumberFormat.E164
                    ),
                    email_1=form.email_1.data,
                    queue="normal",
                    gender=form.gender.data,
                    dob=form.dob.data,
                    active=True if form.active.data == 1 else False,
                    is_company=False,
                    warning_level=form.warning_level.data,
                    warning_email=form.warning_email.data,
                )
                if not r.success:
                    return r.dict()

                log.debug(r)

                _user = await user_service.get_by_kyc(r.data.kyc_id)

                # Then update the user
                u = await user_service.update(
                    _user.data.id,
                    password=form.password.data,
                    active=True if form.active.data == 1 else False,
                )
                log.debug(f"****************** {u}")

                if not u.success:
                    return u.dict()
            except Exception as e:
                log.error(e)
        else:
            r = await account_service.add(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                country_id=form.country_id.data,
                billing_id=form.billing_id.data,
                msisdn_1=phonenumbers.format_number(
                    msisdn_1, phonenumbers.PhoneNumberFormat.E164
                ),
                email_1=form.email_1.data,
                gender=form.gender.data,
                dob=form.dob.data,
                is_company=False,
                active=True if form.active.data == 1 else False,
                warning_level=form.warning_level.data,
                warning_email=form.warning_email.data,
                queue="normal",
                tin=None,
                address_1=None,
            )

            if not r.success:
                return r.dict()

            log.debug(r)

            # Now we create this person as the first admin
            # 1. Get the groups
            rows = await group_service.list(r.data.id)
            group = rows.data[0]  # yes, this is an assumption
            # 2. Create user with this group
            u = await user_service.add_with_kyc(
                group_id=group.id,
                password=form.password.data,
                active=True if form.active.data == 1 else False,
                kyc_id=r.data.kyc_id,
            )
            if not u.success:
                return u.dict()

        return r.dict()

    if id:
        try:
            _account = await account_service.get(id)
            _account = _account.data
            _user = await user_service.get_by_kyc(_account.kyc_id)
            _user = _user.data

            log.debug(_account)
            msisdn_1 = phonenumbers.parse(
                _account.kyc.msisdns[0].id, _account.kyc.country_id
            )
            form.country_id.data = _account.kyc.country_id
            form.password.data = None
            form.dob.data = _account.kyc.dob
            form.first_name.data = _account.kyc.first_name
            form.last_name.data = _account.kyc.last_name
            form.email_1.data = _account.kyc.emails[0].id
            form.msisdn_1.data = msisdn_1.national_number
            form.gender.data = _account.kyc.gender
            form.password.data = ""
            form.active.data = 1 if _user.active else 0
        except Exception as e:
            log.error(e)

    return render_template("accounts/individual_edit.djhtml", form=form)


@accounts_bp.route("/kyc", methods=["GET", "POST"])
@accounts_bp.route("/kyc/<string:id>", methods=["GET", "POST"])
@admin_required()
async def editKYC(id=None):
    """Edit KYC"""
    if not id:
        flash("Failed to retrieve KYC", "danger")
        return render_template("accounts/business.djhtml")

    try:
        kyc = await kyc_service.get(id)

        rows = await document_type_service.list()
        document_types = [x for x in rows.data if x.is_company == kyc.data.is_company]

        rows = await kyc_service.get_documents(id)

        documents = {}
        for r in rows.data:
            documents[r.document_type_id] = r

        return render_template(
            "accounts/kyc.djhtml",
            kyc=kyc.data,
            document_types=document_types,
            documents=documents,
        )
    except Exception as e:
        log.error(e, exc_info=True)

    return ""


@accounts_bp.route("/document/<string:id>/verify", methods=["POST"])
@admin_required()
async def verifyKYCDocument(id):
    """Verify KYC Document"""
    r = await kyc_service.verify_document(id, current_user.id)

    return r.dict()


@accounts_bp.route("/document/<string:kyc_id>/<string:id>")
@admin_required()
async def getKYCDocument(kyc_id, id):
    try:
        document = await kyc_service.get_document(kyc_id, id)
        document_type = await document_type_service.get(document.data.document_type_id)
        kyc = await kyc_service.get(kyc_id)

        name = (
            kyc.data.business_name
            if kyc.data.is_company
            else f"{kyc.data.firstname} {kyc.data.lastname}"
        )
        filename = f"{name} - {document_type.data.name}.pdf"

        log.debug(f"{settings.KYC_FILE_PATH}/{id[:1]}/{id} => {filename}")
        return send_from_directory(
            f"{settings.KYC_FILE_PATH}/{id[:1]}",
            path=id,
            download_name=filename,
            attachment_filename=filename,
        )
    except Exception as e:
        log.error(e, exc_info=True)


@accounts_bp.route(
    "/document/<string:kyc_id>/<string:type>/edit", methods=["GET", "POST"]
)
@admin_required()
async def editKYCDocument(kyc_id, type):
    form = KYCDocumentForm()
    document_type = await document_type_service.get(type)
    kyc = await kyc_service.get(kyc_id)

    if form.validate_on_submit():
        r = await kyc_service.add_document(
            kyc_id=kyc_id,
            name=document_type.data.name,
            document_type_id=type,
            uploaded_file=form.document.data,
        )

        return r.dict()

    return render_template(
        "accounts/kyc_edit.djhtml",
        form=form,
        document_type=document_type.data,
        kyc=kyc.data,
    )


@accounts_bp.route("/users", methods=["GET", "POST"])
@accounts_bp.route("/users/<string:id>", methods=["GET", "POST"])
@admin_required()
async def editUsers(id=None):
    """Edit Users"""
    if not id:
        flash("Failed to retrieve users", "danger")
        return render_template("accounts/business.djhtml")

    account = await account_service.get(id)

    return render_template("accounts/users.djhtml", account=account.data)


@accounts_bp.route("/users/<string:account_id>/json", methods=["POST"])
@admin_required()
async def usersJSON(account_id):
    """List Account Users"""
    params = dict(request.values)
    try:
        users = await user_service.user_json(account_id, params)
        return users
    except Exception as e:
        log.error(e, exc_info=True)
        return []


@accounts_bp.route("/staff", methods=["GET", "POST"])
@admin_required()
async def staff():
    """Staff Members"""
    admin_groups = await admin_group_service.list()
    return render_template("accounts/staff.djhtml", admin_groups=admin_groups.data)


@accounts_bp.route("/user/state/<string:state>", methods=["POST"])
@admin_required()
async def userChangeState(state):
    id = request.values.get("id")
    if state == "enable":
        r = await user_service.enable(id)
    else:
        r = await user_service.disable(id)

    return r.dict()


@accounts_bp.route("/staff/edit", methods=["GET", "POST"])
@admin_required()
async def staffEdit():
    """Edit Staff Users"""
    params = request.values
    id = params.get("id", None)

    form = StaffForm()
    form.id.data = id
    form.admin_group_id.choices = await choices.admin_groups()
    form.country_id.choices = await choices.countries()

    if form.validate_on_submit():
        msisdn = validateMSISDN(form.msisdn.data, form.country_id.data)

        if not msisdn:
            return {
                "success": False,
                "message": "The phone number entered is not valid for the selected country",
            }
        if id:
            r = await admin_service.update(
                form.id.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                dob=form.dob.data,
                gender=form.gender.data,
                country_id=form.country_id.data,
                msisdn=msisdn,
                password=form.password.data,
                admin_group_id=form.admin_group_id.data,
                email=form.email.data,
            )
        else:
            r = await admin_service.add(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                dob=form.dob.data,
                gender=form.gender.data,
                country_id=form.country_id.data,
                msisdn=msisdn,
                password=form.password.data,
                admin_group_id=form.admin_group_id.data,
                email=form.email.data,
            )
        return r.dict()

    if id:
        try:
            _user = await admin_service.get(id)
            log.debug(_user)
            if _user.data.msisdn:
                msisdn = phonenumbers.parse(_user.data.msisdn)
                form.msisdn.data = msisdn.national_number
            form.first_name.data = _user.data.first_name
            form.last_name.data = _user.data.last_name
            form.dob.data = _user.data.dob
            form.gender.data = _user.data.gender
            form.country_id.data = _user.data.country_id
            form.admin_group_id.data = _user.data.admin_group_id
            form.email.data = _user.data.email
            form.id.data = _user.data.id

        except Exception as e:
            log.error(e, exc_info=True)
            pass

    return render_template("accounts/staff_edit.djhtml", form=form)


@accounts_bp.route("/staff/json", methods=["POST"])
@admin_required()
async def staffJSON():
    """List Staff User"""
    params = dict(request.values)
    users = await admin_service.admin_json(params)
    return users


@accounts_bp.route("/account/state/<string:state>", methods=["POST"])
@admin_required()
async def accountChangeState(state):
    id = request.values.get("id")
    if state == "enable":
        r = await account_service.enable(id)
    else:
        r = await account_service.disable(id)

    return r.dict()


@accounts_bp.route("/user/<string:account_id>/edit", methods=["GET", "POST"])
@admin_required()
async def userChange(account_id: UUID):
    """Edit Business Account Users"""
    params = request.values
    id = params.get("id", None)
    kyc_id = None

    form = BusinessUserForm()
    form.id.data = id
    form.account_group_id.choices = await choices.account_groups(account_id)
    form.country_id.choices = await choices.countries()

    if request.method == "POST":
        msisdn = validateMSISDN(form.msisdn_1.data, form.country_id.data)

        if not msisdn:
            return {"success": False, "message": "Invalid mobile number"}

        try:
            if id:
                r = await user_service.update(
                    form.id.data,
                    account_id=account_id,
                    account_group_id=form.account_group_id.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    password=form.password.data,
                    email_1=form.email_1.data,
                    msisdn_1=msisdn,
                    dob=form.dob.data,
                    gender=form.gender.data,
                    country_id=form.country_id.data,
                )
            else:
                r = await user_service.add(
                    account_id=account_id,
                    account_group_id=form.account_group_id.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    password=form.password.data,
                    email_1=form.email_1.data,
                    msisdn_1=msisdn,
                    dob=form.dob.data,
                    gender=form.gender.data,
                    country_id=form.country_id.data,
                )
            return r.dict()
        except Exception as e:
            log.error(e, exc_info=True)
            return {"success": False, "message": "System Error"}

    try:
        if id:
            _user = await user_service.get(id)
            _user = _user.data
            log.debug(_user)
            form.password.data = None
            form.first_name.data = _user.kyc.first_name
            form.last_name.data = _user.kyc.last_name
            form.email_1.data = _user.kyc.emails[0].id
            if _user.kyc.msisdns:
                msisdn = phonenumbers.parse(
                    _user.kyc.msisdns[0].id, _user.kyc.country_id
                )
                form.msisdn_1.data = msisdn.national_number
            form.gender.data = _user.kyc.gender
            form.dob.data = _user.kyc.dob
            form.account_group_id.data = _user.account_group_id
            form.country_id.data = _user.kyc.country_id
            kyc_id = _user.kyc.id
    except Exception as e:
        log.error(e, exc_info=True)

    return render_template(
        "accounts/user_edit.djhtml", form=form, id=account_id, kyc_id=kyc_id
    )


@accounts_bp.route("/api", methods=["GET", "POST"])
@accounts_bp.route("/api/<string:id>", methods=["GET", "POST"])
@admin_required()
async def editApiKeys(id=None):
    """Edit API Keys"""
    account = await account_service.get(id)
    apikeys = await api_service.list(id)

    log.debug(apikeys)

    return render_template(
        "accounts/api.djhtml", account=account.data, apikeys=apikeys.data
    )


@accounts_bp.route("/api-action/<string:action>", methods=["POST"])
@admin_required()
async def api(action):
    """Edit API Keys"""
    id = request.values.get("id")

    r = None
    try:
        if action == "disable":
            r = await api_service.disable(id)
        elif action == "enable":
            r = await api_service.enable(id)
        elif action == "new":
            r = await api_service.add(
                account_id=request.values.get("account_id"),
                name=request.values.get("name"),
            )
    except Exception as e:
        log.error(e)

    if r:
        return r.dict()

    return {"success": False, "message": "Invalid action specified"}


@accounts_bp.route("/group")
@accounts_bp.route("/group/<string:account_id>")
@admin_required()
async def groups(account_id=None):
    """Client group."""
    try:
        _roles = await choices.roles()

        account = await account_service.get(account_id)
        groups = await group_service.list(account_id)
    except Exception as e:
        log.error(e, exc_info=True)

    return render_template(
        "accounts/groups.djhtml",
        groups=groups.data,
        account=account.data,
        _roles=dict(_roles),
    )


@accounts_bp.route("/group/<string:account_id>/edit", methods=["GET", "POST"])
@accounts_bp.route("/group/<string:account_id>/<int:id>/edit", methods=["GET", "POST"])
@admin_required()
async def groupEdit(account_id, id=None):
    """Edit Group"""
    form = GroupForm()
    form.id.data = id

    account = await account_service.get(account_id)
    form.roles.choices = await choices.roles()

    if form.validate_on_submit():
        # Save form
        if form.id.data > 0:
            r = await group_service.update(
                id, name=form.name.data, roles=form.roles.data
            )
        else:
            r = await group_service.add(
                account_id=account_id,
                name=form.name.data,
                roles=form.roles.data,
            )

        return r.dict()

    if id > 0:
        res = await group_service.get(id)
        form.name.data = res.data.name
        form.roles.data = res.data.roles

    return render_template("users/group_edit.djhtml", form=form, account=account, id=id)


@accounts_bp.route("/group/<string:account_id>/action", methods=["GET", "POST"])
@admin_required()
async def groupAction(account_id):
    """Edit Group"""
    id = request.values.get("id")
    action = request.values.get("action")

    if action == "delete":
        r = await group_service.delete(id)
        return r.dict()

    return {"success": False, "message": "Invalid action specified"}


@accounts_bp.route("/group/<string:account_id>/remove", methods=["POST"])
@admin_required()
async def groupRemove(account_id):
    """Remove Group"""
    id = request.values.get("id")
    r = await group_service.delete(id)
    return r.dict()


@accounts_bp.route("/update-balances", methods=["POST"])
@admin_required()
async def updateBalances():
    """Update account balances"""
    msg = {
        "action": "fix-balances",
        "payload": {},
    }

    async with httpx.AsyncClient() as client:
        await client.post("http://nsqd:4151/pub?topic=accounting", json=msg)

    return {"success": True}
