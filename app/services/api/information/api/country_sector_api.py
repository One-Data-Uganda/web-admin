# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable, List

from app.services.api.information import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.information.api_client import ApiClient


class _CountrySectorApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_country_sector(
        self, country_sector_create: m.CountrySectorCreate
    ) -> Awaitable[m.CountrySector]:
        """
        Create new country_sector.
        """
        body = jsonable_encoder(country_sector_create)

        return self.api_client.request(type_=m.CountrySector, method="POST", url="/v1/country-sector/", json=body)

    def _build_for_delete_country_sector(self, id: str) -> Awaitable[m.CountrySector]:
        """
        Delete an country_sector.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.CountrySector,
            method="DELETE",
            url="/v1/country-sector/{id}",
            path_params=path_params,
        )

    def _build_for_get_country_sector(self, id: str) -> Awaitable[m.CountrySector]:
        """
        Get country_sector by ID.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.CountrySector,
            method="GET",
            url="/v1/country-sector/{id}",
            path_params=path_params,
        )

    def _build_for_list_country_sectors(
        self,
    ) -> Awaitable[List[m.CountrySector]]:
        """
        Retrieve country_sectors.
        """
        return self.api_client.request(
            type_=List[m.CountrySector],
            method="GET",
            url="/v1/country-sector/",
        )

    def _build_for_update_country_sector(
        self, id: str, country_sector_update: m.CountrySectorUpdate
    ) -> Awaitable[m.CountrySector]:
        """
        Update a country_sector.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(country_sector_update)

        return self.api_client.request(
            type_=m.CountrySector, method="PUT", url="/v1/country-sector/{id}", path_params=path_params, json=body
        )


class AsyncCountrySectorApi(_CountrySectorApi):
    async def create_country_sector(self, country_sector_create: m.CountrySectorCreate) -> m.CountrySector:
        """
        Create new country_sector.
        """
        return await self._build_for_create_country_sector(country_sector_create=country_sector_create)

    async def delete_country_sector(self, id: str) -> m.CountrySector:
        """
        Delete an country_sector.
        """
        return await self._build_for_delete_country_sector(id=id)

    async def get_country_sector(self, id: str) -> m.CountrySector:
        """
        Get country_sector by ID.
        """
        return await self._build_for_get_country_sector(id=id)

    async def list_country_sectors(
        self,
    ) -> List[m.CountrySector]:
        """
        Retrieve country_sectors.
        """
        return await self._build_for_list_country_sectors()

    async def update_country_sector(self, id: str, country_sector_update: m.CountrySectorUpdate) -> m.CountrySector:
        """
        Update a country_sector.
        """
        return await self._build_for_update_country_sector(id=id, country_sector_update=country_sector_update)


class SyncCountrySectorApi(_CountrySectorApi):
    def create_country_sector(self, country_sector_create: m.CountrySectorCreate) -> m.CountrySector:
        """
        Create new country_sector.
        """
        coroutine = self._build_for_create_country_sector(country_sector_create=country_sector_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_country_sector(self, id: str) -> m.CountrySector:
        """
        Delete an country_sector.
        """
        coroutine = self._build_for_delete_country_sector(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_country_sector(self, id: str) -> m.CountrySector:
        """
        Get country_sector by ID.
        """
        coroutine = self._build_for_get_country_sector(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_country_sectors(
        self,
    ) -> List[m.CountrySector]:
        """
        Retrieve country_sectors.
        """
        coroutine = self._build_for_list_country_sectors()
        return get_event_loop().run_until_complete(coroutine)

    def update_country_sector(self, id: str, country_sector_update: m.CountrySectorUpdate) -> m.CountrySector:
        """
        Update a country_sector.
        """
        coroutine = self._build_for_update_country_sector(id=id, country_sector_update=country_sector_update)
        return get_event_loop().run_until_complete(coroutine)
