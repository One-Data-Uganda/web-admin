from app.core.config import settings
from app.core.logger import log
from app.services.api.user.api_client import ApiClient, AsyncApis, SyncApis

client = ApiClient(host=settings.USER_SERVICE, timeout=30)
api = AsyncApis(client)
api_sync = SyncApis(client)


async def country_list():
    try:
        r = await api.country_api.list_countries()
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


async def country(country_id: str):
    try:
        r = await api.country_api.get_country(country_id)

        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


async def role_list():
    try:
        r = await api.role_api.list_roles()
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


async def role(role_id):
    try:
        r = await api.role_api.get_role(role_id)

        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None
