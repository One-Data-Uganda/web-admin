# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from app.services.api.user import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.user.api_client import ApiClient


class _ContactPersonApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_contact_person(
        self, contact_person_create: m.ContactPersonCreate
    ) -> Awaitable[m.ContactPersonResponse]:
        """
        Create new contact person.
        """
        body = jsonable_encoder(contact_person_create)

        return self.api_client.request(
            type_=m.ContactPersonResponse, method="POST", url="/v1/contact-person/", json=body
        )

    def _build_for_delete_contact_person(self, id: int) -> Awaitable[m.ContactPersonResponse]:
        """
        Delete contact_person
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.ContactPersonResponse,
            method="DELETE",
            url="/v1/contact-person/{id}",
            path_params=path_params,
        )

    def _build_for_get_contact_person(self, id: int) -> Awaitable[m.ContactPersonResponse]:
        """
        Get a specific contact_person by id.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.ContactPersonResponse,
            method="GET",
            url="/v1/contact-person/{id}",
            path_params=path_params,
        )

    def _build_for_list_contact_persons(
        self,
    ) -> Awaitable[m.ContactPersonListResponse]:
        """
        Contact Person listing
        """
        return self.api_client.request(
            type_=m.ContactPersonListResponse,
            method="GET",
            url="/v1/contact-person/",
        )

    def _build_for_update_contact_person(
        self, id: int, contact_person_update: m.ContactPersonUpdate
    ) -> Awaitable[m.ContactPersonResponse]:
        """
        Update a contact_person.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(contact_person_update)

        return self.api_client.request(
            type_=m.ContactPersonResponse,
            method="PUT",
            url="/v1/contact-person/{id}",
            path_params=path_params,
            json=body,
        )


class AsyncContactPersonApi(_ContactPersonApi):
    async def create_contact_person(self, contact_person_create: m.ContactPersonCreate) -> m.ContactPersonResponse:
        """
        Create new contact person.
        """
        return await self._build_for_create_contact_person(contact_person_create=contact_person_create)

    async def delete_contact_person(self, id: int) -> m.ContactPersonResponse:
        """
        Delete contact_person
        """
        return await self._build_for_delete_contact_person(id=id)

    async def get_contact_person(self, id: int) -> m.ContactPersonResponse:
        """
        Get a specific contact_person by id.
        """
        return await self._build_for_get_contact_person(id=id)

    async def list_contact_persons(
        self,
    ) -> m.ContactPersonListResponse:
        """
        Contact Person listing
        """
        return await self._build_for_list_contact_persons()

    async def update_contact_person(
        self, id: int, contact_person_update: m.ContactPersonUpdate
    ) -> m.ContactPersonResponse:
        """
        Update a contact_person.
        """
        return await self._build_for_update_contact_person(id=id, contact_person_update=contact_person_update)


class SyncContactPersonApi(_ContactPersonApi):
    def create_contact_person(self, contact_person_create: m.ContactPersonCreate) -> m.ContactPersonResponse:
        """
        Create new contact person.
        """
        coroutine = self._build_for_create_contact_person(contact_person_create=contact_person_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_contact_person(self, id: int) -> m.ContactPersonResponse:
        """
        Delete contact_person
        """
        coroutine = self._build_for_delete_contact_person(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_contact_person(self, id: int) -> m.ContactPersonResponse:
        """
        Get a specific contact_person by id.
        """
        coroutine = self._build_for_get_contact_person(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_contact_persons(
        self,
    ) -> m.ContactPersonListResponse:
        """
        Contact Person listing
        """
        coroutine = self._build_for_list_contact_persons()
        return get_event_loop().run_until_complete(coroutine)

    def update_contact_person(self, id: int, contact_person_update: m.ContactPersonUpdate) -> m.ContactPersonResponse:
        """
        Update a contact_person.
        """
        coroutine = self._build_for_update_contact_person(id=id, contact_person_update=contact_person_update)
        return get_event_loop().run_until_complete(coroutine)
