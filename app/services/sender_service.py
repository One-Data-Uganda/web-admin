import datetime
import json

from flask_login import current_user

from app.core.config import settings
from app.core.logger import log
from app.services import FailureResponseModel
from app.services.api.sms import models
from app.services.api.sms.api_client import ApiClient, AsyncApis, SyncApis
from app.services.api.sms.exceptions import UnexpectedResponse

client = ApiClient(host=settings.SMS_SERVICE, timeout=30)
api = AsyncApis(client)
api_sync = SyncApis(client)


async def add(account_id, name):
    try:
        body = models.SenderCreate(
            account_id=account_id,
            name=name.strip(),
            status=0,
            user_id=current_user.id,
            date_submitted=datetime.datetime.now(),
            is_default=False,
        )

        r = await api.sender_api.create_sender(body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def make_default(id: int):
    try:
        r = await api.sender_api.set_sender_default(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def delete(id):
    try:
        r = await api.sender_api.delete_sender(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def get(id):
    try:
        r = await api.sender_api.get_sender(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def list(account_id):
    try:
        r = await api.sender_api.get_senders_for_account(account_id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")
