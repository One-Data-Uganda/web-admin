import json

from app.core.config import settings
from app.core.logger import log
from app.services import FailureResponseModel
from app.services.api.user import models
from app.services.api.user.api_client import ApiClient, AsyncApis
from app.services.api.user.exceptions import UnexpectedResponse

client = ApiClient(host=settings.USER_SERVICE, timeout=30)
api = AsyncApis(client)


async def add(name: str, roles: list):
    try:
        body = models.AdminGroupCreate(name=name, roles=roles)
        r = await api.admin_group_api.create_admin_group(body)
        return r.body
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def update(id, name: str, roles: list):
    try:
        body = models.AdminGroupUpdate(name=name, roles=roles)

        r = await api.admin_group_api.update(id, body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def get(id):
    try:
        r = await api.admin_group_api.get_admin_group(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def delete(id):
    try:
        r = await api.admin_group_api.delete_admin_group(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def list():
    try:
        r = await api.admin_group_api.list_admin_groups()

        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")
