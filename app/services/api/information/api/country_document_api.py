# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable, List
from uuid import UUID

from app.services.api.information import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.information.api_client import ApiClient


class _CountryDocumentApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_country_document(
        self, country_document_create: m.CountryDocumentCreate
    ) -> Awaitable[m.CountryDocument]:
        """
        Create new country_document.
        """
        body = jsonable_encoder(country_document_create)

        return self.api_client.request(type_=m.CountryDocument, method="POST", url="/v1/country-document/", json=body)

    def _build_for_delete_country_document(self, id: UUID) -> Awaitable[m.CountryDocument]:
        """
        Delete an country_document.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.CountryDocument,
            method="DELETE",
            url="/v1/country-document/{id}",
            path_params=path_params,
        )

    def _build_for_get_country_document(self, id: UUID) -> Awaitable[m.CountryDocument]:
        """
        Get country_document by ID.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.CountryDocument,
            method="GET",
            url="/v1/country-document/{id}",
            path_params=path_params,
        )

    def _build_for_get_country_document_file(self, id: UUID) -> Awaitable[m.Any]:
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.Any,
            method="GET",
            url="/v1/country-document/{id}/file",
            path_params=path_params,
        )

    def _build_for_list_country_documents(self, country_id: str) -> Awaitable[List[m.CountryDocument]]:
        """
        Retrieve country_documents.
        """
        path_params = {"country_id": str(country_id)}

        return self.api_client.request(
            type_=List[m.CountryDocument],
            method="GET",
            url="/v1/country-document/{country_id}/list",
            path_params=path_params,
        )

    def _build_for_update_country_document(
        self, id: UUID, country_document_update: m.CountryDocumentUpdate
    ) -> Awaitable[m.CountryDocument]:
        """
        Update a country_document.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(country_document_update)

        return self.api_client.request(
            type_=m.CountryDocument, method="PUT", url="/v1/country-document/{id}", path_params=path_params, json=body
        )


class AsyncCountryDocumentApi(_CountryDocumentApi):
    async def create_country_document(self, country_document_create: m.CountryDocumentCreate) -> m.CountryDocument:
        """
        Create new country_document.
        """
        return await self._build_for_create_country_document(country_document_create=country_document_create)

    async def delete_country_document(self, id: UUID) -> m.CountryDocument:
        """
        Delete an country_document.
        """
        return await self._build_for_delete_country_document(id=id)

    async def get_country_document(self, id: UUID) -> m.CountryDocument:
        """
        Get country_document by ID.
        """
        return await self._build_for_get_country_document(id=id)

    async def get_country_document_file(self, id: UUID) -> m.Any:
        return await self._build_for_get_country_document_file(id=id)

    async def list_country_documents(self, country_id: str) -> List[m.CountryDocument]:
        """
        Retrieve country_documents.
        """
        return await self._build_for_list_country_documents(country_id=country_id)

    async def update_country_document(
        self, id: UUID, country_document_update: m.CountryDocumentUpdate
    ) -> m.CountryDocument:
        """
        Update a country_document.
        """
        return await self._build_for_update_country_document(id=id, country_document_update=country_document_update)


class SyncCountryDocumentApi(_CountryDocumentApi):
    def create_country_document(self, country_document_create: m.CountryDocumentCreate) -> m.CountryDocument:
        """
        Create new country_document.
        """
        coroutine = self._build_for_create_country_document(country_document_create=country_document_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_country_document(self, id: UUID) -> m.CountryDocument:
        """
        Delete an country_document.
        """
        coroutine = self._build_for_delete_country_document(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_country_document(self, id: UUID) -> m.CountryDocument:
        """
        Get country_document by ID.
        """
        coroutine = self._build_for_get_country_document(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_country_document_file(self, id: UUID) -> m.Any:
        coroutine = self._build_for_get_country_document_file(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_country_documents(self, country_id: str) -> List[m.CountryDocument]:
        """
        Retrieve country_documents.
        """
        coroutine = self._build_for_list_country_documents(country_id=country_id)
        return get_event_loop().run_until_complete(coroutine)

    def update_country_document(self, id: UUID, country_document_update: m.CountryDocumentUpdate) -> m.CountryDocument:
        """
        Update a country_document.
        """
        coroutine = self._build_for_update_country_document(id=id, country_document_update=country_document_update)
        return get_event_loop().run_until_complete(coroutine)
