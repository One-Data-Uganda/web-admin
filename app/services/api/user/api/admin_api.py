# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Any, Awaitable
from uuid import UUID

from app.services.api.user import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.user.api_client import ApiClient


class _AdminApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_admin_json(self, body: Any) -> Awaitable[m.Any]:
        body = jsonable_encoder(body)

        return self.api_client.request(type_=m.Any, method="POST", url="/v1/admin/json", json=body)

    def _build_for_check_admin_email(self, email_model: m.EmailModel) -> Awaitable[m.AdminResponse]:
        """
        Check email uniqueness
        """
        body = jsonable_encoder(email_model)

        return self.api_client.request(type_=m.AdminResponse, method="POST", url="/v1/admin/check-email", json=body)

    def _build_for_check_admin_msisdn(self, msisdn_model: m.MSISDNModel) -> Awaitable[m.AdminResponse]:
        """
        Check msisdn uniqueness
        """
        body = jsonable_encoder(msisdn_model)

        return self.api_client.request(type_=m.AdminResponse, method="POST", url="/v1/admin/check-msisdn", json=body)

    def _build_for_create_admin(self, admin_create: m.AdminCreate) -> Awaitable[m.AdminResponse]:
        """
        Create new admin.
        """
        body = jsonable_encoder(admin_create)

        return self.api_client.request(type_=m.AdminResponse, method="POST", url="/v1/admin/", json=body)

    def _build_for_disable_admin(self, id: UUID) -> Awaitable[m.AdminResponse]:
        """
        Disable admin
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.AdminResponse,
            method="PUT",
            url="/v1/admin/{id}/disable",
            path_params=path_params,
        )

    def _build_for_enable_admin(self, id: UUID) -> Awaitable[m.AdminResponse]:
        """
        Enable admin
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.AdminResponse,
            method="PUT",
            url="/v1/admin/{id}/enable",
            path_params=path_params,
        )

    def _build_for_get_admin(self, id: UUID) -> Awaitable[m.AdminResponse]:
        """
        Get a specific admin by id.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.AdminResponse,
            method="GET",
            url="/v1/admin/{id}",
            path_params=path_params,
        )

    def _build_for_list_admins(
        self,
    ) -> Awaitable[m.AdminListResponse]:
        """
        List admins
        """
        return self.api_client.request(
            type_=m.AdminListResponse,
            method="GET",
            url="/v1/admin/",
        )

    def _build_for_login_admin(self, admin_login: m.AdminLogin) -> Awaitable[m.AdminResponse]:
        """
        Admin login
        """
        body = jsonable_encoder(admin_login)

        return self.api_client.request(type_=m.AdminResponse, method="POST", url="/v1/admin/login", json=body)

    def _build_for_set_admin_password(self, id: UUID, password_model: m.PasswordModel) -> Awaitable[m.AdminResponse]:
        """
        Set admin password
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(password_model)

        return self.api_client.request(
            type_=m.AdminResponse, method="PUT", url="/v1/admin/{id}/password", path_params=path_params, json=body
        )

    def _build_for_update_admin(self, id: UUID, admin_update: m.AdminUpdate) -> Awaitable[m.AdminResponse]:
        """
        Update an admin.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(admin_update)

        return self.api_client.request(
            type_=m.AdminResponse, method="PUT", url="/v1/admin/{id}", path_params=path_params, json=body
        )


class AsyncAdminApi(_AdminApi):
    async def admin_json(self, body: Any) -> m.Any:
        return await self._build_for_admin_json(body=body)

    async def check_admin_email(self, email_model: m.EmailModel) -> m.AdminResponse:
        """
        Check email uniqueness
        """
        return await self._build_for_check_admin_email(email_model=email_model)

    async def check_admin_msisdn(self, msisdn_model: m.MSISDNModel) -> m.AdminResponse:
        """
        Check msisdn uniqueness
        """
        return await self._build_for_check_admin_msisdn(msisdn_model=msisdn_model)

    async def create_admin(self, admin_create: m.AdminCreate) -> m.AdminResponse:
        """
        Create new admin.
        """
        return await self._build_for_create_admin(admin_create=admin_create)

    async def disable_admin(self, id: UUID) -> m.AdminResponse:
        """
        Disable admin
        """
        return await self._build_for_disable_admin(id=id)

    async def enable_admin(self, id: UUID) -> m.AdminResponse:
        """
        Enable admin
        """
        return await self._build_for_enable_admin(id=id)

    async def get_admin(self, id: UUID) -> m.AdminResponse:
        """
        Get a specific admin by id.
        """
        return await self._build_for_get_admin(id=id)

    async def list_admins(
        self,
    ) -> m.AdminListResponse:
        """
        List admins
        """
        return await self._build_for_list_admins()

    async def login_admin(self, admin_login: m.AdminLogin) -> m.AdminResponse:
        """
        Admin login
        """
        return await self._build_for_login_admin(admin_login=admin_login)

    async def set_admin_password(self, id: UUID, password_model: m.PasswordModel) -> m.AdminResponse:
        """
        Set admin password
        """
        return await self._build_for_set_admin_password(id=id, password_model=password_model)

    async def update_admin(self, id: UUID, admin_update: m.AdminUpdate) -> m.AdminResponse:
        """
        Update an admin.
        """
        return await self._build_for_update_admin(id=id, admin_update=admin_update)


class SyncAdminApi(_AdminApi):
    def admin_json(self, body: Any) -> m.Any:
        coroutine = self._build_for_admin_json(body=body)
        return get_event_loop().run_until_complete(coroutine)

    def check_admin_email(self, email_model: m.EmailModel) -> m.AdminResponse:
        """
        Check email uniqueness
        """
        coroutine = self._build_for_check_admin_email(email_model=email_model)
        return get_event_loop().run_until_complete(coroutine)

    def check_admin_msisdn(self, msisdn_model: m.MSISDNModel) -> m.AdminResponse:
        """
        Check msisdn uniqueness
        """
        coroutine = self._build_for_check_admin_msisdn(msisdn_model=msisdn_model)
        return get_event_loop().run_until_complete(coroutine)

    def create_admin(self, admin_create: m.AdminCreate) -> m.AdminResponse:
        """
        Create new admin.
        """
        coroutine = self._build_for_create_admin(admin_create=admin_create)
        return get_event_loop().run_until_complete(coroutine)

    def disable_admin(self, id: UUID) -> m.AdminResponse:
        """
        Disable admin
        """
        coroutine = self._build_for_disable_admin(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def enable_admin(self, id: UUID) -> m.AdminResponse:
        """
        Enable admin
        """
        coroutine = self._build_for_enable_admin(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_admin(self, id: UUID) -> m.AdminResponse:
        """
        Get a specific admin by id.
        """
        coroutine = self._build_for_get_admin(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_admins(
        self,
    ) -> m.AdminListResponse:
        """
        List admins
        """
        coroutine = self._build_for_list_admins()
        return get_event_loop().run_until_complete(coroutine)

    def login_admin(self, admin_login: m.AdminLogin) -> m.AdminResponse:
        """
        Admin login
        """
        coroutine = self._build_for_login_admin(admin_login=admin_login)
        return get_event_loop().run_until_complete(coroutine)

    def set_admin_password(self, id: UUID, password_model: m.PasswordModel) -> m.AdminResponse:
        """
        Set admin password
        """
        coroutine = self._build_for_set_admin_password(id=id, password_model=password_model)
        return get_event_loop().run_until_complete(coroutine)

    def update_admin(self, id: UUID, admin_update: m.AdminUpdate) -> m.AdminResponse:
        """
        Update an admin.
        """
        coroutine = self._build_for_update_admin(id=id, admin_update=admin_update)
        return get_event_loop().run_until_complete(coroutine)
