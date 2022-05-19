# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from app.services.api.user import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.user.api_client import ApiClient


class _AdminGroupApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_admin_group(self, admin_group_create: m.AdminGroupCreate) -> Awaitable[m.AdminGroupResponse]:
        """
        Create new admin group.
        """
        body = jsonable_encoder(admin_group_create)

        return self.api_client.request(type_=m.AdminGroupResponse, method="POST", url="/v1/admin-group/", json=body)

    def _build_for_delete_admin_group(self, id: int) -> Awaitable[m.AdminGroupResponse]:
        """
        Delete admin_group
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.AdminGroupResponse,
            method="DELETE",
            url="/v1/admin-group/{id}",
            path_params=path_params,
        )

    def _build_for_get_admin_group(self, id: int) -> Awaitable[m.AdminGroupResponse]:
        """
        Get a specific admin_group by id.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.AdminGroupResponse,
            method="GET",
            url="/v1/admin-group/{id}",
            path_params=path_params,
        )

    def _build_for_list_admin_groups(
        self,
    ) -> Awaitable[m.AdminGroupListResponse]:
        """
        Admin Group listing
        """
        return self.api_client.request(
            type_=m.AdminGroupListResponse,
            method="GET",
            url="/v1/admin-group/",
        )

    def _build_for_update_admin_group(
        self, id: int, admin_group_update: m.AdminGroupUpdate
    ) -> Awaitable[m.AdminGroupResponse]:
        """
        Update a admin_group.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(admin_group_update)

        return self.api_client.request(
            type_=m.AdminGroupResponse, method="PUT", url="/v1/admin-group/{id}", path_params=path_params, json=body
        )


class AsyncAdminGroupApi(_AdminGroupApi):
    async def create_admin_group(self, admin_group_create: m.AdminGroupCreate) -> m.AdminGroupResponse:
        """
        Create new admin group.
        """
        return await self._build_for_create_admin_group(admin_group_create=admin_group_create)

    async def delete_admin_group(self, id: int) -> m.AdminGroupResponse:
        """
        Delete admin_group
        """
        return await self._build_for_delete_admin_group(id=id)

    async def get_admin_group(self, id: int) -> m.AdminGroupResponse:
        """
        Get a specific admin_group by id.
        """
        return await self._build_for_get_admin_group(id=id)

    async def list_admin_groups(
        self,
    ) -> m.AdminGroupListResponse:
        """
        Admin Group listing
        """
        return await self._build_for_list_admin_groups()

    async def update_admin_group(self, id: int, admin_group_update: m.AdminGroupUpdate) -> m.AdminGroupResponse:
        """
        Update a admin_group.
        """
        return await self._build_for_update_admin_group(id=id, admin_group_update=admin_group_update)


class SyncAdminGroupApi(_AdminGroupApi):
    def create_admin_group(self, admin_group_create: m.AdminGroupCreate) -> m.AdminGroupResponse:
        """
        Create new admin group.
        """
        coroutine = self._build_for_create_admin_group(admin_group_create=admin_group_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_admin_group(self, id: int) -> m.AdminGroupResponse:
        """
        Delete admin_group
        """
        coroutine = self._build_for_delete_admin_group(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_admin_group(self, id: int) -> m.AdminGroupResponse:
        """
        Get a specific admin_group by id.
        """
        coroutine = self._build_for_get_admin_group(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_admin_groups(
        self,
    ) -> m.AdminGroupListResponse:
        """
        Admin Group listing
        """
        coroutine = self._build_for_list_admin_groups()
        return get_event_loop().run_until_complete(coroutine)

    def update_admin_group(self, id: int, admin_group_update: m.AdminGroupUpdate) -> m.AdminGroupResponse:
        """
        Update a admin_group.
        """
        coroutine = self._build_for_update_admin_group(id=id, admin_group_update=admin_group_update)
        return get_event_loop().run_until_complete(coroutine)
