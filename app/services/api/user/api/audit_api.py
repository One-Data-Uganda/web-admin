# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Any, Awaitable
from uuid import UUID

from app.services.api.user import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.user.api_client import ApiClient


class _AuditApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_account_audit_json(self, account_id: UUID, body: Any) -> Awaitable[m.Any]:
        path_params = {"account_id": str(account_id)}

        body = jsonable_encoder(body)

        return self.api_client.request(
            type_=m.Any, method="POST", url="/v1/audit/{account_id}/json", path_params=path_params, json=body
        )

    def _build_for_admin_audit_json(self, body: Any) -> Awaitable[m.Any]:
        """
        Get audit records for admins
        """
        body = jsonable_encoder(body)

        return self.api_client.request(type_=m.Any, method="POST", url="/v1/audit/json/admin", json=body)

    def _build_for_audit_json(self, body: Any) -> Awaitable[m.Any]:
        """
        Get all account audit records
        """
        body = jsonable_encoder(body)

        return self.api_client.request(type_=m.Any, method="POST", url="/v1/audit/json", json=body)


class AsyncAuditApi(_AuditApi):
    async def account_audit_json(self, account_id: UUID, body: Any) -> m.Any:
        return await self._build_for_account_audit_json(account_id=account_id, body=body)

    async def admin_audit_json(self, body: Any) -> m.Any:
        """
        Get audit records for admins
        """
        return await self._build_for_admin_audit_json(body=body)

    async def audit_json(self, body: Any) -> m.Any:
        """
        Get all account audit records
        """
        return await self._build_for_audit_json(body=body)


class SyncAuditApi(_AuditApi):
    def account_audit_json(self, account_id: UUID, body: Any) -> m.Any:
        coroutine = self._build_for_account_audit_json(account_id=account_id, body=body)
        return get_event_loop().run_until_complete(coroutine)

    def admin_audit_json(self, body: Any) -> m.Any:
        """
        Get audit records for admins
        """
        coroutine = self._build_for_admin_audit_json(body=body)
        return get_event_loop().run_until_complete(coroutine)

    def audit_json(self, body: Any) -> m.Any:
        """
        Get all account audit records
        """
        coroutine = self._build_for_audit_json(body=body)
        return get_event_loop().run_until_complete(coroutine)
