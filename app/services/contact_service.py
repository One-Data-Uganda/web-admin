import json

from app.core.config import settings
from app.core.logger import log
from app.services import FailureResponseModel
from app.services.api.sms.api_client import ApiClient, AsyncApis, SyncApis
from app.services.api.sms.exceptions import UnexpectedResponse

client = ApiClient(host=settings.SMS_SERVICE, timeout=240)
api = AsyncApis(client)
api_sync = SyncApis(client)


async def delete(id):
    try:
        r = await api.contact_api.delete_contact(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def list(list_id):
    try:
        r = await api.contact_api.list_contacts(list_id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def listJSON(list_id, params):
    try:
        r = await api.contact_api.list_contacts_json(list_id, params)
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return []
