import json
from uuid import UUID

from app.core.config import settings
from app.core.logger import log
from app.services.api.user import models  # noqa
from app.services.api.user.api_client import ApiClient, AsyncApis
from app.services.api.user.exceptions import UnexpectedResponse

client = ApiClient(host=settings.USER_SERVICE, timeout=30)
api = AsyncApis(client)


async def set(user_id: UUID, name: str, value: str):
    data = models.UserPreferenceCreate(
        user_id=user_id,
        name=name,
        value=value,
    )
    try:
        r = await api.user_preference_api.set_user_preference(data)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return models.FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return models.FailureResponseModel(success=False, message="System Error")


async def delete(user_id: UUID, name: str):
    try:
        r = await api.user_preference_api.delete_preference(user_id=user_id, name=name)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return models.FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return models.FailureResponseModel(success=False, message="System Error")


async def list(user_id: UUID):
    try:
        r = await api.user_preference_api.list_preferences(user_id=user_id)
        return r
    except UnexpectedResponse as e:
        return models.UserPreferenceResponse(success=True, data=None)
    except Exception as e:
        log.error(e, exc_info=True)
        return models.UserPreferenceResponse(success=True, data=None)
