# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from app.services.api.user import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.user.api_client import ApiClient


class _RoleApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_role(self, role_create: m.RoleCreate) -> Awaitable[m.RoleResponse]:
        """
        Create new role.
        """
        body = jsonable_encoder(role_create)

        return self.api_client.request(type_=m.RoleResponse, method="POST", url="/v1/role/", json=body)

    def _build_for_delete_role(self, role_id: str) -> Awaitable[m.RoleResponse]:
        """
        Delete a role.
        """
        path_params = {"role_id": str(role_id)}

        return self.api_client.request(
            type_=m.RoleResponse,
            method="DELETE",
            url="/v1/role/{role_id}",
            path_params=path_params,
        )

    def _build_for_list_roles(
        self,
    ) -> Awaitable[m.RoleListResponse]:
        """
        Get all roles
        """
        return self.api_client.request(
            type_=m.RoleListResponse,
            method="GET",
            url="/v1/role/",
        )

    def _build_for_update_role(self, id: str, role_update: m.RoleUpdate) -> Awaitable[m.RoleResponse]:
        """
        Update role
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(role_update)

        return self.api_client.request(
            type_=m.RoleResponse, method="PUT", url="/v1/role/{id}", path_params=path_params, json=body
        )


class AsyncRoleApi(_RoleApi):
    async def create_role(self, role_create: m.RoleCreate) -> m.RoleResponse:
        """
        Create new role.
        """
        return await self._build_for_create_role(role_create=role_create)

    async def delete_role(self, role_id: str) -> m.RoleResponse:
        """
        Delete a role.
        """
        return await self._build_for_delete_role(role_id=role_id)

    async def list_roles(
        self,
    ) -> m.RoleListResponse:
        """
        Get all roles
        """
        return await self._build_for_list_roles()

    async def update_role(self, id: str, role_update: m.RoleUpdate) -> m.RoleResponse:
        """
        Update role
        """
        return await self._build_for_update_role(id=id, role_update=role_update)


class SyncRoleApi(_RoleApi):
    def create_role(self, role_create: m.RoleCreate) -> m.RoleResponse:
        """
        Create new role.
        """
        coroutine = self._build_for_create_role(role_create=role_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_role(self, role_id: str) -> m.RoleResponse:
        """
        Delete a role.
        """
        coroutine = self._build_for_delete_role(role_id=role_id)
        return get_event_loop().run_until_complete(coroutine)

    def list_roles(
        self,
    ) -> m.RoleListResponse:
        """
        Get all roles
        """
        coroutine = self._build_for_list_roles()
        return get_event_loop().run_until_complete(coroutine)

    def update_role(self, id: str, role_update: m.RoleUpdate) -> m.RoleResponse:
        """
        Update role
        """
        coroutine = self._build_for_update_role(id=id, role_update=role_update)
        return get_event_loop().run_until_complete(coroutine)
