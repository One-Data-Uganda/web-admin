from flask import Blueprint, render_template, request, send_from_directory
from flask_wtf import FlaskForm
from wtforms import EmailField, SelectField, StringField, SubmitField

from app.core.logger import log  # noqa
from app.services import (
    account_service,
    user_service,
)
from app.utils import choices, login_required
from app.utils.ext_fields import AttribSelectField

reports_bp = Blueprint("reports", __name__)


@reports_bp.route("/send-email")
async def sendEmailReport():
    return render_template("send_email.djhtml")


@reports_bp.route("/files/<filename>")
async def sendReport(filename):
    return send_from_directory("/project/reports/", filename)


@reports_bp.route("/audit")
@login_required()
async def audit():
    accounts = await account_service.list()
    return render_template("reports/audit.djhtml", accounts=accounts.data)


@reports_bp.route("/audit/json", methods=["POST"])
@login_required()
async def auditJSON():
    audit = await account_service.auditJSON(
        params=request.values,
    )
    log.debug(audit)

    return audit
