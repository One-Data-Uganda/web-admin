import datetime
import json
import uuid

from app.core.config import settings
from app.core.logger import log
from app.services import FailureResponseModel
from app.services.api.accounting import models
from app.services.api.accounting.api_client import ApiClient, AsyncApis, SyncApis
from app.services.api.accounting.exceptions import UnexpectedResponse

client = ApiClient(host=settings.ACCOUNTING_SERVICE, timeout=240)
api = AsyncApis(client)
api_sync = SyncApis(client)


async def add(user_id: uuid.UUID, account_id: uuid.UUID, msisdn: str):
    try:
        r = await api.blacklist_api.create_blacklist(
            models.BlacklistCreate(
                account_id=account_id,
                msisdn=msisdn,
                created_at=datetime.datetime.now(),
                user_id=user_id,
            )
        )
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def delete(id: int):
    try:
        r = await api.blacklist_api.delete_blacklist(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def list(account_id: uuid.UUID):
    try:
        r = await api.blacklist_api.list_blacklists_for_account(account_id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def get(id: int):
    try:
        r = await api.blacklist_api.get_blacklist(id)

        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")
