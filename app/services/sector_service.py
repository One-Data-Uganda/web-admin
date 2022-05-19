import json

from app.core.config import settings
from app.core.logger import log
from app.services import FailureResponseModel
from app.services.api.information import models
from app.services.api.information.api_client import ApiClient, AsyncApis, SyncApis
from app.services.api.information.exceptions import UnexpectedResponse

client = ApiClient(host=settings.INFORMATION_SERVICE, timeout=30)
api = AsyncApis(client)
api_sync = SyncApis(client)


async def sectors():
    try:
        r = await api.sector_api.list_sectors()
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


async def sector_industries():
    try:
        r = await api.sector_industry_api.list_sector_industries()
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


async def sector_groups():
    try:
        r = await api.sector_industry_api.list_sector_groups()
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


async def sector_divisions():
    try:
        r = await api.sector_industry_api.list_sector_divisions()
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None
