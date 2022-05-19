# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from app.services.api.user import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.user.api_client import ApiClient


class _CountryApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_country(self, country_create: m.CountryCreate) -> Awaitable[m.CountryResponse]:
        """
        Create new country.
        """
        body = jsonable_encoder(country_create)

        return self.api_client.request(type_=m.CountryResponse, method="POST", url="/v1/country/", json=body)

    def _build_for_delete_country(self, country_id: str) -> Awaitable[m.CountryResponse]:
        """
        Delete a country.
        """
        path_params = {"country_id": str(country_id)}

        return self.api_client.request(
            type_=m.CountryResponse,
            method="DELETE",
            url="/v1/country/{country_id}",
            path_params=path_params,
        )

    def _build_for_get_country(self, id: str) -> Awaitable[m.CountryResponse]:
        """
        Get Country
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.CountryResponse,
            method="GET",
            url="/v1/country/{id}",
            path_params=path_params,
        )

    def _build_for_list_countries(
        self,
    ) -> Awaitable[m.CountryListResponse]:
        """
        Get all countries
        """
        return self.api_client.request(
            type_=m.CountryListResponse,
            method="GET",
            url="/v1/country/",
        )

    def _build_for_update_country(self, id: str, country_update: m.CountryUpdate) -> Awaitable[m.CountryResponse]:
        """
        Update country
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(country_update)

        return self.api_client.request(
            type_=m.CountryResponse, method="PUT", url="/v1/country/{id}", path_params=path_params, json=body
        )


class AsyncCountryApi(_CountryApi):
    async def create_country(self, country_create: m.CountryCreate) -> m.CountryResponse:
        """
        Create new country.
        """
        return await self._build_for_create_country(country_create=country_create)

    async def delete_country(self, country_id: str) -> m.CountryResponse:
        """
        Delete a country.
        """
        return await self._build_for_delete_country(country_id=country_id)

    async def get_country(self, id: str) -> m.CountryResponse:
        """
        Get Country
        """
        return await self._build_for_get_country(id=id)

    async def list_countries(
        self,
    ) -> m.CountryListResponse:
        """
        Get all countries
        """
        return await self._build_for_list_countries()

    async def update_country(self, id: str, country_update: m.CountryUpdate) -> m.CountryResponse:
        """
        Update country
        """
        return await self._build_for_update_country(id=id, country_update=country_update)


class SyncCountryApi(_CountryApi):
    def create_country(self, country_create: m.CountryCreate) -> m.CountryResponse:
        """
        Create new country.
        """
        coroutine = self._build_for_create_country(country_create=country_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_country(self, country_id: str) -> m.CountryResponse:
        """
        Delete a country.
        """
        coroutine = self._build_for_delete_country(country_id=country_id)
        return get_event_loop().run_until_complete(coroutine)

    def get_country(self, id: str) -> m.CountryResponse:
        """
        Get Country
        """
        coroutine = self._build_for_get_country(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_countries(
        self,
    ) -> m.CountryListResponse:
        """
        Get all countries
        """
        coroutine = self._build_for_list_countries()
        return get_event_loop().run_until_complete(coroutine)

    def update_country(self, id: str, country_update: m.CountryUpdate) -> m.CountryResponse:
        """
        Update country
        """
        coroutine = self._build_for_update_country(id=id, country_update=country_update)
        return get_event_loop().run_until_complete(coroutine)
