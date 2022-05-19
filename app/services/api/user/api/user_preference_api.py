# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable
from uuid import UUID

from app.services.api.user import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.user.api_client import ApiClient


class _UserPreferenceApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_delete_preference(self, user_id: UUID, name: str) -> Awaitable[m.UserPreferenceResponse]:
        """
        Delete user_preference
        """
        path_params = {"user_id": str(user_id), "name": str(name)}

        return self.api_client.request(
            type_=m.UserPreferenceResponse,
            method="DELETE",
            url="/v1/user-preference/{user_id}/{name}",
            path_params=path_params,
        )

    def _build_for_get_preference(self, user_id: UUID, name: str) -> Awaitable[m.UserPreferenceResponse]:
        """
        Get a specific user_preference by id.
        """
        path_params = {"user_id": str(user_id), "name": str(name)}

        return self.api_client.request(
            type_=m.UserPreferenceResponse,
            method="GET",
            url="/v1/user-preference/{user_id}/{name}",
            path_params=path_params,
        )

    def _build_for_list_preferences(self, user_id: UUID) -> Awaitable[m.UserPreferenceListResponse]:
        """
        Get a specific user_preference by id.
        """
        path_params = {"user_id": str(user_id)}

        return self.api_client.request(
            type_=m.UserPreferenceListResponse,
            method="GET",
            url="/v1/user-preference/{user_id}",
            path_params=path_params,
        )

    def _build_for_set_user_preference(
        self, user_preference_create: m.UserPreferenceCreate
    ) -> Awaitable[m.UserPreferenceResponse]:
        """
        Create new user preference.
        """
        body = jsonable_encoder(user_preference_create)

        return self.api_client.request(
            type_=m.UserPreferenceResponse, method="POST", url="/v1/user-preference/", json=body
        )


class AsyncUserPreferenceApi(_UserPreferenceApi):
    async def delete_preference(self, user_id: UUID, name: str) -> m.UserPreferenceResponse:
        """
        Delete user_preference
        """
        return await self._build_for_delete_preference(user_id=user_id, name=name)

    async def get_preference(self, user_id: UUID, name: str) -> m.UserPreferenceResponse:
        """
        Get a specific user_preference by id.
        """
        return await self._build_for_get_preference(user_id=user_id, name=name)

    async def list_preferences(self, user_id: UUID) -> m.UserPreferenceListResponse:
        """
        Get a specific user_preference by id.
        """
        return await self._build_for_list_preferences(user_id=user_id)

    async def set_user_preference(self, user_preference_create: m.UserPreferenceCreate) -> m.UserPreferenceResponse:
        """
        Create new user preference.
        """
        return await self._build_for_set_user_preference(user_preference_create=user_preference_create)


class SyncUserPreferenceApi(_UserPreferenceApi):
    def delete_preference(self, user_id: UUID, name: str) -> m.UserPreferenceResponse:
        """
        Delete user_preference
        """
        coroutine = self._build_for_delete_preference(user_id=user_id, name=name)
        return get_event_loop().run_until_complete(coroutine)

    def get_preference(self, user_id: UUID, name: str) -> m.UserPreferenceResponse:
        """
        Get a specific user_preference by id.
        """
        coroutine = self._build_for_get_preference(user_id=user_id, name=name)
        return get_event_loop().run_until_complete(coroutine)

    def list_preferences(self, user_id: UUID) -> m.UserPreferenceListResponse:
        """
        Get a specific user_preference by id.
        """
        coroutine = self._build_for_list_preferences(user_id=user_id)
        return get_event_loop().run_until_complete(coroutine)

    def set_user_preference(self, user_preference_create: m.UserPreferenceCreate) -> m.UserPreferenceResponse:
        """
        Create new user preference.
        """
        coroutine = self._build_for_set_user_preference(user_preference_create=user_preference_create)
        return get_event_loop().run_until_complete(coroutine)
