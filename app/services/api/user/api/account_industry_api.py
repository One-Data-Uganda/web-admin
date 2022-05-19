# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from app.services.api.user import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.user.api_client import ApiClient


class _AccountIndustryApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_account_industry(
        self, account_industry_create: m.AccountIndustryCreate
    ) -> Awaitable[m.AccountIndustryResponse]:
        """
        Create new account industry.
        """
        body = jsonable_encoder(account_industry_create)

        return self.api_client.request(
            type_=m.AccountIndustryResponse, method="POST", url="/v1/account-industry/", json=body
        )

    def _build_for_delete_account_industry(self, id: int) -> Awaitable[m.AccountIndustryResponse]:
        """
        Delete account_industry
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.AccountIndustryResponse,
            method="DELETE",
            url="/v1/account-industry/{id}",
            path_params=path_params,
        )

    def _build_for_get_account_industry(self, id: int) -> Awaitable[m.AccountIndustryResponse]:
        """
        Get a specific account_industry by id.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.AccountIndustryResponse,
            method="GET",
            url="/v1/account-industry/{id}",
            path_params=path_params,
        )

    def _build_for_list_account_industrys(
        self,
    ) -> Awaitable[m.AccountIndustryListResponse]:
        """
        Account Industry listing
        """
        return self.api_client.request(
            type_=m.AccountIndustryListResponse,
            method="GET",
            url="/v1/account-industry/",
        )

    def _build_for_update_account_industry(
        self, id: int, account_industry_update: m.AccountIndustryUpdate
    ) -> Awaitable[m.AccountIndustryResponse]:
        """
        Update a account_industry.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(account_industry_update)

        return self.api_client.request(
            type_=m.AccountIndustryResponse,
            method="PUT",
            url="/v1/account-industry/{id}",
            path_params=path_params,
            json=body,
        )


class AsyncAccountIndustryApi(_AccountIndustryApi):
    async def create_account_industry(
        self, account_industry_create: m.AccountIndustryCreate
    ) -> m.AccountIndustryResponse:
        """
        Create new account industry.
        """
        return await self._build_for_create_account_industry(account_industry_create=account_industry_create)

    async def delete_account_industry(self, id: int) -> m.AccountIndustryResponse:
        """
        Delete account_industry
        """
        return await self._build_for_delete_account_industry(id=id)

    async def get_account_industry(self, id: int) -> m.AccountIndustryResponse:
        """
        Get a specific account_industry by id.
        """
        return await self._build_for_get_account_industry(id=id)

    async def list_account_industrys(
        self,
    ) -> m.AccountIndustryListResponse:
        """
        Account Industry listing
        """
        return await self._build_for_list_account_industrys()

    async def update_account_industry(
        self, id: int, account_industry_update: m.AccountIndustryUpdate
    ) -> m.AccountIndustryResponse:
        """
        Update a account_industry.
        """
        return await self._build_for_update_account_industry(id=id, account_industry_update=account_industry_update)


class SyncAccountIndustryApi(_AccountIndustryApi):
    def create_account_industry(self, account_industry_create: m.AccountIndustryCreate) -> m.AccountIndustryResponse:
        """
        Create new account industry.
        """
        coroutine = self._build_for_create_account_industry(account_industry_create=account_industry_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_account_industry(self, id: int) -> m.AccountIndustryResponse:
        """
        Delete account_industry
        """
        coroutine = self._build_for_delete_account_industry(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_account_industry(self, id: int) -> m.AccountIndustryResponse:
        """
        Get a specific account_industry by id.
        """
        coroutine = self._build_for_get_account_industry(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_account_industrys(
        self,
    ) -> m.AccountIndustryListResponse:
        """
        Account Industry listing
        """
        coroutine = self._build_for_list_account_industrys()
        return get_event_loop().run_until_complete(coroutine)

    def update_account_industry(
        self, id: int, account_industry_update: m.AccountIndustryUpdate
    ) -> m.AccountIndustryResponse:
        """
        Update a account_industry.
        """
        coroutine = self._build_for_update_account_industry(id=id, account_industry_update=account_industry_update)
        return get_event_loop().run_until_complete(coroutine)
