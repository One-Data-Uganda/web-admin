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


async def send(user, identifier):
    try:
        body = models.MTRedis(identifier=identifier, user=user)
        log.debug(body)
        r = await api.mt_api.post_redis_mt(body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def mtJSON(account_id, params):
    try:
        r = await api.mt_api.mt_json(account_id, params)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def task(task_id):
    try:
        r = await api.tasks_api.get_task_state(task_id)
        return r
    except UnexpectedResponse as e:
        return json.loads(e.content)
    except Exception as e:
        log.error(e, exc_info=True)
        return {"success": False, "message": "System Error"}


async def mtGraph(params):
    try:
        r = await api.mt_api.mt_graph(params)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")
