# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from app.services.api.information import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.information.api_client import ApiClient


class _SectorGroupApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_sector_group(
        self, sector_group_create: m.SectorGroupCreate
    ) -> Awaitable[m.SectorGroupResponse]:
        """
        Create new sector_group.
        """
        body = jsonable_encoder(sector_group_create)

        return self.api_client.request(type_=m.SectorGroupResponse, method="POST", url="/v1/sector-group/", json=body)

    def _build_for_delete_sector_group(self, id: str) -> Awaitable[m.SectorGroupResponse]:
        """
        Delete an sector_group.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.SectorGroupResponse,
            method="DELETE",
            url="/v1/sector-group/{id}",
            path_params=path_params,
        )

    def _build_for_get_sector_group(self, id: str) -> Awaitable[m.SectorGroupResponse]:
        """
        Get sector_group by ID.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.SectorGroupResponse,
            method="GET",
            url="/v1/sector-group/{id}",
            path_params=path_params,
        )

    def _build_for_list_sector_groups(
        self,
    ) -> Awaitable[m.SectorGroupListResponse]:
        """
        Retrieve sector_groups.
        """
        return self.api_client.request(
            type_=m.SectorGroupListResponse,
            method="GET",
            url="/v1/sector-group/",
        )

    def _build_for_update_sector_group(
        self, id: str, sector_group_update: m.SectorGroupUpdate
    ) -> Awaitable[m.SectorGroupResponse]:
        """
        Update a sector_group.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(sector_group_update)

        return self.api_client.request(
            type_=m.SectorGroupResponse, method="PUT", url="/v1/sector-group/{id}", path_params=path_params, json=body
        )


class AsyncSectorGroupApi(_SectorGroupApi):
    async def create_sector_group(self, sector_group_create: m.SectorGroupCreate) -> m.SectorGroupResponse:
        """
        Create new sector_group.
        """
        return await self._build_for_create_sector_group(sector_group_create=sector_group_create)

    async def delete_sector_group(self, id: str) -> m.SectorGroupResponse:
        """
        Delete an sector_group.
        """
        return await self._build_for_delete_sector_group(id=id)

    async def get_sector_group(self, id: str) -> m.SectorGroupResponse:
        """
        Get sector_group by ID.
        """
        return await self._build_for_get_sector_group(id=id)

    async def list_sector_groups(
        self,
    ) -> m.SectorGroupListResponse:
        """
        Retrieve sector_groups.
        """
        return await self._build_for_list_sector_groups()

    async def update_sector_group(self, id: str, sector_group_update: m.SectorGroupUpdate) -> m.SectorGroupResponse:
        """
        Update a sector_group.
        """
        return await self._build_for_update_sector_group(id=id, sector_group_update=sector_group_update)


class SyncSectorGroupApi(_SectorGroupApi):
    def create_sector_group(self, sector_group_create: m.SectorGroupCreate) -> m.SectorGroupResponse:
        """
        Create new sector_group.
        """
        coroutine = self._build_for_create_sector_group(sector_group_create=sector_group_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_sector_group(self, id: str) -> m.SectorGroupResponse:
        """
        Delete an sector_group.
        """
        coroutine = self._build_for_delete_sector_group(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_sector_group(self, id: str) -> m.SectorGroupResponse:
        """
        Get sector_group by ID.
        """
        coroutine = self._build_for_get_sector_group(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_sector_groups(
        self,
    ) -> m.SectorGroupListResponse:
        """
        Retrieve sector_groups.
        """
        coroutine = self._build_for_list_sector_groups()
        return get_event_loop().run_until_complete(coroutine)

    def update_sector_group(self, id: str, sector_group_update: m.SectorGroupUpdate) -> m.SectorGroupResponse:
        """
        Update a sector_group.
        """
        coroutine = self._build_for_update_sector_group(id=id, sector_group_update=sector_group_update)
        return get_event_loop().run_until_complete(coroutine)
