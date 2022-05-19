import datetime
import json
import uuid

from app.core.config import settings
from app.core.logger import log
from app.services import FailureResponseModel
from app.services.api.sms import models
from app.services.api.sms.api_client import ApiClient, AsyncApis, SyncApis
from app.services.api.sms.exceptions import UnexpectedResponse

client = ApiClient(host=settings.SMS_SERVICE, timeout=30)
api = AsyncApis(client)
api_sync = SyncApis(client)


async def add(
    account_id: uuid.UUID,
    keyword: str,
    keyword_type: str,
    alias_id: int,
    list_id: int,
    url: str,
    text: str,
):
    try:
        r = await api.keyword_api.create_keyword(
            models.KeywordCreate(
                account_id=account_id,
                keyword=keyword,
                keyword_type=keyword_type,
                alias_id=alias_id,
                list_id=list_id,
                url=url,
                text=text,
                status=0,
                active=False,
                created_at=datetime.datetime.now(),
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
        r = await api.keyword_api.delete_keyword(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def disable(id):
    try:
        r = await api.keyword_api.update_keyword(id, {"active": False})
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def enable(id):
    try:
        r = await api.keyword_api.update_keyword(id, {"active": True})
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def list(account_id: uuid.UUID):
    try:
        r = await api.keyword_api.list_keywords_for_account(account_id)
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None
