import os

from asgiref.wsgi import WsgiToAsgi
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response

from app import create_app

wsgi_app = create_app(os.environ.get("CONFIG_TYPE", "dev"))
wsgi_app = DispatcherMiddleware(Response("Not Found", status=404), {"/admin": wsgi_app})

asgi_app = WsgiToAsgi(wsgi_app)
