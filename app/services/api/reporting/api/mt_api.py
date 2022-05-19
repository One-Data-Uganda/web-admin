# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Any, Awaitable
from uuid import UUID

from app.services.api.reporting import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.reporting.api_client import ApiClient


class _MtApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_mt_graph(self, body: Any) -> Awaitable[m.Any]:
        """
        MT Graph JSON
        """
        body = jsonable_encoder(body)

        return self.api_client.request(type_=m.Any, method="POST", url="/v1/mt/graph", json=body)

    def _build_for_mt_network_admin(self, body: Any) -> Awaitable[m.Any]:
        """
        MT Network JSON
        """
        body = jsonable_encoder(body)

        return self.api_client.request(type_=m.Any, method="POST", url="/v1/mt/network", json=body)

    def _build_for_mt_report(self, account_id: UUID, body: Any) -> Awaitable[m.Any]:
        """
        MT JSON
        """
        path_params = {"account_id": str(account_id)}

        body = jsonable_encoder(body)

        return self.api_client.request(
            type_=m.Any, method="POST", url="/v1/mt/report/{account_id}", path_params=path_params, json=body
        )

    def _build_for_mt_report_admin(self, body: Any) -> Awaitable[m.Any]:
        """
        MT JSON
        """
        body = jsonable_encoder(body)

        return self.api_client.request(type_=m.Any, method="POST", url="/v1/mt/report", json=body)

    def _build_for_mt_report_light(self, body: Any) -> Awaitable[m.Any]:
        """
        MT JSON
        """
        body = jsonable_encoder(body)

        return self.api_client.request(type_=m.Any, method="POST", url="/v1/mt/light", json=body)

    def _build_for_mt_simple_report(self, account_id: UUID, body: Any) -> Awaitable[m.Any]:
        """
        MT JSON
        """
        path_params = {"account_id": str(account_id)}

        body = jsonable_encoder(body)

        return self.api_client.request(
            type_=m.Any, method="POST", url="/v1/mt/simple/{account_id}", path_params=path_params, json=body
        )

    def _build_for_mt_summary(self, account_id: UUID, body: Any) -> Awaitable[m.Any]:
        """
        MT JSON
        """
        path_params = {"account_id": str(account_id)}

        body = jsonable_encoder(body)

        return self.api_client.request(
            type_=m.Any, method="POST", url="/v1/mt/summary/{account_id}", path_params=path_params, json=body
        )

    def _build_for_mt_summary_admin(self, body: Any) -> Awaitable[m.Any]:
        """
        MT JSON
        """
        body = jsonable_encoder(body)

        return self.api_client.request(type_=m.Any, method="POST", url="/v1/mt/summary", json=body)


class AsyncMtApi(_MtApi):
    async def mt_graph(self, body: Any) -> m.Any:
        """
        MT Graph JSON
        """
        return await self._build_for_mt_graph(body=body)

    async def mt_network_admin(self, body: Any) -> m.Any:
        """
        MT Network JSON
        """
        return await self._build_for_mt_network_admin(body=body)

    async def mt_report(self, account_id: UUID, body: Any) -> m.Any:
        """
        MT JSON
        """
        return await self._build_for_mt_report(account_id=account_id, body=body)

    async def mt_report_admin(self, body: Any) -> m.Any:
        """
        MT JSON
        """
        return await self._build_for_mt_report_admin(body=body)

    async def mt_report_light(self, body: Any) -> m.Any:
        """
        MT JSON
        """
        return await self._build_for_mt_report_light(body=body)

    async def mt_simple_report(self, account_id: UUID, body: Any) -> m.Any:
        """
        MT JSON
        """
        return await self._build_for_mt_simple_report(account_id=account_id, body=body)

    async def mt_summary(self, account_id: UUID, body: Any) -> m.Any:
        """
        MT JSON
        """
        return await self._build_for_mt_summary(account_id=account_id, body=body)

    async def mt_summary_admin(self, body: Any) -> m.Any:
        """
        MT JSON
        """
        return await self._build_for_mt_summary_admin(body=body)


class SyncMtApi(_MtApi):
    def mt_graph(self, body: Any) -> m.Any:
        """
        MT Graph JSON
        """
        coroutine = self._build_for_mt_graph(body=body)
        return get_event_loop().run_until_complete(coroutine)

    def mt_network_admin(self, body: Any) -> m.Any:
        """
        MT Network JSON
        """
        coroutine = self._build_for_mt_network_admin(body=body)
        return get_event_loop().run_until_complete(coroutine)

    def mt_report(self, account_id: UUID, body: Any) -> m.Any:
        """
        MT JSON
        """
        coroutine = self._build_for_mt_report(account_id=account_id, body=body)
        return get_event_loop().run_until_complete(coroutine)

    def mt_report_admin(self, body: Any) -> m.Any:
        """
        MT JSON
        """
        coroutine = self._build_for_mt_report_admin(body=body)
        return get_event_loop().run_until_complete(coroutine)

    def mt_report_light(self, body: Any) -> m.Any:
        """
        MT JSON
        """
        coroutine = self._build_for_mt_report_light(body=body)
        return get_event_loop().run_until_complete(coroutine)

    def mt_simple_report(self, account_id: UUID, body: Any) -> m.Any:
        """
        MT JSON
        """
        coroutine = self._build_for_mt_simple_report(account_id=account_id, body=body)
        return get_event_loop().run_until_complete(coroutine)

    def mt_summary(self, account_id: UUID, body: Any) -> m.Any:
        """
        MT JSON
        """
        coroutine = self._build_for_mt_summary(account_id=account_id, body=body)
        return get_event_loop().run_until_complete(coroutine)

    def mt_summary_admin(self, body: Any) -> m.Any:
        """
        MT JSON
        """
        coroutine = self._build_for_mt_summary_admin(body=body)
        return get_event_loop().run_until_complete(coroutine)
