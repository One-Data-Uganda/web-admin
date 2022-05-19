# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Any, Awaitable
from uuid import UUID

from app.services.api.reporting import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.reporting.api_client import ApiClient


class _GeneralApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_dummy(
        self,
    ) -> Awaitable[m.FailureResponseModel]:
        return self.api_client.request(
            type_=m.FailureResponseModel,
            method="POST",
            url="/v1/general/dummy",
        )

    def _build_for_keyword_json(self, body: Any) -> Awaitable[m.Any]:
        """
        MT JSON
        """
        body = jsonable_encoder(body)

        return self.api_client.request(type_=m.Any, method="POST", url="/v1/general/keyword", json=body)

    def _build_for_keyword_performance_json(self, account_id: UUID, body: Any) -> Awaitable[m.Any]:
        """
        MT JSON
        """
        path_params = {"account_id": str(account_id)}

        body = jsonable_encoder(body)

        return self.api_client.request(
            type_=m.Any,
            method="POST",
            url="/v1/general/keyword-performance/{account_id}",
            path_params=path_params,
            json=body,
        )

    def _build_for_keyword_performance_json_admin(self, body: Any) -> Awaitable[m.Any]:
        """
        MT JSON
        """
        body = jsonable_encoder(body)

        return self.api_client.request(type_=m.Any, method="POST", url="/v1/general/keyword-performance", json=body)

    def _build_for_outbox_json(self, account_id: UUID, body: Any) -> Awaitable[m.Any]:
        """
        MT JSON
        """
        path_params = {"account_id": str(account_id)}

        body = jsonable_encoder(body)

        return self.api_client.request(
            type_=m.Any, method="POST", url="/v1/general/outbox/{account_id}", path_params=path_params, json=body
        )

    def _build_for_sender_json(self, body: Any) -> Awaitable[m.Any]:
        """
        MT JSON
        """
        body = jsonable_encoder(body)

        return self.api_client.request(type_=m.Any, method="POST", url="/v1/general/sender", json=body)


class AsyncGeneralApi(_GeneralApi):
    async def dummy(
        self,
    ) -> m.FailureResponseModel:
        return await self._build_for_dummy()

    async def keyword_json(self, body: Any) -> m.Any:
        """
        MT JSON
        """
        return await self._build_for_keyword_json(body=body)

    async def keyword_performance_json(self, account_id: UUID, body: Any) -> m.Any:
        """
        MT JSON
        """
        return await self._build_for_keyword_performance_json(account_id=account_id, body=body)

    async def keyword_performance_json_admin(self, body: Any) -> m.Any:
        """
        MT JSON
        """
        return await self._build_for_keyword_performance_json_admin(body=body)

    async def outbox_json(self, account_id: UUID, body: Any) -> m.Any:
        """
        MT JSON
        """
        return await self._build_for_outbox_json(account_id=account_id, body=body)

    async def sender_json(self, body: Any) -> m.Any:
        """
        MT JSON
        """
        return await self._build_for_sender_json(body=body)


class SyncGeneralApi(_GeneralApi):
    def dummy(
        self,
    ) -> m.FailureResponseModel:
        coroutine = self._build_for_dummy()
        return get_event_loop().run_until_complete(coroutine)

    def keyword_json(self, body: Any) -> m.Any:
        """
        MT JSON
        """
        coroutine = self._build_for_keyword_json(body=body)
        return get_event_loop().run_until_complete(coroutine)

    def keyword_performance_json(self, account_id: UUID, body: Any) -> m.Any:
        """
        MT JSON
        """
        coroutine = self._build_for_keyword_performance_json(account_id=account_id, body=body)
        return get_event_loop().run_until_complete(coroutine)

    def keyword_performance_json_admin(self, body: Any) -> m.Any:
        """
        MT JSON
        """
        coroutine = self._build_for_keyword_performance_json_admin(body=body)
        return get_event_loop().run_until_complete(coroutine)

    def outbox_json(self, account_id: UUID, body: Any) -> m.Any:
        """
        MT JSON
        """
        coroutine = self._build_for_outbox_json(account_id=account_id, body=body)
        return get_event_loop().run_until_complete(coroutine)

    def sender_json(self, body: Any) -> m.Any:
        """
        MT JSON
        """
        coroutine = self._build_for_sender_json(body=body)
        return get_event_loop().run_until_complete(coroutine)
