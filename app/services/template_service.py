import json

from app.core.config import settings
from app.core.logger import log
from app.services import FailureResponseModel
from app.services.api.sms import models
from app.services.api.sms.api_client import ApiClient, AsyncApis, SyncApis
from app.services.api.sms.exceptions import UnexpectedResponse

client = ApiClient(host=settings.SMS_SERVICE, timeout=30)
api = AsyncApis(client)
api_sync = SyncApis(client)


async def add(account_id, name, details):
    try:
        r = await api.message_template_api.create_message_template(
            models.MessageTemplateCreate(
                name=name, account_id=account_id, details=details
            )
        )
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def update(id, name, details):
    try:
        r = await api.message_template_api.update_message_template(
            id, {"name": name, "details": details}
        )
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def get(id):
    try:
        r = await api.message_template_api.get_message_template(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def delete(id):
    try:
        r = await api.message_template_api.delete_message_template(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def list(account_id):
    try:
        r = await api.message_template_api.list_message_templates(account_id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")
