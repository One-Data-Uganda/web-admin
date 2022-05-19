# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from app.services.api.information import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.information.api_client import ApiClient


class _SectorDivisionApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_sector_division(
        self, sector_division_create: m.SectorDivisionCreate
    ) -> Awaitable[m.SectorDivisionResponse]:
        """
        Create new sector_division.
        """
        body = jsonable_encoder(sector_division_create)

        return self.api_client.request(
            type_=m.SectorDivisionResponse, method="POST", url="/v1/sector-division/", json=body
        )

    def _build_for_delete_sector_division(self, id: str) -> Awaitable[m.SectorDivisionResponse]:
        """
        Delete an sector_division.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.SectorDivisionResponse,
            method="DELETE",
            url="/v1/sector-division/{id}",
            path_params=path_params,
        )

    def _build_for_get_sector_division(self, id: str) -> Awaitable[m.SectorDivisionResponse]:
        """
        Get sector_division by ID.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.SectorDivisionResponse,
            method="GET",
            url="/v1/sector-division/{id}",
            path_params=path_params,
        )

    def _build_for_list_sector_divisions(
        self,
    ) -> Awaitable[m.SectorDivisionListResponse]:
        """
        Retrieve sector_divisions.
        """
        return self.api_client.request(
            type_=m.SectorDivisionListResponse,
            method="GET",
            url="/v1/sector-division/",
        )

    def _build_for_update_sector_division(
        self, id: str, sector_division_update: m.SectorDivisionUpdate
    ) -> Awaitable[m.SectorDivisionResponse]:
        """
        Update a sector_division.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(sector_division_update)

        return self.api_client.request(
            type_=m.SectorDivisionResponse,
            method="PUT",
            url="/v1/sector-division/{id}",
            path_params=path_params,
            json=body,
        )


class AsyncSectorDivisionApi(_SectorDivisionApi):
    async def create_sector_division(self, sector_division_create: m.SectorDivisionCreate) -> m.SectorDivisionResponse:
        """
        Create new sector_division.
        """
        return await self._build_for_create_sector_division(sector_division_create=sector_division_create)

    async def delete_sector_division(self, id: str) -> m.SectorDivisionResponse:
        """
        Delete an sector_division.
        """
        return await self._build_for_delete_sector_division(id=id)

    async def get_sector_division(self, id: str) -> m.SectorDivisionResponse:
        """
        Get sector_division by ID.
        """
        return await self._build_for_get_sector_division(id=id)

    async def list_sector_divisions(
        self,
    ) -> m.SectorDivisionListResponse:
        """
        Retrieve sector_divisions.
        """
        return await self._build_for_list_sector_divisions()

    async def update_sector_division(
        self, id: str, sector_division_update: m.SectorDivisionUpdate
    ) -> m.SectorDivisionResponse:
        """
        Update a sector_division.
        """
        return await self._build_for_update_sector_division(id=id, sector_division_update=sector_division_update)


class SyncSectorDivisionApi(_SectorDivisionApi):
    def create_sector_division(self, sector_division_create: m.SectorDivisionCreate) -> m.SectorDivisionResponse:
        """
        Create new sector_division.
        """
        coroutine = self._build_for_create_sector_division(sector_division_create=sector_division_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_sector_division(self, id: str) -> m.SectorDivisionResponse:
        """
        Delete an sector_division.
        """
        coroutine = self._build_for_delete_sector_division(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_sector_division(self, id: str) -> m.SectorDivisionResponse:
        """
        Get sector_division by ID.
        """
        coroutine = self._build_for_get_sector_division(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_sector_divisions(
        self,
    ) -> m.SectorDivisionListResponse:
        """
        Retrieve sector_divisions.
        """
        coroutine = self._build_for_list_sector_divisions()
        return get_event_loop().run_until_complete(coroutine)

    def update_sector_division(
        self, id: str, sector_division_update: m.SectorDivisionUpdate
    ) -> m.SectorDivisionResponse:
        """
        Update a sector_division.
        """
        coroutine = self._build_for_update_sector_division(id=id, sector_division_update=sector_division_update)
        return get_event_loop().run_until_complete(coroutine)
