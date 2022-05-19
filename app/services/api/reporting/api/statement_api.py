# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from app.services.api.reporting import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.reporting.api_client import ApiClient


class _StatementApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_get_statement(self, statement_model: m.StatementModel) -> Awaitable[m.FailureResponseModel]:
        body = jsonable_encoder(statement_model)

        return self.api_client.request(type_=m.FailureResponseModel, method="POST", url="/v1/statement/", json=body)


class AsyncStatementApi(_StatementApi):
    async def get_statement(self, statement_model: m.StatementModel) -> m.FailureResponseModel:
        return await self._build_for_get_statement(statement_model=statement_model)


class SyncStatementApi(_StatementApi):
    def get_statement(self, statement_model: m.StatementModel) -> m.FailureResponseModel:
        coroutine = self._build_for_get_statement(statement_model=statement_model)
        return get_event_loop().run_until_complete(coroutine)
