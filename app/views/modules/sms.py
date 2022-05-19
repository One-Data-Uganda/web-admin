from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import (
    HiddenField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
    validators,
)

from app.core.logger import log
from app.services import (  # noqa
    account_service,
    blacklist_service,
    keyword_service,
    report_service,
    sender_service,
    shortcode_service,
    smsservice_service,
)
from app.utils import Struct, admin_required, choices, validateMSISDN
from app.utils.ext_fields import AttribSelectField

sms_bp = Blueprint("sms", __name__)


class KeywordForm(FlaskForm):
    id = HiddenField("ID")
    is_company = SelectField(
        "Account Type",
        choices=[("", "-- Select -- "), ("True", "Company"), ("False", "Individual")],
    )
    account_id = AttribSelectField("Account", validators=[validators.DataRequired()])
    keyword = StringField("Keyword", validators=[validators.DataRequired()])
    keyword_type = SelectField("Keyword Type")
    alias_id = AttribSelectField("Keyword Alias")
    url = StringField("URL")
    list_id = AttribSelectField("Contact List")
    text = TextAreaField("Text")
    save_btn = SubmitField("Save")


class BlacklistForm(FlaskForm):
    is_company = SelectField(
        "Account Type",
        choices=[("", "-- Select -- "), ("True", "Company"), ("False", "Individual")],
    )
    account_id = AttribSelectField("Account")
    country_id = AttribSelectField("Country")
    calling_code = StringField("Calling Code")
    msisdn = StringField("MSISDN", validators=[validators.DataRequired()])
    shortcode = SelectField("Shortcode (optional)")
    sender = StringField("Sender ID (optional)")
    notes = TextAreaField("Notes")
    save_btn = SubmitField("Save")


class SenderForm(FlaskForm):
    id = HiddenField("ID")
    is_company = SelectField(
        "Type",
        choices=[
            ("", "Select"),
            ("True", "Company"),
            ("False", "Individual"),
        ],
    )
    name = StringField("Sender ID", validators=[validators.DataRequired()])
    account_id = AttribSelectField("Account", validators=[validators.DataRequired()])
    save_btn = SubmitField("Save Changes")


class ShortcodeForm(FlaskForm):
    id = HiddenField("ID")
    is_company = SelectField(
        "Type",
        choices=[
            ("", "Select"),
            ("True", "Company"),
            ("False", "Individual"),
        ],
    )
    name = StringField("Name", validators=[validators.DataRequired()])
    account_id = AttribSelectField("Account", validators=[validators.DataRequired()])
    save_btn = SubmitField("Save Changes")


@sms_bp.route("/sender")
@admin_required()
async def sender():
    """Senders"""
    accounts = await account_service.list()
    return render_template("sms/senders.djhtml", accounts=accounts.data)


@sms_bp.route("/sender/edit", methods=["GET", "POST"])
@admin_required()
async def senderEdit():
    """Edit Sender"""
    id = request.values.get("id", 0)

    id = int(id)

    form = SenderForm()
    form.id.data = id
    form.account_id.choices = await choices.accounts_chained()

    if form.validate_on_submit():
        log.debug(form.account_id.data)
        # Save form
        if id:
            r = await sender_service.update(
                id, name=form.name.data, account_id=form.account_id.data
            )
        else:
            r = await sender_service.add(
                name=form.name.data, account_id=form.account_id.data
            )

        return r.dict()

    if id:
        sender = await sender_service.get(id)
        form.name.data = sender.data.name
        form.is_company.data = f"company-{sender.data.account.is_company}"
        form.account_id.data = sender.data.account_id

    return render_template("sms/sender_edit.djhtml", form=form)


@sms_bp.route("/sender/action", methods=["POST"])
@admin_required()
async def senderAction():
    """Remove Sender"""
    id = request.values.get("id")
    action = request.values.get("action")

    if action == "delete":
        r = await sender_service.delete(id)
    elif action == "enable":
        r = await sender_service.enable(id)
    elif action == "disable":
        r = await sender_service.disable(id)
    elif action == "reject":
        r = await sender_service.reject(id, request.values.get("reason"))
    elif action == "approve":
        r = await sender_service.approve(id)
    else:
        return {"success": False, "message": "ERROR: Invalid action"}

    return r.dict()


@sms_bp.route("/sender/json", methods=["POST"])
@admin_required()
async def senderJSON():
    """List Senders"""
    params = dict(request.values)
    senders = await report_service.senderJSON(params)
    return senders


@sms_bp.route("/shortcode")
@admin_required()
async def shortcode():
    """Shortcodes"""
    _shortcodes = await shortcode_service.list()

    shortcodes = []
    try:
        for r in _shortcodes.data:
            x = r.dict()
            if r.account_id:
                account = await account_service.get(r.account_id)
                log.info(account)
                x["account_name"] = (
                    account.data.kyc.business_name
                    if account.data.kyc.is_company
                    else f"{account.data.kyc.firstname} {account.data.kyc.lastname}"
                )
            shortcodes.append(x)
    except Exception as e:
        log.error(e, exc_info=True)
    return render_template("sms/shortcode.djhtml", shortcodes=shortcodes)


@sms_bp.route("/shortcode/<int:id>/assign", methods=["GET", "POST"])
@admin_required()
async def shortcodeAssign(id):
    """Edit Shortcode"""
    form = ShortcodeForm()
    form.account_id.choices = await choices.accounts_chained()

    if request.method == "POST":
        # Save form
        r = await shortcode_service.assign(id, account_id=form.account_id.data)

        return r.dict()

    shortcode = await shortcode_service.get(id)

    return render_template(
        "sms/shortcode_assign.djhtml", form=form, shortcode=shortcode.data
    )


@sms_bp.route("/shortcode/<int:id>/make-default", methods=["POST"])
@admin_required()
async def shortcodeMakeDefault(id):
    r = await shortcode_service.make_default(id)
    return r.dict()


@sms_bp.route("/shortcode/<int:id>/revoke", methods=["POST"])
@admin_required()
async def shortcodeRevoke(id: int):
    """Revoke Shortcode"""
    r = await shortcode_service.delete_shortcode(id)
    return r.dict()


@sms_bp.route("/keywords")
@admin_required()
async def keywords():
    """Client keyword."""
    keywords = await keyword_service.list()
    accounts = await account_service.list()

    return render_template(
        "sms/keywords.djhtml", keywords=keywords.data, accounts=accounts.data
    )


@sms_bp.route("/keyword/edit", methods=["GET", "POST"])
@admin_required()
async def keywordEdit():
    """Edit Keyword"""
    try:
        form = KeywordForm()

        id = request.values.get("id", None)
        if id:
            r = await keyword_service.get(id)
            data = r.data.dict()
            form = KeywordForm(obj=Struct(**data))
            account = await account_service.get(form.account_id.data)
            if account.success:
                form.is_company.data = str(account.data.kyc.is_company)
                form.account_id.data = str(account.data.id)

                log.debug(f"********* {form.account_id.__dict__}")
            else:
                log.debug(account)
        else:
            id = form.id.data

        form.keyword_type.choices = [
            ("TEXT", "Text"),
            ("ALIAS", "Alias to Keyword"),
            ("URL", "Call External URL"),
            ("LIST", "Broadcast List"),
        ]
        form.alias_id.choices = await choices.keyword_aliases()
        form.list_id.choices = await choices.contact_lists()
        form.account_id.choices = await choices.accounts_chained()
    except Exception as e:
        log.error(e, exc_info=True)
        return ""

    if form.validate_on_submit():
        # Save form
        try:
            keyword_type = form.keyword_type.data
            if id:
                if keyword_type == "ALIAS" and form.id.data == form.alias_id.data:
                    return {
                        "success": False,
                        "message": "ERROR: Cannot alias a keyword to itself",
                    }

                r = await keyword_service.update(
                    id,
                    keyword=form.keyword.data,
                    keyword_type=keyword_type,
                    alias_id=form.alias_id.data if keyword_type == "ALIAS" else None,
                    list_id=form.list_id.data if keyword_type == "LIST" else None,
                    url=form.url.data if keyword_type == "URL" else None,
                    text=form.text.data if keyword_type == "TEXT" else None,
                )
            else:
                r = await keyword_service.add(
                    account_id=form.account_id.data,
                    keyword=form.keyword.data,
                    keyword_type=keyword_type,
                    alias_id=form.alias_id.data if keyword_type == "ALIAS" else None,
                    list_id=form.list_id.data if keyword_type == "LIST" else None,
                    url=form.url.data if keyword_type == "URL" else None,
                    text=form.text.data if keyword_type == "TEXT" else None,
                )
            log.debug(r)
            return r.dict()
        except Exception as e:
            log.error(e, exc_info=True)
            return {"success": False}

    elif request.method == "POST":
        return {"success": False, "message": str(form.errors)}

    return render_template("sms/keyword_edit.djhtml", form=form)


@sms_bp.route("/keyword/action", methods=["POST"])
@admin_required()
async def keywordAction():
    """Remove Keyword"""
    id = request.values.get("id")
    action = request.values.get("action")

    if action == "delete":
        r = await keyword_service.delete(id)
    elif action == "enable":
        r = await keyword_service.enable(id)
    elif action == "disable":
        r = await keyword_service.disable(id)
    elif action == "reject":
        r = await keyword_service.reject(id, request.values.get("reason"))
    elif action == "approve":
        r = await keyword_service.approve(id)
    else:
        return {"success": False, "message": "ERROR: Invalid action"}

    return r.dict()


@sms_bp.route("/keyword/json", methods=["POST"])
@admin_required()
async def keywordJSON():
    """List Keywords"""
    params = dict(request.values)
    keywords = await report_service.keywordJSON(params)
    return keywords


@sms_bp.route("/blacklists")
@admin_required()
async def blacklists():
    """Blacklists"""
    accounts = await account_service.list()
    shortcodes = await shortcode_service.list()
    return render_template(
        "sms/blacklists.djhtml", accounts=accounts.data, shortcodes=shortcodes.data
    )


@sms_bp.route("/blacklists/json", methods=["POST"])
@admin_required()
async def blacklistJSON():
    """List Blacklists"""
    params = dict(request.values)
    blacklists = await blacklist_service.report(params)
    return blacklists


@sms_bp.route("/blacklist/action", methods=["POST"])
@admin_required()
async def blacklistAction():
    """Remove Blacklist"""
    id = request.values.get("id")
    action = request.values.get("action")

    if action == "delete":
        r = await blacklist_service.delete(id)
        log.debug(r)
    else:
        return {"success": False, "message": "ERROR: Invalid action"}

    return r.dict()


@sms_bp.route("/blacklist/edit", methods=["GET", "POST"])
@admin_required()
async def blacklistEdit():
    """Edit Blacklist"""
    form = BlacklistForm()
    form.country_id.choices = await choices.countries()
    form.account_id.choices = await choices.accounts_chained()
    form.shortcode.choices = await choices.shortcodes()

    if form.validate_on_submit():
        msisdn = validateMSISDN(form.msisdn.data, form.country_id.data)

        if not msisdn:
            return {"success": False, "message": "ERROR: Invalid MSISDN specified"}
        # Save form
        try:
            r = await blacklist_service.add(
                account_id=form.account_id.data,
                msisdn=msisdn,
                shortcode=form.shortcode.data,
                sender=form.sender.data,
                notes=form.notes.data,
            )
            log.debug(r)
            return r.dict()
        except Exception as e:
            log.error(e, exc_info=True)
            return {"success": False}

    else:
        for field, errors in form.errors.items():
            log.error(errors)

    return render_template("sms/blacklist_edit.djhtml", form=form)
