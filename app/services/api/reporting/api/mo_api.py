# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Any, Awaitable
from uuid import UUID

from app.services.api.reporting import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.reporting.api_client import ApiClient


class _MoApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_mo_graph(self, body: Any) -> Awaitable[m.Any]:
        """
        MO Graph JSON
        """
        body = jsonable_encoder(body)

        return self.api_client.request(type_=m.Any, method="POST", url="/v1/mo/graph", json=body)

    def _build_for_mo_report(self, account_id: UUID, body: Any) -> Awaitable[m.Any]:
        """
        MO JSON
        """
        path_params = {"account_id": str(account_id)}

        body = jsonable_encoder(body)

        return self.api_client.request(
            type_=m.Any, method="POST", url="/v1/mo/report/{account_id}", path_params=path_params, json=body
        )

    def _build_for_mo_report_admin(self, body: Any) -> Awaitable[m.Any]:
        """
        MO JSON
        """
        body = jsonable_encoder(body)

        return self.api_client.request(type_=m.Any, method="POST", url="/v1/mo/report", json=body)

    def _build_for_mo_summary(self, account_id: UUID, body: Any) -> Awaitable[m.Any]:
        """
        MO Summary
        """
        path_params = {"account_id": str(account_id)}

        body = jsonable_encoder(body)

        return self.api_client.request(
            type_=m.Any, method="POST", url="/v1/mo/summary/{account_id}", path_params=path_params, json=body
        )

    def _build_for_mo_summary_admin(self, body: Any) -> Awaitable[m.Any]:
        """
        MO Summary
        """
        body = jsonable_encoder(body)

        return self.api_client.request(type_=m.Any, method="POST", url="/v1/mo/summary", json=body)


class AsyncMoApi(_MoApi):
    async def mo_graph(self, body: Any) -> m.Any:
        """
        MO Graph JSON
        """
        return await self._build_for_mo_graph(body=body)

    async def mo_report(self, account_id: UUID, body: Any) -> m.Any:
        """
        MO JSON
        """
        return await self._build_for_mo_report(account_id=account_id, body=body)

    async def mo_report_admin(self, body: Any) -> m.Any:
        """
        MO JSON
        """
        return await self._build_for_mo_report_admin(body=body)

    async def mo_summary(self, account_id: UUID, body: Any) -> m.Any:
        """
        MO Summary
        """
        return await self._build_for_mo_summary(account_id=account_id, body=body)

    async def mo_summary_admin(self, body: Any) -> m.Any:
        """
        MO Summary
        """
        return await self._build_for_mo_summary_admin(body=body)


class SyncMoApi(_MoApi):
    def mo_graph(self, body: Any) -> m.Any:
        """
        MO Graph JSON
        """
        coroutine = self._build_for_mo_graph(body=body)
        return get_event_loop().run_until_complete(coroutine)

    def mo_report(self, account_id: UUID, body: Any) -> m.Any:
        """
        MO JSON
        """
        coroutine = self._build_for_mo_report(account_id=account_id, body=body)
        return get_event_loop().run_until_complete(coroutine)

    def mo_report_admin(self, body: Any) -> m.Any:
        """
        MO JSON
        """
        coroutine = self._build_for_mo_report_admin(body=body)
        return get_event_loop().run_until_complete(coroutine)

    def mo_summary(self, account_id: UUID, body: Any) -> m.Any:
        """
        MO Summary
        """
        coroutine = self._build_for_mo_summary(account_id=account_id, body=body)
        return get_event_loop().run_until_complete(coroutine)

    def mo_summary_admin(self, body: Any) -> m.Any:
        """
        MO Summary
        """
        coroutine = self._build_for_mo_summary_admin(body=body)
        return get_event_loop().run_until_complete(coroutine)
