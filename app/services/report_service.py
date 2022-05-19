import json
import uuid

from app.core.config import settings
from app.core.logger import log
from app.services import FailureResponseModel
from app.services.api.reporting.api_client import ApiClient, AsyncApis, SyncApis
from app.services.api.user.exceptions import UnexpectedResponse

client = ApiClient(host=settings.REPORTING_SERVICE, timeout=240)
api = AsyncApis(client)
api_sync = SyncApis(client)


async def mtJSON(account_id: uuid.UUID, params: dict):
    try:
        r = await api.mt_api.mt_report(account_id, params)
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return {}


async def moJSON(account_id: uuid.UUID, params: dict):
    try:
        r = await api.mo_api.mo_report(account_id, params)
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return {}


async def mtSummaryJSON(account_id: uuid.UUID, params: dict):
    try:
        r = await api.mt_api.mt_summary(account_id, params)
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return {}


async def mtLightJSON(account_id: uuid.UUID, params: dict):
    try:
        r = await api.mt_api.mt_report_light(account_id, params)
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return {}


async def mtGraph(params: dict):
    try:
        r = await api.mt_api.mt_graph(params)
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return {}


async def moGraph(params: dict):
    try:
        r = await api.mo_api.mo_graph(params)
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return {}


async def outboxJSON(account_id: uuid.UUID, params: dict):
    try:
        r = await api.general_api.outbox_json(account_id, params)
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return {}


async def keywordPerformanceJSON(account_id: uuid.UUID, params: dict):
    try:
        r = await api.general_api.keyword_performance_json(account_id, params)
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return {}


async def get_statement(account_id, account_name, from_date, to_date, email):
    try:
        body = {
            "account_id": account_id,
            "account_name": account_name,
            "from_date": from_date,
            "to_date": to_date,
            "email": email,
        }
        r = await api.statement_api.get_statement(body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")
