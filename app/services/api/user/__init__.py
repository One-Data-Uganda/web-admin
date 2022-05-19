import inspect

from app.services.api.user import models
from app.services.api.user.api_client import ApiClient, AsyncApis, SyncApis  # noqa F401
from pydantic import BaseModel

for model in inspect.getmembers(models, inspect.isclass):
    if model[1].__module__ == "app.services.api.user.models":
        model_class = model[1]
        if isinstance(model_class, BaseModel) or hasattr(model_class, "update_forward_refs"):
            try:
                model_class.update_forward_refs()
            except Exception:
                pass
