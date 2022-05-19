# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from app.services.api.information import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.information.api_client import ApiClient


class _SectorIndustryApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_sector_industry(
        self, sector_industry_create: m.SectorIndustryCreate
    ) -> Awaitable[m.SectorIndustryResponse]:
        """
        Create new sector_industry.
        """
        body = jsonable_encoder(sector_industry_create)

        return self.api_client.request(
            type_=m.SectorIndustryResponse, method="POST", url="/v1/sector-industry/", json=body
        )

    def _build_for_delete_sector_industry(self, id: str) -> Awaitable[m.SectorIndustryResponse]:
        """
        Delete an sector_industry.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.SectorIndustryResponse,
            method="DELETE",
            url="/v1/sector-industry/{id}",
            path_params=path_params,
        )

    def _build_for_get_sector_industry(self, id: str) -> Awaitable[m.SectorIndustryResponse]:
        """
        Get sector_industry by ID.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.SectorIndustryResponse,
            method="GET",
            url="/v1/sector-industry/{id}",
            path_params=path_params,
        )

    def _build_for_list_sector_industries(
        self,
    ) -> Awaitable[m.SectorIndustryListResponse]:
        """
        Retrieve sector_industrys.
        """
        return self.api_client.request(
            type_=m.SectorIndustryListResponse,
            method="GET",
            url="/v1/sector-industry/",
        )

    def _build_for_update_sector_industry(
        self, id: str, sector_industry_update: m.SectorIndustryUpdate
    ) -> Awaitable[m.SectorIndustryResponse]:
        """
        Update a sector_industry.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(sector_industry_update)

        return self.api_client.request(
            type_=m.SectorIndustryResponse,
            method="PUT",
            url="/v1/sector-industry/{id}",
            path_params=path_params,
            json=body,
        )


class AsyncSectorIndustryApi(_SectorIndustryApi):
    async def create_sector_industry(self, sector_industry_create: m.SectorIndustryCreate) -> m.SectorIndustryResponse:
        """
        Create new sector_industry.
        """
        return await self._build_for_create_sector_industry(sector_industry_create=sector_industry_create)

    async def delete_sector_industry(self, id: str) -> m.SectorIndustryResponse:
        """
        Delete an sector_industry.
        """
        return await self._build_for_delete_sector_industry(id=id)

    async def get_sector_industry(self, id: str) -> m.SectorIndustryResponse:
        """
        Get sector_industry by ID.
        """
        return await self._build_for_get_sector_industry(id=id)

    async def list_sector_industries(
        self,
    ) -> m.SectorIndustryListResponse:
        """
        Retrieve sector_industrys.
        """
        return await self._build_for_list_sector_industries()

    async def update_sector_industry(
        self, id: str, sector_industry_update: m.SectorIndustryUpdate
    ) -> m.SectorIndustryResponse:
        """
        Update a sector_industry.
        """
        return await self._build_for_update_sector_industry(id=id, sector_industry_update=sector_industry_update)


class SyncSectorIndustryApi(_SectorIndustryApi):
    def create_sector_industry(self, sector_industry_create: m.SectorIndustryCreate) -> m.SectorIndustryResponse:
        """
        Create new sector_industry.
        """
        coroutine = self._build_for_create_sector_industry(sector_industry_create=sector_industry_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_sector_industry(self, id: str) -> m.SectorIndustryResponse:
        """
        Delete an sector_industry.
        """
        coroutine = self._build_for_delete_sector_industry(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_sector_industry(self, id: str) -> m.SectorIndustryResponse:
        """
        Get sector_industry by ID.
        """
        coroutine = self._build_for_get_sector_industry(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_sector_industries(
        self,
    ) -> m.SectorIndustryListResponse:
        """
        Retrieve sector_industrys.
        """
        coroutine = self._build_for_list_sector_industries()
        return get_event_loop().run_until_complete(coroutine)

    def update_sector_industry(
        self, id: str, sector_industry_update: m.SectorIndustryUpdate
    ) -> m.SectorIndustryResponse:
        """
        Update a sector_industry.
        """
        coroutine = self._build_for_update_sector_industry(id=id, sector_industry_update=sector_industry_update)
        return get_event_loop().run_until_complete(coroutine)
