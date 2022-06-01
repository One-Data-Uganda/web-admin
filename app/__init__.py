import datetime
import json
import os
import sys
import time
from urllib.parse import quote_plus

import redis
from celery import Celery
from dominate import tags
from flask import Flask, abort, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager, current_user
from flask_nav import Nav, register_renderer
from flask_nav.renderers import Renderer
from flask_session import Session
from flask_thumbnails import Thumbnail
from flask_uploads import IMAGES, UploadSet, configure_uploads
from flask_wtf.csrf import CSRFError, CSRFProtect
from werkzeug.exceptions import HTTPException

# Werkzeug 0.15 and newer
from werkzeug.middleware.proxy_fix import ProxyFix

import celeryconfig
from app.core.config import settings
from config import config

from .celery_utils import init_celery
from .core.logger import log


class OverwriteUploadSet(UploadSet):
    def resolve_conflict(self, target_folder, basename):
        # I don't care about conflicts
        return basename


class MenuRenderer(Renderer):
    def visit_Navbar(self, node):
        sub = []
        for item in node.items:
            sub.append(self.visit(item))

        r = tags.div(
            cls="menu menu-lg-rounded menu-column menu-lg-row menu-state-primary menu-state-bg-gray-200 menu-title-dark menu-state-title-primary-light menu-state-icon-primary-light menu-arrow-gray-400 fw-bold my-5 my-lg-0 align-items-stretch flex-grow-1",
            id="#kt_header_menu",
            data_kt_menu="true",
            *sub,
        )
        return r

    def visit_TopItem(self, node):
        if node.active:
            _cls = " active "
        else:
            _cls = ""

        div = tags.div(
            cls="menu-item me-lg-1",
        )

        link = tags.a(href=node.get_url(), cls="menu-link py-3 " + _cls)
        link += tags.span("{}".format(node.text["name"]), cls="menu-title")
        div += link
        return div

    def visit_Text(self, node):
        div = tags.div(cls="menu-section")
        div += tags.h4("{}".format(node.text["name"]), cls="menu-text")
        if node.text.get("icon", None):
            div += tags.i(cld=node.text["icon"])
        return div

    def visit_View(self, node):
        if node.active:
            _cls = " here"
        else:
            _cls = ""

        div = tags.div(cls="menu-item" + _cls)

        link = tags.a(href=node.get_url(), cls="menu-link py-3")
        if node.text.get("icon"):
            icon = tags.i(cls=node.text.get("icon", ""))
            link += tags.span(icon, cls="menu-icon")

        link += tags.span(f'{node.text["name"]}', cls="menu-title")
        div += link
        return div

    def visit_Subgroup(self, node):
        if node.active:
            _cls = " here show"
        else:
            _cls = ""

        div = tags.div(
            cls="menu-item menu-lg-down-accordion me-lg-1" + _cls,
            data_kt_menu_placement="bottom-start"
            if node.title.get("top", False)
            else "right-start",
            data_kt_menu_trigger="{default:'click', lg: 'hover'}",
        )

        link = tags.span(cls="menu-link py-3")

        if node.title.get("icon"):
            icon = tags.i(cls=node.title.get("icon", ""))
            link += tags.span(icon, cls="menu-icon")

        link += tags.span(f'{node.title["name"]}', cls="menu-title")
        link += tags.span(cls="menu-arrow")

        div += link

        sub = []
        for item in node.items:
            sub.append(self.visit(item))
        if sub:
            div += tags.div(
                cls="menu-sub menu-sub-lg-down-accordion menu-sub-lg-dropdown menu-rounded-0 py-lg-4 w-lg-225px",
                *sub,
            )

        return div


class ListRenderer(Renderer):
    def visit_Navbar(self, node):
        ul = tags.ul(cls="header-tabs nav align-self-end font-size-lg", role="tablist")
        for item in node.items:
            ul += self.visit_TopItem(item)

        return ul

    def visit_TopItem(self, node):
        li = tags.li(cls="nav-item")
        if node.active:
            _cls = "active"
        else:
            _cls = ""

        link = tags.a(
            node.title["name"],
            href="#",
            cls=f"nav-link py-4 px-6 {_cls}",
            data_toggle="tab",
            data_target=f"#header_{node.title['id']}",
            role="tab",
        )
        li += link
        return li


app = Flask(__name__, static_folder="../static")

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URI", "postgresql+psycopg2://one_data:one_data@db/one_data"
)
app.config["SQLALCHEMY_BINDS"] = {
    "project": "postgresql+psycopg2://one_data:one_data@db/project_db",
    "information": "postgresql+psycopg2://one_data:one_data@db/information_db",
}

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()
app.jinja_env.filters["quote_plus"] = lambda u: quote_plus(u)

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1)

CORS(app)

login_manager = LoginManager()
nav = Nav()
csrf = CSRFProtect()
thumb = Thumbnail()
sess = Session()

CELERY_BROKER = settings.CELERY_BROKER
CELERY_BACKEND = settings.CELERY_BACKEND

kannelRedis = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=10,
    decode_responses=True,
)

redisConn = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True,
)

celery = Celery(__name__, backend=CELERY_BACKEND, broker=CELERY_BROKER)
celery.config_from_object(celeryconfig)
user_images = OverwriteUploadSet("userimages", IMAGES)


@app.errorhandler(Exception)
def internal_server_error(error):
    # pass through HTTP errors
    log.error(error)
    if isinstance(error, HTTPException):
        return error

    log.error(error, exc_info=True)
    return (
        render_template(
            "error.djhtml",
            error_code="Oops",
            message="Something went wrong. Please try again, or return to the home page",
        ),
        500,
    )


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.djhtml"), 404


@app.context_processor
def inject_today_date():
    return {"today_date": datetime.date.today()}


@app.context_processor
def inject_tStamp():
    return {"tStamp": time.time()}


# Usually, CSRF failures occur in JS requests
@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return {
        "success": False,
        "message": "ERROR: Your session has expired, please refresh and login",
    }


@app.context_processor
def inject_WebsocketURL():
    if settings.CONFIG_TYPE == "dev":
        return {"websocket_url": "ws://localhost:9105/ws"}

    if settings.WEBSOCKET_SSL:
        protocol = "wss"
    else:
        protocol = "ws"

    return {"websocket_url": f"{protocol}://{request.host}/ws"}


@app.template_filter()
def default_profile_image(value):
    fpath = f'{app.config["THUMBNAIL_MEDIA_ROOT"]}/{value}'

    if not os.path.isfile(fpath):
        value = "blank.png"

    return value


def handle_catch(caller, on_exception):
    try:
        return caller()
    except Exception:
        return on_exception


@app.template_filter()
def numberFormat(value):
    return format(int(value), ",d")


@app.template_filter()
def floatFormat(value):
    value = float(value)
    return "{:,.2f}".format(value)


@app.template_filter()
def currencyFormat(value):
    value = float(value)
    return "{:,.3f}".format(value)


@app.context_processor
def utility_processor():
    def getX(val):
        if val:
            return "X"
        else:
            return ""

    def balances():
        r = redisConn.hget("accountbilling", current_user.account["id"])
        if r:
            return json.loads(r)
        return {"actual_balance": 0, "available_balance": 0}

    return dict(getX=getX, balances=balances)


def getSettings(id):
    r = redisConn.hget("setting", str(id))

    if not r:
        return ""

    r = json.loads(r)
    return r["value"]


@app.route("/abort")
def closeme():
    abort(500)


def create_app(config_type="dev"):
    app.config.from_object(config[config_type])
    app.config.update(SESSION_COOKIE_NAME="sms-gw-admin")

    login_manager.init_app(app)
    nav.init_app(app)
    csrf.init_app(app)
    try:
        thumb.init_app(app)
    except Exception:
        pass
    sess.init_app(app)

    configure_uploads(app, user_images)

    # patch_request_class(app, 32 * 1024 * 1024)  # 32MB file size limit
    init_celery(app, celery)
    celery.conf.update(app.config)

    app.url_map.strict_slashes = False

    from .views.base import base_bp
    from .views.modules.accounts import accounts_bp
    from .views.modules.reports import reports_bp
    from .views.modules.system import system_bp

    app.register_blueprint(base_bp, url_prefix="/")
    app.register_blueprint(accounts_bp, url_prefix="/accounts")
    app.register_blueprint(reports_bp, url_prefix="/reports")
    app.register_blueprint(system_bp, url_prefix="/system")

    register_renderer(app, "renderer", MenuRenderer)

    app.jinja_env.globals["handle_catch"] = handle_catch
    app.jinja_env.globals["settings"] = getSettings

    # Make directories
    try:
        os.makedirs(app.config["PDF_FOLDER"])
        os.makedirs(app.config["UPLOADED_PHOTOS_DEST"])
    except Exception:
        pass

    return app
