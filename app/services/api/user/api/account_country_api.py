# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from app.services.api.user import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.user.api_client import ApiClient


class _AccountCountryApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_account_country(
        self, account_country_create: m.AccountCountryCreate
    ) -> Awaitable[m.AccountCountryResponse]:
        """
        Create new account country.
        """
        body = jsonable_encoder(account_country_create)

        return self.api_client.request(
            type_=m.AccountCountryResponse, method="POST", url="/v1/account-country/", json=body
        )

    def _build_for_delete_account_country(self, id: int) -> Awaitable[m.AccountCountryResponse]:
        """
        Delete account_country
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.AccountCountryResponse,
            method="DELETE",
            url="/v1/account-country/{id}",
            path_params=path_params,
        )

    def _build_for_get_account_country(self, id: int) -> Awaitable[m.AccountCountryResponse]:
        """
        Get a specific account_country by id.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.AccountCountryResponse,
            method="GET",
            url="/v1/account-country/{id}",
            path_params=path_params,
        )

    def _build_for_list_account_countrys(
        self,
    ) -> Awaitable[m.AccountCountryListResponse]:
        """
        Account Country listing
        """
        return self.api_client.request(
            type_=m.AccountCountryListResponse,
            method="GET",
            url="/v1/account-country/",
        )

    def _build_for_update_account_country(
        self, id: int, account_country_update: m.AccountCountryUpdate
    ) -> Awaitable[m.AccountCountryResponse]:
        """
        Update a account_country.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(account_country_update)

        return self.api_client.request(
            type_=m.AccountCountryResponse,
            method="PUT",
            url="/v1/account-country/{id}",
            path_params=path_params,
            json=body,
        )


class AsyncAccountCountryApi(_AccountCountryApi):
    async def create_account_country(self, account_country_create: m.AccountCountryCreate) -> m.AccountCountryResponse:
        """
        Create new account country.
        """
        return await self._build_for_create_account_country(account_country_create=account_country_create)

    async def delete_account_country(self, id: int) -> m.AccountCountryResponse:
        """
        Delete account_country
        """
        return await self._build_for_delete_account_country(id=id)

    async def get_account_country(self, id: int) -> m.AccountCountryResponse:
        """
        Get a specific account_country by id.
        """
        return await self._build_for_get_account_country(id=id)

    async def list_account_countrys(
        self,
    ) -> m.AccountCountryListResponse:
        """
        Account Country listing
        """
        return await self._build_for_list_account_countrys()

    async def update_account_country(
        self, id: int, account_country_update: m.AccountCountryUpdate
    ) -> m.AccountCountryResponse:
        """
        Update a account_country.
        """
        return await self._build_for_update_account_country(id=id, account_country_update=account_country_update)


class SyncAccountCountryApi(_AccountCountryApi):
    def create_account_country(self, account_country_create: m.AccountCountryCreate) -> m.AccountCountryResponse:
        """
        Create new account country.
        """
        coroutine = self._build_for_create_account_country(account_country_create=account_country_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_account_country(self, id: int) -> m.AccountCountryResponse:
        """
        Delete account_country
        """
        coroutine = self._build_for_delete_account_country(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_account_country(self, id: int) -> m.AccountCountryResponse:
        """
        Get a specific account_country by id.
        """
        coroutine = self._build_for_get_account_country(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_account_countrys(
        self,
    ) -> m.AccountCountryListResponse:
        """
        Account Country listing
        """
        coroutine = self._build_for_list_account_countrys()
        return get_event_loop().run_until_complete(coroutine)

    def update_account_country(
        self, id: int, account_country_update: m.AccountCountryUpdate
    ) -> m.AccountCountryResponse:
        """
        Update a account_country.
        """
        coroutine = self._build_for_update_account_country(id=id, account_country_update=account_country_update)
        return get_event_loop().run_until_complete(coroutine)
