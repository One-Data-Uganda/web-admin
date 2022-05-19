import json

from app.core.config import settings
from app.core.logger import log
from app.services import FailureResponseModel
from app.services.api.user import models
from app.services.api.user.api_client import ApiClient, AsyncApis, SyncApis
from app.services.api.user.exceptions import UnexpectedResponse

client = ApiClient(host=settings.USER_SERVICE, timeout=30)
api = AsyncApis(client)
api_sync = SyncApis(client)


async def add(name):
    try:
        r = await api.document_type_api.create_document_type(
            models.Document_TypeCreate(
                id=name,
            )
        )
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def delete(id):
    try:
        r = await api.document_type_api.delete_document_type(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def list():
    try:
        r = await api.document_type_api.list_document_types()
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


async def get(id):
    try:
        r = await api.document_type_api.get_document_type(id)

        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None
