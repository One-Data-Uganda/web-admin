from flask import Blueprint, render_template, request, send_from_directory
from flask_wtf import FlaskForm
from wtforms import EmailField, SelectField, StringField, SubmitField

from app.core.logger import log  # noqa
from app.services import (
    account_service,
    accounting_service,
    api_service,
    keyword_service,
    network_service,
    report_service,
    user_service,
)
from app.utils import choices, login_required
from app.utils.ext_fields import AttribSelectField

reports_bp = Blueprint("reports", __name__)


class StatementForm(FlaskForm):
    is_company = SelectField(
        "Type", choices=[("", "Select"), ("True", "Company"), ("False", "Individual")]
    )
    account_id = AttribSelectField("Account")
    date_from = StringField("Date From")
    date_to = StringField("Date To")
    email = EmailField("Email to Send To")
    btn_submit = SubmitField("Generate Statement")


@reports_bp.route("/send-email")
async def sendEmailReport():
    return render_template("send_email.djhtml")


@reports_bp.route("/files/<filename>")
async def sendReport(filename):
    return send_from_directory("/project/reports/", filename)


async def getmtstatus(status):
    if status == 0:
        return "Queued"
    elif status == 1:
        return "Delivered"
    elif status == 2:
        return "Not Delivered"
    elif status == 4:
        return "Unreachable"
    elif status == 8:
        return "Pending"
    elif status == 16:
        return "Rejected"
    else:
        return "Pending"


@reports_bp.route("/mt")
@login_required()
async def mt():
    networks = await network_service.list()
    accounts = await account_service.list()
    apis = await api_service.listAll()
    users = await user_service.listAll()
    log.debug(apis)

    return render_template(
        "reports/mt.djhtml",
        networks=networks.data,
        accounts=accounts.data,
        apis=apis.data,
        users=users.data,
    )


@reports_bp.route("/mt/json", methods=["POST"])
@login_required()
async def mtJSON():
    try:
        mt = await report_service.mtJSON(
            params=dict(request.values),
        )

        return mt
    except Exception as e:
        log.error(e, exc_info=True)

    return {}


@reports_bp.route("/mt-light")
@login_required()
async def mtLight():
    networks = await network_service.list()
    accounts = await account_service.list()

    return render_template(
        "reports/mt-light.djhtml", networks=networks.data, accounts=accounts.data
    )


@reports_bp.route("/mt-light/json", methods=["POST"])
@login_required()
async def mtLightJSON():
    try:
        mt = await report_service.mtLightJSON(
            params=dict(request.values),
        )

        return mt
    except Exception as e:
        log.error(e, exc_info=True)

    return {}


@reports_bp.route("/mt-summary")
@login_required()
async def mtSummary():
    networks = await network_service.list()
    accounts = await account_service.list()

    return render_template(
        "reports/mt-summary.djhtml", networks=networks.data, accounts=accounts.data
    )


@reports_bp.route("/mt-summary/json", methods=["POST"])
@login_required()
async def mtSummaryJSON():
    try:
        mt = await report_service.mtSummaryJSON(
            params=dict(request.values),
        )

        return mt
    except Exception as e:
        log.error(e, exc_info=True)

    return {}


@reports_bp.route("/mt-network")
@login_required()
async def mtNetwork():
    networks = await network_service.list()

    return render_template("reports/mt-network.djhtml", networks=networks.data)


@reports_bp.route("/mt-network/json", methods=["POST"])
@login_required()
async def mtNetworkJSON():
    try:
        mt = await report_service.mtNetworkJSON(
            params=dict(request.values),
        )

        return mt
    except Exception as e:
        log.error(e, exc_info=True)

    return {}


@reports_bp.route("/mt-simple")
@login_required()
async def mtSimple():
    networks = await network_service.list()
    log.debug(networks)

    return render_template("reports/mt-simple.djhtml", networks=networks.data)


@reports_bp.route("/mt-simple/json", methods=["POST"])
@login_required()
async def mtSimpleJSON():
    log.debug(request.values)
    try:
        mt = await report_service.mtJSON(
            params=dict(request.values),
        )

        return mt
    except Exception as e:
        log.error(e, exc_info=True)

    return {}


@reports_bp.route("/mt/graph")
@login_required()
async def mtGraph():
    params = dict(request.values)
    r = await report_service.mtGraph(params)
    return r


@reports_bp.route("/mo/graph")
@login_required()
async def moGraph():
    params = dict(request.values)
    r = await report_service.moGraph(params)
    return r


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


@reports_bp.route("/statement", methods=["POST", "GET"])
@login_required()
async def statement():
    form = StatementForm()
    account_choices = await choices.accounts_chained()
    form.account_id.choices = account_choices

    if form.validate_on_submit():
        account_choices = {r[0]: r[1] for r in account_choices if r[0]}

        log.debug(account_choices)
        account_display = account_choices.get(form.account_id.data)
        r = await report_service.get_statement(
            form.account_id.data,
            account_display,
            form.date_from.data,
            form.date_to.data,
            form.email.data,
        )

        return r.dict()

    return render_template("reports/statement_admin.djhtml", form=form)


@reports_bp.route("/mo")
@login_required()
async def mo():
    keywords = await keyword_service.list()
    accounts = await account_service.list()

    return render_template(
        "reports/mo.djhtml", keywords=keywords.data, accounts=accounts.data
    )


@reports_bp.route("/mo/json", methods=["POST"])
@login_required()
async def moJSON():
    try:
        mo = await report_service.moJSON(
            params=dict(request.values),
        )

        return mo
    except Exception as e:
        log.error(e, exc_info=True)

    return {}


@reports_bp.route("/mo-summary")
@login_required()
async def moSummary():
    keywords = await keyword_service.list()
    accounts = await account_service.list()

    return render_template(
        "reports/mo-summary.djhtml", keywords=keywords.data, accounts=accounts.data
    )


@reports_bp.route("/mo-summary/json", methods=["POST"])
@login_required()
async def moSummaryJSON():
    try:
        mo = await report_service.moSummaryJSON(
            params=dict(request.values),
        )

        return mo
    except Exception as e:
        log.error(e, exc_info=True)

    return {}


@reports_bp.route("/keyword-performance")
@login_required()
async def keywordPerformance():
    return render_template("reports/keyword-performance.djhtml")


@reports_bp.route("/keyword-performance/json", methods=["POST"])
@login_required()
async def keywordPerformanceJSON():
    try:
        keyword_performance = await report_service.keywordPerformanceJSON(
            params=dict(request.values),
        )
        log.debug(keyword_performance)

        return keyword_performance
    except Exception as e:
        log.error(e, exc_info=True)
        return {}


@reports_bp.route("/closing-balance")
@login_required()
async def closingBalance():
    accounts = await account_service.list()

    return render_template("reports/closing-balance.djhtml", accounts=accounts.data)


@reports_bp.route("/closing-balance/json", methods=["POST"])
@login_required()
async def closingBalanceJSON():
    log.debug(dict(request.values))

    try:
        closing = await accounting_service.closingBalanceJSON(
            params=dict(request.values),
        )

        return closing
    except Exception as e:
        log.error(e, exc_info=True)

    return {}
