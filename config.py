import os
from datetime import timedelta

import redis

basedir = os.path.dirname(__file__)


class Config(object):
    DEBUG = False
    TESTING = False
    APPLICATION_ROOT = "/admin"
    PROPAGATE_EXCEPTIONS = True
    SECRET_KEY = os.environ.get(
        "SECRET_KEY", "7vjr7UZb6WEhJY9Hme5mJSBXmhLKmXSb3KY79Ju2FLEmWjMB9utnnRPhCz9HjdJH"
    )
    PDF_FOLDER = f"{basedir}/static/data/pdf/"
    UPLOADS_DEFAULT_DEST = f"{basedir}/static/data/uploads/"
    THUMBNAIL_MEDIA_ROOT = f"{basedir}/static/data/uploads/userimages"
    THUMBNAIL_MEDIA_URL = f"{APPLICATION_ROOT}/static/data/uploads/userimages/"
    THUMBNAIL_MEDIA_THUMBNAIL_ROOT = THUMBNAIL_MEDIA_ROOT
    THUMBNAIL_MEDIA_THUMBNAIL_URL = THUMBNAIL_MEDIA_URL
    THUMBNAIL_STORAGE_BACKEND = (
        "flask_thumbnails.storage_backends.FilesystemStorageBackend"
    )
    THUMBNAIL_DEFAULT_FORMAT = "JPEG"

    WTF_CSRF_TIME_LIMIT = None
    # Flask-Session
    SESSION_KEY_PREFIX = "sms-admin:"
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=180)
    SESSION_REFRESH_EACH_REQUEST = True
    REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
    REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}", db=3)

    DEFAULT_SENDER_ID = os.environ.get("DEFAULT_SENDER_ID", "FDI")


class DevelopmentConfig(Config):
    DEBUG = True
    EXPLAIN_TEMPLATE_LOADING = False


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


config = {"dev": DevelopmentConfig, "test": TestingConfig, "prod": ProductionConfig}
