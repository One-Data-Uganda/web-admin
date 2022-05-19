import json
import time
from functools import wraps

import phonenumbers
from flask import _request_ctx_stack, current_app, request
from flask import url_for as _url_for
from flask_login import current_user

from app import redisConn
from app.core.logger import log


def validateMSISDN(msisdn: str, country_id: str):
    if not msisdn or not country_id:
        return None

    try:
        msisdn_parsed = phonenumbers.parse(msisdn, country_id)
    except Exception:
        msisdn_parsed = None

    if msisdn_parsed and phonenumbers.is_valid_number(msisdn_parsed):
        return phonenumbers.format_number(
            msisdn_parsed, phonenumbers.PhoneNumberFormat.E164
        )

    return None


def login_required(role=None):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return current_app.login_manager.unauthorized()
            if role and role not in current_user.roles:
                return current_app.login_manager.unauthorized()
            try:
                # current_app.ensure_sync available in Flask >= 2.0
                return current_app.ensure_sync(fn)(*args, **kwargs)
            except AttributeError:
                return fn(*args, **kwargs)

        return decorated_view

    return wrapper


def admin_required():
    return login_required(role="admin")


def timestamp():
    """Return the current timestamp as an integer."""
    return int(time.time())


def url_for(*args, **kwargs):
    """
    url_for replacement that works even when there is no request context.
    """
    if "_external" not in kwargs:
        kwargs["_external"] = False
    reqctx = _request_ctx_stack.top
    if reqctx is None:
        if kwargs["_external"]:
            raise RuntimeError(
                "Cannot generate external URLs without a " "request context."
            )
        with current_app.test_request_context():
            return _url_for(*args, **kwargs)
    return _url_for(*args, **kwargs)


def getIP():
    try:
        if "CF-Connecting-IP" in request.headers:
            remote_addr = request.headers.getlist("CF-Connecting-IP")[0]
        elif "X-Forwarded-For" in request.headers:
            log.debug(request.access_route)
            try:
                remote_addr = request.access_route[1]
            except Exception:
                remote_addr = request.access_route[-1]
        else:
            remote_addr = request.remote_addr or "untrackable"
        return remote_addr
    except Exception:
        return None


def audit(atype, description):
    ip = getIP()
    # audit = Audit(
    #     user_id=current_user.id, atype=atype, description=description, ipaddress=ip
    # )
    # db.session.add(audit)
    # db.session.commit()


def getSetting(id):
    r = redisConn.hget("setting", id)
    x = json.loads(r)
    return x["value"]
