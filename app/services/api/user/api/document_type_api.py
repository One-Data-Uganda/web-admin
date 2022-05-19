# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from app.services.api.user import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.user.api_client import ApiClient


class _DocumentTypeApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_document_type(
        self, document_type_create: m.DocumentTypeCreate
    ) -> Awaitable[m.DocumentTypeResponse]:
        """
        Create new document_type.
        """
        body = jsonable_encoder(document_type_create)

        return self.api_client.request(type_=m.DocumentTypeResponse, method="POST", url="/v1/document-type/", json=body)

    def _build_for_delete_document_type(self, id: str) -> Awaitable[m.DocumentTypeResponse]:
        """
        Delete a document_type.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.DocumentTypeResponse,
            method="DELETE",
            url="/v1/document-type/{id}",
            path_params=path_params,
        )

    def _build_for_get_document_type(self, id: str) -> Awaitable[m.DocumentTypeResponse]:
        """
        Get DocumentType
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.DocumentTypeResponse,
            method="GET",
            url="/v1/document-type/{id}",
            path_params=path_params,
        )

    def _build_for_list_document_types(
        self,
    ) -> Awaitable[m.DocumentTypeListResponse]:
        """
        Get all document_types
        """
        return self.api_client.request(
            type_=m.DocumentTypeListResponse,
            method="GET",
            url="/v1/document-type/",
        )

    def _build_for_update_document_type(
        self, id: str, document_type_update: m.DocumentTypeUpdate
    ) -> Awaitable[m.DocumentTypeResponse]:
        """
        Update document_type
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(document_type_update)

        return self.api_client.request(
            type_=m.DocumentTypeResponse, method="PUT", url="/v1/document-type/{id}", path_params=path_params, json=body
        )


class AsyncDocumentTypeApi(_DocumentTypeApi):
    async def create_document_type(self, document_type_create: m.DocumentTypeCreate) -> m.DocumentTypeResponse:
        """
        Create new document_type.
        """
        return await self._build_for_create_document_type(document_type_create=document_type_create)

    async def delete_document_type(self, id: str) -> m.DocumentTypeResponse:
        """
        Delete a document_type.
        """
        return await self._build_for_delete_document_type(id=id)

    async def get_document_type(self, id: str) -> m.DocumentTypeResponse:
        """
        Get DocumentType
        """
        return await self._build_for_get_document_type(id=id)

    async def list_document_types(
        self,
    ) -> m.DocumentTypeListResponse:
        """
        Get all document_types
        """
        return await self._build_for_list_document_types()

    async def update_document_type(self, id: str, document_type_update: m.DocumentTypeUpdate) -> m.DocumentTypeResponse:
        """
        Update document_type
        """
        return await self._build_for_update_document_type(id=id, document_type_update=document_type_update)


class SyncDocumentTypeApi(_DocumentTypeApi):
    def create_document_type(self, document_type_create: m.DocumentTypeCreate) -> m.DocumentTypeResponse:
        """
        Create new document_type.
        """
        coroutine = self._build_for_create_document_type(document_type_create=document_type_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_document_type(self, id: str) -> m.DocumentTypeResponse:
        """
        Delete a document_type.
        """
        coroutine = self._build_for_delete_document_type(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_document_type(self, id: str) -> m.DocumentTypeResponse:
        """
        Get DocumentType
        """
        coroutine = self._build_for_get_document_type(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_document_types(
        self,
    ) -> m.DocumentTypeListResponse:
        """
        Get all document_types
        """
        coroutine = self._build_for_list_document_types()
        return get_event_loop().run_until_complete(coroutine)

    def update_document_type(self, id: str, document_type_update: m.DocumentTypeUpdate) -> m.DocumentTypeResponse:
        """
        Update document_type
        """
        coroutine = self._build_for_update_document_type(id=id, document_type_update=document_type_update)
        return get_event_loop().run_until_complete(coroutine)
