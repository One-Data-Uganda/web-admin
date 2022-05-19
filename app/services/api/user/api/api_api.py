# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable
from uuid import UUID

from app.services.api.user import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.user.api_client import ApiClient


class _ApiApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_auth_api(self, api_login: m.APILogin) -> Awaitable[m.APIAuthResponse]:
        """
        Authenticate API
        """
        body = jsonable_encoder(api_login)

        return self.api_client.request(type_=m.APIAuthResponse, method="POST", url="/v1/api/auth", json=body)

    def _build_for_create_api(self, api_new: m.APINew) -> Awaitable[m.APIResponse]:
        """
        Create new api.
        """
        body = jsonable_encoder(api_new)

        return self.api_client.request(type_=m.APIResponse, method="POST", url="/v1/api/", json=body)

    def _build_for_delete_api(self, id: UUID) -> Awaitable[m.APIResponse]:
        """
        Delete an api.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.APIResponse,
            method="DELETE",
            url="/v1/api/{id}",
            path_params=path_params,
        )

    def _build_for_disable_api(self, id: UUID) -> Awaitable[m.APIResponse]:
        """
        Disable api
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.APIResponse,
            method="PUT",
            url="/v1/api/{id}/disable",
            path_params=path_params,
        )

    def _build_for_enable_api(self, id: UUID) -> Awaitable[m.APIResponse]:
        """
        Enable api
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.APIResponse,
            method="PUT",
            url="/v1/api/{id}/enable",
            path_params=path_params,
        )

    def _build_for_get_api(self, id: UUID) -> Awaitable[m.APIResponse]:
        """
        Get an api.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.APIResponse,
            method="GET",
            url="/v1/api/{id}",
            path_params=path_params,
        )

    def _build_for_get_api_count(self, account_id: UUID) -> Awaitable[m.APICountResponse]:
        """
        Count API Keys
        """
        path_params = {"account_id": str(account_id)}

        return self.api_client.request(
            type_=m.APICountResponse,
            method="GET",
            url="/v1/api/{account_id}/count",
            path_params=path_params,
        )

    def _build_for_list_by_account_id(self, account_id: UUID) -> Awaitable[m.APIListResponse]:
        """
        List API Keys
        """
        path_params = {"account_id": str(account_id)}

        return self.api_client.request(
            type_=m.APIListResponse,
            method="GET",
            url="/v1/api/{account_id}/list",
            path_params=path_params,
        )


class AsyncApiApi(_ApiApi):
    async def auth_api(self, api_login: m.APILogin) -> m.APIAuthResponse:
        """
        Authenticate API
        """
        return await self._build_for_auth_api(api_login=api_login)

    async def create_api(self, api_new: m.APINew) -> m.APIResponse:
        """
        Create new api.
        """
        return await self._build_for_create_api(api_new=api_new)

    async def delete_api(self, id: UUID) -> m.APIResponse:
        """
        Delete an api.
        """
        return await self._build_for_delete_api(id=id)

    async def disable_api(self, id: UUID) -> m.APIResponse:
        """
        Disable api
        """
        return await self._build_for_disable_api(id=id)

    async def enable_api(self, id: UUID) -> m.APIResponse:
        """
        Enable api
        """
        return await self._build_for_enable_api(id=id)

    async def get_api(self, id: UUID) -> m.APIResponse:
        """
        Get an api.
        """
        return await self._build_for_get_api(id=id)

    async def get_api_count(self, account_id: UUID) -> m.APICountResponse:
        """
        Count API Keys
        """
        return await self._build_for_get_api_count(account_id=account_id)

    async def list_by_account_id(self, account_id: UUID) -> m.APIListResponse:
        """
        List API Keys
        """
        return await self._build_for_list_by_account_id(account_id=account_id)


class SyncApiApi(_ApiApi):
    def auth_api(self, api_login: m.APILogin) -> m.APIAuthResponse:
        """
        Authenticate API
        """
        coroutine = self._build_for_auth_api(api_login=api_login)
        return get_event_loop().run_until_complete(coroutine)

    def create_api(self, api_new: m.APINew) -> m.APIResponse:
        """
        Create new api.
        """
        coroutine = self._build_for_create_api(api_new=api_new)
        return get_event_loop().run_until_complete(coroutine)

    def delete_api(self, id: UUID) -> m.APIResponse:
        """
        Delete an api.
        """
        coroutine = self._build_for_delete_api(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def disable_api(self, id: UUID) -> m.APIResponse:
        """
        Disable api
        """
        coroutine = self._build_for_disable_api(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def enable_api(self, id: UUID) -> m.APIResponse:
        """
        Enable api
        """
        coroutine = self._build_for_enable_api(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_api(self, id: UUID) -> m.APIResponse:
        """
        Get an api.
        """
        coroutine = self._build_for_get_api(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_api_count(self, account_id: UUID) -> m.APICountResponse:
        """
        Count API Keys
        """
        coroutine = self._build_for_get_api_count(account_id=account_id)
        return get_event_loop().run_until_complete(coroutine)

    def list_by_account_id(self, account_id: UUID) -> m.APIListResponse:
        """
        List API Keys
        """
        coroutine = self._build_for_list_by_account_id(account_id=account_id)
        return get_event_loop().run_until_complete(coroutine)
