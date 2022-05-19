# flake8: noqa E501
from asyncio import get_event_loop
from typing import IO, TYPE_CHECKING, Any, Awaitable, Dict
from uuid import UUID

from app.services.api.user import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.user.api_client import ApiClient


class _KycApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_add_kyc_document(
        self, kyc_id: UUID, name: str, document_type_id: str, uploaded_file: IO[Any]
    ) -> Awaitable[m.KYCDocumentResponse]:
        """
        Add a KYC document
        """
        path_params = {"kyc_id": str(kyc_id)}

        files: Dict[str, IO[Any]] = {}  # noqa F841
        data: Dict[str, Any] = {}  # noqa F841
        data["name"] = name
        data["document_type_id"] = document_type_id
        files["uploaded_file"] = uploaded_file

        return self.api_client.request(
            type_=m.KYCDocumentResponse,
            method="POST",
            url="/v1/kyc/{kyc_id}/document",
            path_params=path_params,
            data=data,
            files=files,
        )

    def _build_for_create_kyc(self, kyc_create: m.KYCCreate) -> Awaitable[m.KYCResponse]:
        """
        Create new kyc.
        """
        body = jsonable_encoder(kyc_create)

        return self.api_client.request(type_=m.KYCResponse, method="POST", url="/v1/kyc/", json=body)

    def _build_for_get_by_business_name(self, business_name: str) -> Awaitable[m.KYCResponse]:
        query_params = {"business_name": str(business_name)}

        return self.api_client.request(
            type_=m.KYCResponse,
            method="POST",
            url="/v1/kyc/check-business-name",
            params=query_params,
        )

    def _build_for_get_by_email(self, email: str) -> Awaitable[m.KYCResponse]:
        query_params = {"email": str(email)}

        return self.api_client.request(
            type_=m.KYCResponse,
            method="POST",
            url="/v1/kyc/check-email",
            params=query_params,
        )

    def _build_for_get_by_msisdn(self, msisdn: str) -> Awaitable[m.KYCResponse]:
        query_params = {"msisdn": str(msisdn)}

        return self.api_client.request(
            type_=m.KYCResponse,
            method="POST",
            url="/v1/kyc/check-msisdn",
            params=query_params,
        )

    def _build_for_get_kyc(self, id: UUID) -> Awaitable[m.KYCResponse]:
        """
        Get a specific kyc by id.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.KYCResponse,
            method="GET",
            url="/v1/kyc/{id}",
            path_params=path_params,
        )

    def _build_for_get_kyc_document(self, id: UUID) -> Awaitable[m.KYCDocumentResponse]:
        """
        Retrieve a KYC document
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.KYCDocumentResponse,
            method="GET",
            url="/v1/kyc/document/{id}",
            path_params=path_params,
        )

    def _build_for_get_kyc_document_file(self, kyc_id: UUID, id: UUID) -> Awaitable[m.Any]:
        """
        Retrieve a KYC document
        """
        path_params = {"kyc_id": str(kyc_id), "id": str(id)}

        return self.api_client.request(
            type_=m.Any,
            method="GET",
            url="/v1/kyc/{kyc_id}/document/{id}/file",
            path_params=path_params,
        )

    def _build_for_update_kyc(self, id: UUID, kyc_update: m.KYCUpdate) -> Awaitable[m.KYCResponse]:
        """
        Update a kyc.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(kyc_update)

        return self.api_client.request(
            type_=m.KYCResponse, method="PUT", url="/v1/kyc/{id}", path_params=path_params, json=body
        )

    def _build_for_update_kyc_document(self, id: UUID, uploaded_file: IO[Any]) -> Awaitable[m.KYCDocumentResponse]:
        """
        Update a KYC document
        """
        path_params = {"id": str(id)}

        files: Dict[str, IO[Any]] = {}  # noqa F841
        data: Dict[str, Any] = {}  # noqa F841
        files["uploaded_file"] = uploaded_file

        return self.api_client.request(
            type_=m.KYCDocumentResponse,
            method="PUT",
            url="/v1/kyc/{id}/document",
            path_params=path_params,
            data=data,
            files=files,
        )


class AsyncKycApi(_KycApi):
    async def add_kyc_document(
        self, kyc_id: UUID, name: str, document_type_id: str, uploaded_file: IO[Any]
    ) -> m.KYCDocumentResponse:
        """
        Add a KYC document
        """
        return await self._build_for_add_kyc_document(
            kyc_id=kyc_id, name=name, document_type_id=document_type_id, uploaded_file=uploaded_file
        )

    async def create_kyc(self, kyc_create: m.KYCCreate) -> m.KYCResponse:
        """
        Create new kyc.
        """
        return await self._build_for_create_kyc(kyc_create=kyc_create)

    async def get_by_business_name(self, business_name: str) -> m.KYCResponse:
        return await self._build_for_get_by_business_name(business_name=business_name)

    async def get_by_email(self, email: str) -> m.KYCResponse:
        return await self._build_for_get_by_email(email=email)

    async def get_by_msisdn(self, msisdn: str) -> m.KYCResponse:
        return await self._build_for_get_by_msisdn(msisdn=msisdn)

    async def get_kyc(self, id: UUID) -> m.KYCResponse:
        """
        Get a specific kyc by id.
        """
        return await self._build_for_get_kyc(id=id)

    async def get_kyc_document(self, id: UUID) -> m.KYCDocumentResponse:
        """
        Retrieve a KYC document
        """
        return await self._build_for_get_kyc_document(id=id)

    async def get_kyc_document_file(self, kyc_id: UUID, id: UUID) -> m.Any:
        """
        Retrieve a KYC document
        """
        return await self._build_for_get_kyc_document_file(kyc_id=kyc_id, id=id)

    async def update_kyc(self, id: UUID, kyc_update: m.KYCUpdate) -> m.KYCResponse:
        """
        Update a kyc.
        """
        return await self._build_for_update_kyc(id=id, kyc_update=kyc_update)

    async def update_kyc_document(self, id: UUID, uploaded_file: IO[Any]) -> m.KYCDocumentResponse:
        """
        Update a KYC document
        """
        return await self._build_for_update_kyc_document(id=id, uploaded_file=uploaded_file)


class SyncKycApi(_KycApi):
    def add_kyc_document(
        self, kyc_id: UUID, name: str, document_type_id: str, uploaded_file: IO[Any]
    ) -> m.KYCDocumentResponse:
        """
        Add a KYC document
        """
        coroutine = self._build_for_add_kyc_document(
            kyc_id=kyc_id, name=name, document_type_id=document_type_id, uploaded_file=uploaded_file
        )
        return get_event_loop().run_until_complete(coroutine)

    def create_kyc(self, kyc_create: m.KYCCreate) -> m.KYCResponse:
        """
        Create new kyc.
        """
        coroutine = self._build_for_create_kyc(kyc_create=kyc_create)
        return get_event_loop().run_until_complete(coroutine)

    def get_by_business_name(self, business_name: str) -> m.KYCResponse:
        coroutine = self._build_for_get_by_business_name(business_name=business_name)
        return get_event_loop().run_until_complete(coroutine)

    def get_by_email(self, email: str) -> m.KYCResponse:
        coroutine = self._build_for_get_by_email(email=email)
        return get_event_loop().run_until_complete(coroutine)

    def get_by_msisdn(self, msisdn: str) -> m.KYCResponse:
        coroutine = self._build_for_get_by_msisdn(msisdn=msisdn)
        return get_event_loop().run_until_complete(coroutine)

    def get_kyc(self, id: UUID) -> m.KYCResponse:
        """
        Get a specific kyc by id.
        """
        coroutine = self._build_for_get_kyc(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_kyc_document(self, id: UUID) -> m.KYCDocumentResponse:
        """
        Retrieve a KYC document
        """
        coroutine = self._build_for_get_kyc_document(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_kyc_document_file(self, kyc_id: UUID, id: UUID) -> m.Any:
        """
        Retrieve a KYC document
        """
        coroutine = self._build_for_get_kyc_document_file(kyc_id=kyc_id, id=id)
        return get_event_loop().run_until_complete(coroutine)

    def update_kyc(self, id: UUID, kyc_update: m.KYCUpdate) -> m.KYCResponse:
        """
        Update a kyc.
        """
        coroutine = self._build_for_update_kyc(id=id, kyc_update=kyc_update)
        return get_event_loop().run_until_complete(coroutine)

    def update_kyc_document(self, id: UUID, uploaded_file: IO[Any]) -> m.KYCDocumentResponse:
        """
        Update a KYC document
        """
        coroutine = self._build_for_update_kyc_document(id=id, uploaded_file=uploaded_file)
        return get_event_loop().run_until_complete(coroutine)
