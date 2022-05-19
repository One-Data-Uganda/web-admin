import datetime
import json
from uuid import UUID

from app.core.config import settings
from app.core.logger import log
from app.services import FailureResponseModel
from app.services.api.sms import models
from app.services.api.sms.api_client import ApiClient, AsyncApis, SyncApis
from app.services.api.sms.exceptions import UnexpectedResponse

client = ApiClient(host=settings.SMS_SERVICE, timeout=30)
api = AsyncApis(client)
api_sync = SyncApis(client)


async def add(code, smsc_id):
    try:
        body = models.ShortcodeCreate(code=code, smsc_id=smsc_id)

        r = await api.shortcode_api.create_shortcode(body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def assign(
    id: int,
    account_id: UUID,
):
    try:
        body = models.ShortcodeUpdate(
            account_id=account_id, assign_date=datetime.datetime.now().date()
        )
        r = await api.shortcode_api.update_shortcode(id, body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def make_default(
    id: int,
):
    try:
        r = await api.shortcode_api.make_shortcode_default(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def revoke(
    id: int,
):
    try:
        r = await api.shortcode_api.revoke_shortcode(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def update(id: int, code: int, smsc_id: str):
    try:
        body = models.ShortcodeUpdate(code=code, smsc_id=smsc_id)
        r = await api.shortcode_api.update_shortcode(id, body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def get(id):
    try:
        r = await api.shortcode_api.get_shortcode(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def delete(id):
    try:
        r = await api.shortcode_api.delete_shortcode(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def list():
    try:
        r = await api.shortcode_api.list_shortcodes()
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def list_for_account(account_id):
    try:
        r = await api.shortcode_api.list_for_account(account_id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")
