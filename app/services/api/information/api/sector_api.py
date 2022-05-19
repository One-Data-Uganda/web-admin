# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from app.services.api.information import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.information.api_client import ApiClient


class _SectorApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_sector(self, sector_create: m.SectorCreate) -> Awaitable[m.SectorResponse]:
        """
        Create new sector.
        """
        body = jsonable_encoder(sector_create)

        return self.api_client.request(type_=m.SectorResponse, method="POST", url="/v1/sector/", json=body)

    def _build_for_delete_sector(self, id: str) -> Awaitable[m.SectorResponse]:
        """
        Delete an sector.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.SectorResponse,
            method="DELETE",
            url="/v1/sector/{id}",
            path_params=path_params,
        )

    def _build_for_get_sector(self, id: str) -> Awaitable[m.SectorResponse]:
        """
        Get sector by ID.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.SectorResponse,
            method="GET",
            url="/v1/sector/{id}",
            path_params=path_params,
        )

    def _build_for_list_sectors(
        self,
    ) -> Awaitable[m.SectorListResponse]:
        """
        Retrieve sectors.
        """
        return self.api_client.request(
            type_=m.SectorListResponse,
            method="GET",
            url="/v1/sector/",
        )

    def _build_for_update_sector(self, id: str, sector_update: m.SectorUpdate) -> Awaitable[m.SectorResponse]:
        """
        Update a sector.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(sector_update)

        return self.api_client.request(
            type_=m.SectorResponse, method="PUT", url="/v1/sector/{id}", path_params=path_params, json=body
        )


class AsyncSectorApi(_SectorApi):
    async def create_sector(self, sector_create: m.SectorCreate) -> m.SectorResponse:
        """
        Create new sector.
        """
        return await self._build_for_create_sector(sector_create=sector_create)

    async def delete_sector(self, id: str) -> m.SectorResponse:
        """
        Delete an sector.
        """
        return await self._build_for_delete_sector(id=id)

    async def get_sector(self, id: str) -> m.SectorResponse:
        """
        Get sector by ID.
        """
        return await self._build_for_get_sector(id=id)

    async def list_sectors(
        self,
    ) -> m.SectorListResponse:
        """
        Retrieve sectors.
        """
        return await self._build_for_list_sectors()

    async def update_sector(self, id: str, sector_update: m.SectorUpdate) -> m.SectorResponse:
        """
        Update a sector.
        """
        return await self._build_for_update_sector(id=id, sector_update=sector_update)


class SyncSectorApi(_SectorApi):
    def create_sector(self, sector_create: m.SectorCreate) -> m.SectorResponse:
        """
        Create new sector.
        """
        coroutine = self._build_for_create_sector(sector_create=sector_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_sector(self, id: str) -> m.SectorResponse:
        """
        Delete an sector.
        """
        coroutine = self._build_for_delete_sector(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_sector(self, id: str) -> m.SectorResponse:
        """
        Get sector by ID.
        """
        coroutine = self._build_for_get_sector(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_sectors(
        self,
    ) -> m.SectorListResponse:
        """
        Retrieve sectors.
        """
        coroutine = self._build_for_list_sectors()
        return get_event_loop().run_until_complete(coroutine)

    def update_sector(self, id: str, sector_update: m.SectorUpdate) -> m.SectorResponse:
        """
        Update a sector.
        """
        coroutine = self._build_for_update_sector(id=id, sector_update=sector_update)
        return get_event_loop().run_until_complete(coroutine)
