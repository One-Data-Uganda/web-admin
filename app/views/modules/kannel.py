from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    HiddenField,
    IntegerField,
    RadioField,
    SelectField,
    StringField,
    SubmitField,
    validators,
)

from app.core.logger import log
from app.services import (
    network_service,
    sendsms_user_service,
    shortcode_service,
    smpp_service,
    smsservice_service,
)
from app.utils import Struct, admin_required, choices

kannel_bp = Blueprint("kannel", __name__)


class HostForm(FlaskForm):
    id = HiddenField("ID")
    network_id = HiddenField("Network ID")
    name = StringField("Name", validators=[validators.DataRequired()])
    smsc_type = SelectField(
        "SMSC Type",
        choices=[("smpp", "SMPP"), ("http", "HTTP"), ("fake", "FAKE")],
        validators=[validators.DataRequired()],
    )
    host = StringField("Host", validators=[validators.DataRequired()])
    port = IntegerField("Transmit Port")
    receive_port = IntegerField("Receive Port")
    transceiver_mode = BooleanField("Transceiver?")
    use_ssl = BooleanField("SSL?")
    username = StringField("Username", validators=[validators.DataRequired()])
    password = StringField("Password", validators=[validators.DataRequired()])
    system_type = StringField("System Type")
    wait_ack = IntegerField("Wait ACK Time", default=60)
    log_level = IntegerField("Log Level", default=2)
    msg_type_id = StringField("Message Type ID")

    allowed_prefix = StringField("Allowed Prefix")
    denied_prefix = StringField("Denied Prefix")
    allowed_smsc_id = StringField("Allowed SMSC ID")
    denied_smsc_id = StringField("Denied SMSC ID")

    source_ton = IntegerField("Source Ton", default=0)
    source_npi = IntegerField("NPI", default=0)
    dest_ton = IntegerField("Destination Ton", default=0)
    dest_npi = IntegerField("NPI", default=0)
    save_btn = SubmitField("Save Changes")


class ShortcodeForm(FlaskForm):
    id = IntegerField("Code")
    smsc_id = StringField("SMSC ID(s)")
    save_btn = SubmitField("Save Changes")


class SMSServiceForm(FlaskForm):
    id = HiddenField("ID")
    process_local = RadioField("Process Locally?", choices=[("0", "No"), ("1", "Yes")])
    keyword = StringField("Keyword")
    shortcode_id = SelectField("Shortcode")
    max_messages = IntegerField("Max # of Messages")
    url = StringField("URL")
    url_get = SelectField("Type", choices=[("True", "GET"), ("False", "POST")])
    accepted_smsc = StringField("Accepted SMSC(s)")
    save_btn = SubmitField("Save Changes")


class SendSMSUserForm(FlaskForm):
    id = HiddenField("ID")
    username = StringField("Username")
    password = StringField("Password")
    default_smsc = StringField("Default SMSC")
    save_btn = SubmitField("Save Changes")


class SMPPBoxForm(FlaskForm):
    id = StringField("ID")
    port = IntegerField("Port")
    password = StringField("Password")
    ip_restrictions = StringField("IP Restrictions")
    our_system_id = StringField("Our System ID")
    route_to_smsc = StringField("Route To SMSC")
    save_btn = SubmitField("Save Changes")


@kannel_bp.route("/regenerate", methods=["POST"])
async def regenerate():
    r = await network_service.regenerate()
    return r


@kannel_bp.route("/smpp")
@kannel_bp.route("/smpp/<int:id>")
@admin_required()
async def smpp(id=0):
    """SMPP management"""
    try:
        networks = await network_service.list()
        log.debug(networks)

        network = None

        if not id and networks.data:
            network = networks.data[0]
        else:
            for r in networks.data:
                if r.id == id:
                    network = r

        return render_template(
            "kannel/network.djhtml", current_network=network, networks=networks.data
        )
    except Exception as e:
        log.error(e, exc_info=True)
        return ""


@kannel_bp.route("/smpp/group/add", methods=["POST"])
@admin_required()
async def smppAdd():
    """SMPP addition"""
    r = await network_service.add(request.values["name"])
    return r.dict()


@kannel_bp.route("/smpp/<int:network_id>/host", methods=["POST", "GET"])
@kannel_bp.route("/smpp/<int:network_id>/host/<int:id>", methods=["POST", "GET"])
@admin_required()
async def hostEdit(network_id, id=None):
    form = HostForm()
    form.network_id.data = network_id

    if request.method == "GET":
        if id:
            host = await network_service.gethost(id)
            host = host.data.dict()
            form = HostForm(obj=Struct(**host))

        return render_template("kannel/host.djhtml", form=form)

    if form.validate_on_submit():
        if id and id > 0:
            # Save host
            r = await network_service.updatehost(
                id,
                network_id=network_id,
                name=form.name.data,
                smsc_type=form.smsc_type.data,
                host=form.host.data,
                port=form.port.data,
                receive_port=form.receive_port.data,
                transceiver_mode=form.transceiver_mode.data,
                use_ssl=form.use_ssl.data,
                username=form.username.data,
                password=form.password.data,
                system_type=form.system_type.data,
                wait_ack=form.wait_ack.data,
                log_level=form.log_level.data,
                allowed_prefix=form.allowed_prefix.data,
                denied_prefix=form.denied_prefix.data,
                allowed_smsc_id=form.allowed_smsc_id.data,
                denied_smsc_id=form.denied_smsc_id.data,
                source_ton=form.source_ton.data,
                source_npi=form.source_npi.data,
                dest_ton=form.dest_ton.data,
                dest_npi=form.dest_npi.data,
                msg_type_id=form.msg_type_id.data,
            )
        else:
            # Save host
            r = await network_service.addhost(
                network_id=network_id,
                name=form.name.data,
                smsc_type=form.smsc_type.data,
                host=form.host.data,
                port=form.port.data,
                receive_port=form.receive_port.data,
                transceiver_mode=form.transceiver_mode.data,
                use_ssl=form.use_ssl.data,
                username=form.username.data,
                password=form.password.data,
                system_type=form.system_type.data,
                wait_ack=form.wait_ack.data,
                log_level=form.log_level.data,
                allowed_prefix=form.allowed_prefix.data,
                denied_prefix=form.denied_prefix.data,
                allowed_smsc_id=form.allowed_smsc_id.data,
                denied_smsc_id=form.denied_smsc_id.data,
                source_ton=form.source_ton.data,
                source_npi=form.source_npi.data,
                dest_ton=form.dest_ton.data,
                dest_npi=form.dest_npi.data,
                msg_type_id=form.msg_type_id.data,
                active=True,
            )
        return r.dict()
    else:
        return {"success": False, "message": str(form.errors)}


@kannel_bp.route("/smpp/<int:id>/list", methods=["POST"])
@admin_required()
async def hostList(id):
    r = await network_service.list_for_network(id)
    return {"data": r.data}


@kannel_bp.route("/smpp/host/change", methods=["POST"])
@admin_required()
async def hostChange():
    if request.method == "POST":
        if request.values.get("action") == "disable":
            r = await network_service.disablehost(request.values.get("id"))
        elif request.values.get("action") == "enable":
            r = await network_service.enablehost(request.values.get("id"))
        elif request.values.get("action") == "delete":
            r = await network_service.deletehost(request.values.get("id"))
        elif request.values.get("action") == "clone":
            r = await network_service.clonehost(
                request.values.get("id"), request.values.get("name")
            )
        else:
            return {"success": False, "message": "Invalid action specified"}
        return r.dict()

    return render_template("kannel/host.djhtml")


@kannel_bp.route("/smsc", methods=["POST"])
@admin_required()
async def smscAction():
    smsc = request.values.get("smsc")
    action = request.values.get("action")
    r = await network_service.smsc_action(smsc, action)
    return r


@kannel_bp.route("/queue", methods=["POST"])
@admin_required()
async def queueAction():
    queue = request.values.get("queue")
    action = request.values.get("action")
    r = await network_service.queue_action(queue, action)
    return r.dict()


@kannel_bp.route("/shortcode/change", methods=["POST"])
@admin_required()
async def shortcodeAction():
    if request.values.get("action") == "disable":
        r = await shortcode_service.disable(request.values.get("id"))
    elif request.values.get("action") == "enable":
        r = await shortcode_service.enable(request.values.get("id"))
    elif request.values.get("action") == "delete":
        r = await shortcode_service.delete(request.values.get("id"))
    else:
        return {"success": False, "message": "Invalid action specified"}
    return r.dict()


@kannel_bp.route("/shortcode/edit", methods=["GET", "POST"])
@kannel_bp.route("/shortcode/<int:id>/edit", methods=["GET", "POST"])
@admin_required()
async def shortcodeEdit(id=0):
    """Edit Shortcode"""
    form = ShortcodeForm()

    if form.validate_on_submit():
        # Save form
        if id > 0:
            r = await shortcode_service.update(id, smsc_id=form.smsc_id.data)
        else:
            r = await shortcode_service.add(id=form.id.data, smsc_id=form.smsc_id.data)

        return r.dict()

    shortcode = await shortcode_service.get(id)
    if shortcode.success:
        data = shortcode.data.dict()
        form = ShortcodeForm(obj=Struct(**data))

    return render_template("kannel/shortcode_edit.djhtml", form=form)


@kannel_bp.route("/sms-service/change", methods=["POST"])
@admin_required()
async def SMSServiceAction():
    if request.values.get("action") == "disable":
        r = await smsservice_service.disable(request.values.get("id"))
    elif request.values.get("action") == "enable":
        r = await smsservice_service.enable(request.values.get("id"))
    elif request.values.get("action") == "delete":
        r = await smsservice_service.delete(request.values.get("id"))
    else:
        return {"success": False, "message": "Invalid action specified"}
    return r.dict()


@kannel_bp.route("/sms-service/edit", methods=["GET", "POST"])
@kannel_bp.route("/sms-service/<int:id>/edit", methods=["GET", "POST"])
@admin_required()
async def smsServiceEdit(id=0):
    """Edit SMS Service"""
    form = SMSServiceForm()
    form.shortcode_id.choices = await choices.shortcodes()

    if form.validate_on_submit():
        # Save form
        if form.id.data != "0":
            r = await smsservice_service.update(
                id,
                keyword=form.keyword.data,
                shortcode_id=form.shortcode_id.data,
                max_messages=form.max_messages.data,
                url=form.url.data if form.process_local.data == 0 else "{LOCAL}",
                url_get=form.url_get.data,
                accepted_smsc=form.accepted_smsc.data,
            )
        else:
            r = await smsservice_service.add(
                keyword=form.keyword.data,
                shortcode_id=form.shortcode_id.data,
                max_messages=form.max_messages.data,
                url=form.url.data if form.process_local.data == 0 else "{LOCAL}",
                url_get=form.url_get.data,
                accepted_smsc=form.accepted_smsc.data,
            )

        return r.dict()

    try:
        sms_service = await smsservice_service.get(id)
        if sms_service.success:
            data = sms_service.data.dict()
            form = SMSServiceForm(obj=Struct(**data))

        form.shortcode_id.choices = await choices.shortcodes()
    except Exception as e:
        log.debug(e)

    return render_template("kannel/sms_service_edit.djhtml", form=form)


@kannel_bp.route("/sendsms-user/change", methods=["POST"])
@admin_required()
async def sendSMSUserAction():
    if request.values.get("action") == "disable":
        r = await sendsms_user_service.disable(request.values.get("id"))
    elif request.values.get("action") == "enable":
        r = await sendsms_user_service.enable(request.values.get("id"))
    elif request.values.get("action") == "delete":
        r = await sendsms_user_service.delete(request.values.get("id"))
    else:
        return {"success": False, "message": "Invalid action specified"}
    return r.dict()


@kannel_bp.route("/sendsms-user/edit", methods=["GET", "POST"])
@kannel_bp.route("/sendsms-user/<int:id>/edit", methods=["GET", "POST"])
@admin_required()
async def sendSMSUserEdit(id=0):
    """Edit SendSMS User"""
    form = SendSMSUserForm()

    if form.validate_on_submit():
        # Save form
        if id > 0:
            r = await sendsms_user_service.update(
                id,
                username=form.username.data,
                password=form.password.data,
                default_smsc=form.default_smsc.data,
            )
        else:
            r = await sendsms_user_service.add(
                username=form.username.data,
                password=form.password.data,
                default_smsc=form.default_smsc.data,
            )

        return r.dict()

    sendsms_user = await sendsms_user_service.get(id)
    if sendsms_user.success:
        data = sendsms_user.data.dict()
        form = SendSMSUserForm(obj=Struct(**data))

    return render_template("kannel/sendsms_user_edit.djhtml", form=form)


@kannel_bp.route("/general")
@admin_required()
async def general():
    shortcodes = await shortcode_service.list()
    sms_services = await smsservice_service.list()
    sendsms_users = await sendsms_user_service.list()

    log.debug(shortcodes)

    return render_template(
        "kannel/general.djhtml",
        shortcodes=shortcodes.data,
        sendsms_users=sendsms_users.data,
        sms_services=sms_services.data,
    )


@kannel_bp.route("/smppbox")
@admin_required()
async def smppbox():
    smpps = await smpp_service.list()
    return render_template(
        "kannel/smppbox.djhtml",
        smppboxs=smpps.data,
    )


@kannel_bp.route("/smppbox/change", methods=["POST"])
@admin_required()
async def smppBoxAction():
    if request.values.get("action") == "disable":
        r = await smpp_service.disable(request.values.get("id"))
    elif request.values.get("action") == "enable":
        r = await smpp_service.enable(request.values.get("id"))
    elif request.values.get("action") == "delete":
        r = await smpp_service.delete(request.values.get("id"))
    else:
        return {"success": False, "message": "Invalid action specified"}
    return r.dict()


@kannel_bp.route("/smppbox/edit", methods=["GET", "POST"])
@kannel_bp.route("/smppbox/<string:id>/edit", methods=["GET", "POST"])
@admin_required()
async def smppBoxEdit(id="0"):
    form = SMPPBoxForm()

    try:
        if form.validate_on_submit():
            # Save form
            if id != "0":
                r = await smpp_service.update(
                    id,
                    port=form.port.data,
                    password=form.password.data,
                    ip_restrictions=form.ip_restrictions.data,
                    our_system_id=form.our_system_id.data,
                    route_to_smsc=form.route_to_smsc.data,
                )
            else:
                r = await smpp_service.add(
                    id=form.id.data,
                    port=form.port.data,
                    password=form.password.data,
                    ip_restrictions=form.ip_restrictions.data,
                    our_system_id=form.our_system_id.data,
                    route_to_smsc=form.route_to_smsc.data,
                )

            return r.dict()
        else:
            log.debug(form.errors)
    except Exception as e:
        log.error(e, exc_info=True)

    if id != "0":
        smpp = await smpp_service.get(id)
        if smpp.success:
            data = smpp.data.dict()
            form = SMPPBoxForm(obj=Struct(**data))

    return render_template("kannel/smppbox_edit.djhtml", form=form)


@kannel_bp.route("/regenerate-smpp", methods=["POST"])
async def regenerateSMPP():
    r = await smpp_service.regenerate()
    return r
