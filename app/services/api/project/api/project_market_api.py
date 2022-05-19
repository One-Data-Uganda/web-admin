# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from app.services.api.project import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.project.api_client import ApiClient


class _ProjectMarketApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_project_market(
        self, project_market_create: m.ProjectMarketCreate
    ) -> Awaitable[m.ProjectMarketResponse]:
        """
        Create new project_market.
        """
        body = jsonable_encoder(project_market_create)

        return self.api_client.request(
            type_=m.ProjectMarketResponse, method="POST", url="/v1/project-market/", json=body
        )

    def _build_for_delete_project_market(self, id: str) -> Awaitable[m.ProjectMarketResponse]:
        """
        Delete a project market.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.ProjectMarketResponse,
            method="DELETE",
            url="/v1/project-market/{id}",
            path_params=path_params,
        )

    def _build_for_get_project_market(self, id: str) -> Awaitable[m.ProjectMarketResponse]:
        """
        Get project market by ID.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.ProjectMarketResponse,
            method="GET",
            url="/v1/project-market/{id}",
            path_params=path_params,
        )

    def _build_for_list_project_markets(
        self,
    ) -> Awaitable[m.ProjectMarketListResponse]:
        """
        Retrieve project markets.
        """
        return self.api_client.request(
            type_=m.ProjectMarketListResponse,
            method="GET",
            url="/v1/project-market/",
        )

    def _build_for_update_project_market(
        self, id: str, project_market_update: m.ProjectMarketUpdate
    ) -> Awaitable[m.ProjectMarketResponse]:
        """
        Update a project market.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(project_market_update)

        return self.api_client.request(
            type_=m.ProjectMarketResponse,
            method="PUT",
            url="/v1/project-market/{id}",
            path_params=path_params,
            json=body,
        )


class AsyncProjectMarketApi(_ProjectMarketApi):
    async def create_project_market(self, project_market_create: m.ProjectMarketCreate) -> m.ProjectMarketResponse:
        """
        Create new project_market.
        """
        return await self._build_for_create_project_market(project_market_create=project_market_create)

    async def delete_project_market(self, id: str) -> m.ProjectMarketResponse:
        """
        Delete a project market.
        """
        return await self._build_for_delete_project_market(id=id)

    async def get_project_market(self, id: str) -> m.ProjectMarketResponse:
        """
        Get project market by ID.
        """
        return await self._build_for_get_project_market(id=id)

    async def list_project_markets(
        self,
    ) -> m.ProjectMarketListResponse:
        """
        Retrieve project markets.
        """
        return await self._build_for_list_project_markets()

    async def update_project_market(
        self, id: str, project_market_update: m.ProjectMarketUpdate
    ) -> m.ProjectMarketResponse:
        """
        Update a project market.
        """
        return await self._build_for_update_project_market(id=id, project_market_update=project_market_update)


class SyncProjectMarketApi(_ProjectMarketApi):
    def create_project_market(self, project_market_create: m.ProjectMarketCreate) -> m.ProjectMarketResponse:
        """
        Create new project_market.
        """
        coroutine = self._build_for_create_project_market(project_market_create=project_market_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_project_market(self, id: str) -> m.ProjectMarketResponse:
        """
        Delete a project market.
        """
        coroutine = self._build_for_delete_project_market(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_project_market(self, id: str) -> m.ProjectMarketResponse:
        """
        Get project market by ID.
        """
        coroutine = self._build_for_get_project_market(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_project_markets(
        self,
    ) -> m.ProjectMarketListResponse:
        """
        Retrieve project markets.
        """
        coroutine = self._build_for_list_project_markets()
        return get_event_loop().run_until_complete(coroutine)

    def update_project_market(self, id: str, project_market_update: m.ProjectMarketUpdate) -> m.ProjectMarketResponse:
        """
        Update a project market.
        """
        coroutine = self._build_for_update_project_market(id=id, project_market_update=project_market_update)
        return get_event_loop().run_until_complete(coroutine)
