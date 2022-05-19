# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable
from uuid import UUID

from app.services.api.user import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.user.api_client import ApiClient


class _GroupApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_account_group(
        self, account_group_create: m.AccountGroupCreate
    ) -> Awaitable[m.AccountGroupResponse]:
        """
        Create new account group.
        """
        body = jsonable_encoder(account_group_create)

        return self.api_client.request(type_=m.AccountGroupResponse, method="POST", url="/v1/group/", json=body)

    def _build_for_delete_account_group(self, id: int) -> Awaitable[m.AccountGroupResponse]:
        """
        Delete account_group
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.AccountGroupResponse,
            method="DELETE",
            url="/v1/group/{id}",
            path_params=path_params,
        )

    def _build_for_get_account_group(self, id: int) -> Awaitable[m.AccountGroupResponse]:
        """
        Get a specific account_group by id.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.AccountGroupResponse,
            method="GET",
            url="/v1/group/{id}",
            path_params=path_params,
        )

    def _build_for_list_account_groups(self, account_id: UUID) -> Awaitable[m.AccountGroupListResponse]:
        """
        Account Group listing
        """
        path_params = {"account_id": str(account_id)}

        return self.api_client.request(
            type_=m.AccountGroupListResponse,
            method="GET",
            url="/v1/group/account/{account_id}",
            path_params=path_params,
        )

    def _build_for_update_account_group(
        self, id: int, account_group_update: m.AccountGroupUpdate
    ) -> Awaitable[m.AccountGroupResponse]:
        """
        Update a account_group.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(account_group_update)

        return self.api_client.request(
            type_=m.AccountGroupResponse, method="PUT", url="/v1/group/{id}", path_params=path_params, json=body
        )


class AsyncGroupApi(_GroupApi):
    async def create_account_group(self, account_group_create: m.AccountGroupCreate) -> m.AccountGroupResponse:
        """
        Create new account group.
        """
        return await self._build_for_create_account_group(account_group_create=account_group_create)

    async def delete_account_group(self, id: int) -> m.AccountGroupResponse:
        """
        Delete account_group
        """
        return await self._build_for_delete_account_group(id=id)

    async def get_account_group(self, id: int) -> m.AccountGroupResponse:
        """
        Get a specific account_group by id.
        """
        return await self._build_for_get_account_group(id=id)

    async def list_account_groups(self, account_id: UUID) -> m.AccountGroupListResponse:
        """
        Account Group listing
        """
        return await self._build_for_list_account_groups(account_id=account_id)

    async def update_account_group(self, id: int, account_group_update: m.AccountGroupUpdate) -> m.AccountGroupResponse:
        """
        Update a account_group.
        """
        return await self._build_for_update_account_group(id=id, account_group_update=account_group_update)


class SyncGroupApi(_GroupApi):
    def create_account_group(self, account_group_create: m.AccountGroupCreate) -> m.AccountGroupResponse:
        """
        Create new account group.
        """
        coroutine = self._build_for_create_account_group(account_group_create=account_group_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_account_group(self, id: int) -> m.AccountGroupResponse:
        """
        Delete account_group
        """
        coroutine = self._build_for_delete_account_group(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_account_group(self, id: int) -> m.AccountGroupResponse:
        """
        Get a specific account_group by id.
        """
        coroutine = self._build_for_get_account_group(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_account_groups(self, account_id: UUID) -> m.AccountGroupListResponse:
        """
        Account Group listing
        """
        coroutine = self._build_for_list_account_groups(account_id=account_id)
        return get_event_loop().run_until_complete(coroutine)

    def update_account_group(self, id: int, account_group_update: m.AccountGroupUpdate) -> m.AccountGroupResponse:
        """
        Update a account_group.
        """
        coroutine = self._build_for_update_account_group(id=id, account_group_update=account_group_update)
        return get_event_loop().run_until_complete(coroutine)
