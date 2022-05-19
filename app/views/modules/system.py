from flask import Blueprint, flash, render_template, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField

from app import celery
from app.core.logger import log  # noqa
from app.services import setting_service
from app.utils import admin_required, getSetting

system_bp = Blueprint("system", __name__)


class TermsForm(FlaskForm):
    terms = TextAreaField("Terms")
    privacy = TextAreaField("Privacy Policy")
    save_btn = SubmitField("Save Changes")


@system_bp.route("/terms", methods=["POST", "GET"])
@admin_required()
async def terms():
    form = TermsForm()

    if form.validate_on_submit():
        r = await setting_service.add(
            id="TERMS_AGREEMENT",
            name="Terms & Conditions",
            value=form.terms.data,
            type="rtf",
        )
        if not r.success:
            flash("Failed to save terms & conditions", "danger")

        r = await setting_service.add(
            id="TERMS_PRIVACY",
            name="Privacy Policy",
            value=form.privacy.data,
            type="rtf",
        )
        if not r.success:
            flash("Failed to save privacy policy", "danger")

        flash("Successfully saved", "success")
    else:
        terms = await setting_service.get("TERMS_AGREEMENT")
        privacy = await setting_service.get("TERMS_PRIVACY")
        if terms.success:
            form.terms.data = terms.data.value

        if privacy.success:
            form.privacy.data = privacy.data.value

    return render_template("system/terms.djhtml", form=form)


@system_bp.route("/global", methods=["GET", "POST"])
@admin_required()
async def globalSettings():
    global_settings = [
        "GLOBAL_SMS_COST",
        "GLOBAL_SMS_OUTBOX",
        "GLOBAL_SMS_SENDER",
        "GLOBAL_COMPANY_NAME",
        "GLOBAL_COMPANY_COUNTRY",
        "GLOBAL_COMPANY_SHORTNAME",
        "GLOBAL_COMPANY_URL",
    ]

    if request.method == "POST":
        for r in global_settings:
            v = request.form.get(r)

            r = await setting_service.update(id=r, value=v)
        flash("Successfully saved", "success")

    settingRows = await setting_service.list("GLOBAL")

    settingsDict = [(x.id, x.dict()) for x in settingRows.data]

    return render_template(
        "system/global.djhtml",
        global_settings=global_settings,
        settingsDict=dict(settingsDict),
    )


@system_bp.route("/email", methods=["GET", "POST"])
@admin_required()
async def emailSettings():
    email_settings = [
        "EMAIL_SERVER",
        "EMAIL_SSL",
        "EMAIL_PORT",
        "EMAIL_USERNAME",
        "EMAIL_PASSWORD",
        "EMAIL_SENDER",
    ]

    if request.method == "POST":
        for r in email_settings:
            v = request.form.get(r)

            r = await setting_service.update(id=r, value=v)
        flash("Successfully saved", "success")

    settingRows = await setting_service.list("EMAIL")

    settingsDict = [(x.id, x.dict()) for x in settingRows.data]

    return render_template(
        "system/email.djhtml",
        email_settings=email_settings,
        settingsDict=dict(settingsDict),
    )


@system_bp.route("/send-test", methods=["POST"])
def sendTest():
    email = request.values.get("email")

    test_html = render_template(
        "email/test.djhtml",
    )

    celery.send_task(
        "email.send_email",
        kwargs={
            "to": [email],
            "subject": f"{getSetting('GLOBAL_COMPANY_SHORTNAME')} SMS Gateway Admin Portal - Test Email",
            "message": test_html,
        },
        queue="email",
    )

    return {"success": True}
