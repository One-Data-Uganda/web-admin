# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable, List

from app.services.api.information import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.information.api_client import ApiClient


class _CountryContactApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_country_contact(
        self, country_contact_create: m.CountryContactCreate
    ) -> Awaitable[m.CountryContact]:
        """
        Create new country_contact.
        """
        body = jsonable_encoder(country_contact_create)

        return self.api_client.request(type_=m.CountryContact, method="POST", url="/v1/country-contact/", json=body)

    def _build_for_delete_country_contact(self, id: str) -> Awaitable[m.CountryContact]:
        """
        Delete an country_contact.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.CountryContact,
            method="DELETE",
            url="/v1/country-contact/{id}",
            path_params=path_params,
        )

    def _build_for_get_country_contact(self, id: str) -> Awaitable[m.CountryContact]:
        """
        Get country_contact by ID.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.CountryContact,
            method="GET",
            url="/v1/country-contact/{id}",
            path_params=path_params,
        )

    def _build_for_list_country_contacts(
        self,
    ) -> Awaitable[List[m.CountryContact]]:
        """
        Retrieve country_contacts.
        """
        return self.api_client.request(
            type_=List[m.CountryContact],
            method="GET",
            url="/v1/country-contact/",
        )

    def _build_for_update_country_contact(
        self, id: str, country_contact_update: m.CountryContactUpdate
    ) -> Awaitable[m.CountryContact]:
        """
        Update a country_contact.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(country_contact_update)

        return self.api_client.request(
            type_=m.CountryContact, method="PUT", url="/v1/country-contact/{id}", path_params=path_params, json=body
        )


class AsyncCountryContactApi(_CountryContactApi):
    async def create_country_contact(self, country_contact_create: m.CountryContactCreate) -> m.CountryContact:
        """
        Create new country_contact.
        """
        return await self._build_for_create_country_contact(country_contact_create=country_contact_create)

    async def delete_country_contact(self, id: str) -> m.CountryContact:
        """
        Delete an country_contact.
        """
        return await self._build_for_delete_country_contact(id=id)

    async def get_country_contact(self, id: str) -> m.CountryContact:
        """
        Get country_contact by ID.
        """
        return await self._build_for_get_country_contact(id=id)

    async def list_country_contacts(
        self,
    ) -> List[m.CountryContact]:
        """
        Retrieve country_contacts.
        """
        return await self._build_for_list_country_contacts()

    async def update_country_contact(self, id: str, country_contact_update: m.CountryContactUpdate) -> m.CountryContact:
        """
        Update a country_contact.
        """
        return await self._build_for_update_country_contact(id=id, country_contact_update=country_contact_update)


class SyncCountryContactApi(_CountryContactApi):
    def create_country_contact(self, country_contact_create: m.CountryContactCreate) -> m.CountryContact:
        """
        Create new country_contact.
        """
        coroutine = self._build_for_create_country_contact(country_contact_create=country_contact_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_country_contact(self, id: str) -> m.CountryContact:
        """
        Delete an country_contact.
        """
        coroutine = self._build_for_delete_country_contact(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_country_contact(self, id: str) -> m.CountryContact:
        """
        Get country_contact by ID.
        """
        coroutine = self._build_for_get_country_contact(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_country_contacts(
        self,
    ) -> List[m.CountryContact]:
        """
        Retrieve country_contacts.
        """
        coroutine = self._build_for_list_country_contacts()
        return get_event_loop().run_until_complete(coroutine)

    def update_country_contact(self, id: str, country_contact_update: m.CountryContactUpdate) -> m.CountryContact:
        """
        Update a country_contact.
        """
        coroutine = self._build_for_update_country_contact(id=id, country_contact_update=country_contact_update)
        return get_event_loop().run_until_complete(coroutine)
