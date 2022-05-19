# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Any, Awaitable, List
from uuid import UUID

from app.services.api.user import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.user.api_client import ApiClient


class _AccountApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_add_contact_person(self, contact_person: m.ContactPerson) -> Awaitable[m.ContactPersonResponse]:
        body = jsonable_encoder(contact_person)

        return self.api_client.request(
            type_=m.ContactPersonResponse, method="POST", url="/v1/account/contact-person", json=body
        )

    def _build_for_add_countries(self, any: List[m.Any]) -> Awaitable[m.FailureResponseModel]:
        body = jsonable_encoder(any)

        return self.api_client.request(
            type_=m.FailureResponseModel, method="POST", url="/v1/account/country", json=body
        )

    def _build_for_add_industries(self, any: List[m.Any]) -> Awaitable[m.FailureResponseModel]:
        body = jsonable_encoder(any)

        return self.api_client.request(
            type_=m.FailureResponseModel, method="POST", url="/v1/account/industry", json=body
        )

    def _build_for_create_account(self, account_view_create: m.AccountViewCreate) -> Awaitable[m.AccountResponse]:
        """
        Create new account.
        """
        body = jsonable_encoder(account_view_create)

        return self.api_client.request(type_=m.AccountResponse, method="POST", url="/v1/account/", json=body)

    def _build_for_disable_account(self, id: UUID) -> Awaitable[m.AccountResponse]:
        """
        Disable an account.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.AccountResponse,
            method="PUT",
            url="/v1/account/{id}/disable",
            path_params=path_params,
        )

    def _build_for_enable_account(self, id: UUID) -> Awaitable[m.AccountResponse]:
        """
        Enable an account.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.AccountResponse,
            method="PUT",
            url="/v1/account/{id}/enable",
            path_params=path_params,
        )

    def _build_for_get_account(self, id: UUID) -> Awaitable[m.AccountResponse]:
        """
        Get a specific account by id.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.AccountResponse,
            method="GET",
            url="/v1/account/{id}",
            path_params=path_params,
        )

    def _build_for_list_accounts(
        self,
    ) -> Awaitable[m.AccountListResponse]:
        """
        List accounts
        """
        return self.api_client.request(
            type_=m.AccountListResponse,
            method="GET",
            url="/v1/account/",
        )

    def _build_for_search_accounts(self, body: Any) -> Awaitable[m.Any]:
        body = jsonable_encoder(body)

        return self.api_client.request(type_=m.Any, method="POST", url="/v1/account/search", json=body)

    def _build_for_search_individual(self, body: Any) -> Awaitable[m.Any]:
        body = jsonable_encoder(body)

        return self.api_client.request(type_=m.Any, method="POST", url="/v1/account/search/individual", json=body)

    def _build_for_update_account(
        self, id: UUID, account_view_update: m.AccountViewUpdate
    ) -> Awaitable[m.AccountResponse]:
        """
        Update a account.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(account_view_update)

        return self.api_client.request(
            type_=m.AccountResponse, method="PUT", url="/v1/account/{id}", path_params=path_params, json=body
        )


class AsyncAccountApi(_AccountApi):
    async def add_contact_person(self, contact_person: m.ContactPerson) -> m.ContactPersonResponse:
        return await self._build_for_add_contact_person(contact_person=contact_person)

    async def add_countries(self, any: List[m.Any]) -> m.FailureResponseModel:
        return await self._build_for_add_countries(any=any)

    async def add_industries(self, any: List[m.Any]) -> m.FailureResponseModel:
        return await self._build_for_add_industries(any=any)

    async def create_account(self, account_view_create: m.AccountViewCreate) -> m.AccountResponse:
        """
        Create new account.
        """
        return await self._build_for_create_account(account_view_create=account_view_create)

    async def disable_account(self, id: UUID) -> m.AccountResponse:
        """
        Disable an account.
        """
        return await self._build_for_disable_account(id=id)

    async def enable_account(self, id: UUID) -> m.AccountResponse:
        """
        Enable an account.
        """
        return await self._build_for_enable_account(id=id)

    async def get_account(self, id: UUID) -> m.AccountResponse:
        """
        Get a specific account by id.
        """
        return await self._build_for_get_account(id=id)

    async def list_accounts(
        self,
    ) -> m.AccountListResponse:
        """
        List accounts
        """
        return await self._build_for_list_accounts()

    async def search_accounts(self, body: Any) -> m.Any:
        return await self._build_for_search_accounts(body=body)

    async def search_individual(self, body: Any) -> m.Any:
        return await self._build_for_search_individual(body=body)

    async def update_account(self, id: UUID, account_view_update: m.AccountViewUpdate) -> m.AccountResponse:
        """
        Update a account.
        """
        return await self._build_for_update_account(id=id, account_view_update=account_view_update)


class SyncAccountApi(_AccountApi):
    def add_contact_person(self, contact_person: m.ContactPerson) -> m.ContactPersonResponse:
        coroutine = self._build_for_add_contact_person(contact_person=contact_person)
        return get_event_loop().run_until_complete(coroutine)

    def add_countries(self, any: List[m.Any]) -> m.FailureResponseModel:
        coroutine = self._build_for_add_countries(any=any)
        return get_event_loop().run_until_complete(coroutine)

    def add_industries(self, any: List[m.Any]) -> m.FailureResponseModel:
        coroutine = self._build_for_add_industries(any=any)
        return get_event_loop().run_until_complete(coroutine)

    def create_account(self, account_view_create: m.AccountViewCreate) -> m.AccountResponse:
        """
        Create new account.
        """
        coroutine = self._build_for_create_account(account_view_create=account_view_create)
        return get_event_loop().run_until_complete(coroutine)

    def disable_account(self, id: UUID) -> m.AccountResponse:
        """
        Disable an account.
        """
        coroutine = self._build_for_disable_account(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def enable_account(self, id: UUID) -> m.AccountResponse:
        """
        Enable an account.
        """
        coroutine = self._build_for_enable_account(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_account(self, id: UUID) -> m.AccountResponse:
        """
        Get a specific account by id.
        """
        coroutine = self._build_for_get_account(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_accounts(
        self,
    ) -> m.AccountListResponse:
        """
        List accounts
        """
        coroutine = self._build_for_list_accounts()
        return get_event_loop().run_until_complete(coroutine)

    def search_accounts(self, body: Any) -> m.Any:
        coroutine = self._build_for_search_accounts(body=body)
        return get_event_loop().run_until_complete(coroutine)

    def search_individual(self, body: Any) -> m.Any:
        coroutine = self._build_for_search_individual(body=body)
        return get_event_loop().run_until_complete(coroutine)

    def update_account(self, id: UUID, account_view_update: m.AccountViewUpdate) -> m.AccountResponse:
        """
        Update a account.
        """
        coroutine = self._build_for_update_account(id=id, account_view_update=account_view_update)
        return get_event_loop().run_until_complete(coroutine)
