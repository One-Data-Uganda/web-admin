# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Any, Awaitable
from uuid import UUID

from app.services.api.user import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.user.api_client import ApiClient


class _UserApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_check_password(self, password_model: m.PasswordModel) -> Awaitable[m.FailureResponseModel]:
        """
        Check password Complexity
        """
        body = jsonable_encoder(password_model)

        return self.api_client.request(
            type_=m.FailureResponseModel, method="POST", url="/v1/user/check-password", json=body
        )

    def _build_for_check_user_email(self, email_model: m.EmailModel) -> Awaitable[m.UserResponse]:
        """
        Check email uniqueness
        """
        body = jsonable_encoder(email_model)

        return self.api_client.request(type_=m.UserResponse, method="POST", url="/v1/user/check-email", json=body)

    def _build_for_check_user_msisdn(self, msisdn_model: m.MSISDNModel) -> Awaitable[m.UserResponse]:
        """
        Check msisdn uniqueness
        """
        body = jsonable_encoder(msisdn_model)

        return self.api_client.request(type_=m.UserResponse, method="POST", url="/v1/user/check-msisdn", json=body)

    def _build_for_create_user(self, user_view_create: m.UserViewCreate) -> Awaitable[m.UserResponse]:
        """
        Create new user.
        """
        body = jsonable_encoder(user_view_create)

        return self.api_client.request(type_=m.UserResponse, method="POST", url="/v1/user/", json=body)

    def _build_for_create_user_with_kyc(self, user_create: m.UserCreate) -> Awaitable[m.UserResponse]:
        """
        Create new user (with KYC).
        """
        body = jsonable_encoder(user_create)

        return self.api_client.request(type_=m.UserResponse, method="POST", url="/v1/user/with-kyc", json=body)

    def _build_for_disable_user(self, id: UUID) -> Awaitable[m.UserResponse]:
        """
        Disable user
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.UserResponse,
            method="PUT",
            url="/v1/user/{id}/disable",
            path_params=path_params,
        )

    def _build_for_enable_user(self, id: UUID) -> Awaitable[m.UserResponse]:
        """
        Enable user
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.UserResponse,
            method="PUT",
            url="/v1/user/{id}/enable",
            path_params=path_params,
        )

    def _build_for_get_user(self, id: UUID) -> Awaitable[m.UserResponse]:
        """
        Get a specific user by id.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.UserResponse,
            method="GET",
            url="/v1/user/{id}",
            path_params=path_params,
        )

    def _build_for_login_user(self, user_login: m.UserLogin) -> Awaitable[m.UserResponse]:
        """
        User login
        """
        body = jsonable_encoder(user_login)

        return self.api_client.request(type_=m.UserResponse, method="POST", url="/v1/user/login", json=body)

    def _build_for_set_password(self, id: UUID, password_model: m.PasswordModel) -> Awaitable[m.UserResponse]:
        """
        Set user password
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(password_model)

        return self.api_client.request(
            type_=m.UserResponse, method="PUT", url="/v1/user/{id}/password", path_params=path_params, json=body
        )

    def _build_for_update_user(self, id: UUID, user_view_update: m.UserViewUpdate) -> Awaitable[m.UserResponse]:
        """
        Update a user.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(user_view_update)

        return self.api_client.request(
            type_=m.UserResponse, method="PUT", url="/v1/user/{id}", path_params=path_params, json=body
        )

    def _build_for_user_account_json(self, account_id: UUID, body: Any) -> Awaitable[m.Any]:
        path_params = {"account_id": str(account_id)}

        body = jsonable_encoder(body)

        return self.api_client.request(
            type_=m.Any, method="POST", url="/v1/user/{account_id}/json", path_params=path_params, json=body
        )


class AsyncUserApi(_UserApi):
    async def check_password(self, password_model: m.PasswordModel) -> m.FailureResponseModel:
        """
        Check password Complexity
        """
        return await self._build_for_check_password(password_model=password_model)

    async def check_user_email(self, email_model: m.EmailModel) -> m.UserResponse:
        """
        Check email uniqueness
        """
        return await self._build_for_check_user_email(email_model=email_model)

    async def check_user_msisdn(self, msisdn_model: m.MSISDNModel) -> m.UserResponse:
        """
        Check msisdn uniqueness
        """
        return await self._build_for_check_user_msisdn(msisdn_model=msisdn_model)

    async def create_user(self, user_view_create: m.UserViewCreate) -> m.UserResponse:
        """
        Create new user.
        """
        return await self._build_for_create_user(user_view_create=user_view_create)

    async def create_user_with_kyc(self, user_create: m.UserCreate) -> m.UserResponse:
        """
        Create new user (with KYC).
        """
        return await self._build_for_create_user_with_kyc(user_create=user_create)

    async def disable_user(self, id: UUID) -> m.UserResponse:
        """
        Disable user
        """
        return await self._build_for_disable_user(id=id)

    async def enable_user(self, id: UUID) -> m.UserResponse:
        """
        Enable user
        """
        return await self._build_for_enable_user(id=id)

    async def get_user(self, id: UUID) -> m.UserResponse:
        """
        Get a specific user by id.
        """
        return await self._build_for_get_user(id=id)

    async def login_user(self, user_login: m.UserLogin) -> m.UserResponse:
        """
        User login
        """
        return await self._build_for_login_user(user_login=user_login)

    async def set_password(self, id: UUID, password_model: m.PasswordModel) -> m.UserResponse:
        """
        Set user password
        """
        return await self._build_for_set_password(id=id, password_model=password_model)

    async def update_user(self, id: UUID, user_view_update: m.UserViewUpdate) -> m.UserResponse:
        """
        Update a user.
        """
        return await self._build_for_update_user(id=id, user_view_update=user_view_update)

    async def user_account_json(self, account_id: UUID, body: Any) -> m.Any:
        return await self._build_for_user_account_json(account_id=account_id, body=body)


class SyncUserApi(_UserApi):
    def check_password(self, password_model: m.PasswordModel) -> m.FailureResponseModel:
        """
        Check password Complexity
        """
        coroutine = self._build_for_check_password(password_model=password_model)
        return get_event_loop().run_until_complete(coroutine)

    def check_user_email(self, email_model: m.EmailModel) -> m.UserResponse:
        """
        Check email uniqueness
        """
        coroutine = self._build_for_check_user_email(email_model=email_model)
        return get_event_loop().run_until_complete(coroutine)

    def check_user_msisdn(self, msisdn_model: m.MSISDNModel) -> m.UserResponse:
        """
        Check msisdn uniqueness
        """
        coroutine = self._build_for_check_user_msisdn(msisdn_model=msisdn_model)
        return get_event_loop().run_until_complete(coroutine)

    def create_user(self, user_view_create: m.UserViewCreate) -> m.UserResponse:
        """
        Create new user.
        """
        coroutine = self._build_for_create_user(user_view_create=user_view_create)
        return get_event_loop().run_until_complete(coroutine)

    def create_user_with_kyc(self, user_create: m.UserCreate) -> m.UserResponse:
        """
        Create new user (with KYC).
        """
        coroutine = self._build_for_create_user_with_kyc(user_create=user_create)
        return get_event_loop().run_until_complete(coroutine)

    def disable_user(self, id: UUID) -> m.UserResponse:
        """
        Disable user
        """
        coroutine = self._build_for_disable_user(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def enable_user(self, id: UUID) -> m.UserResponse:
        """
        Enable user
        """
        coroutine = self._build_for_enable_user(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_user(self, id: UUID) -> m.UserResponse:
        """
        Get a specific user by id.
        """
        coroutine = self._build_for_get_user(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def login_user(self, user_login: m.UserLogin) -> m.UserResponse:
        """
        User login
        """
        coroutine = self._build_for_login_user(user_login=user_login)
        return get_event_loop().run_until_complete(coroutine)

    def set_password(self, id: UUID, password_model: m.PasswordModel) -> m.UserResponse:
        """
        Set user password
        """
        coroutine = self._build_for_set_password(id=id, password_model=password_model)
        return get_event_loop().run_until_complete(coroutine)

    def update_user(self, id: UUID, user_view_update: m.UserViewUpdate) -> m.UserResponse:
        """
        Update a user.
        """
        coroutine = self._build_for_update_user(id=id, user_view_update=user_view_update)
        return get_event_loop().run_until_complete(coroutine)

    def user_account_json(self, account_id: UUID, body: Any) -> m.Any:
        coroutine = self._build_for_user_account_json(account_id=account_id, body=body)
        return get_event_loop().run_until_complete(coroutine)
