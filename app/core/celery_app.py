from celery import Celery

from app.core.config import settings

celery_app = Celery(
    "worker", backend=settings.CELERY_BACKEND, broker=settings.CELERY_BROKER
)

celery_app.conf.task_routes = {"web.*": {"queue": "web"}}

celery_app.conf.task_serializer = "pickle"
celery_app.conf.result_serializer = "pickle"
celery_app.conf.accept_content = ["json", "pickle"]

celery_app.conf.enable_utc = False
