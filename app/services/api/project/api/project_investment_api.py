# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from app.services.api.project import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.project.api_client import ApiClient


class _ProjectInvestmentApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_project_investment(
        self, project_investment_create: m.ProjectInvestmentCreate
    ) -> Awaitable[m.ProjectInvestmentResponse]:
        """
        Create new project_investment.
        """
        body = jsonable_encoder(project_investment_create)

        return self.api_client.request(
            type_=m.ProjectInvestmentResponse, method="POST", url="/v1/project-investment/", json=body
        )

    def _build_for_delete_project_investment(self, id: str) -> Awaitable[m.ProjectInvestmentResponse]:
        """
        Delete a project investment.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.ProjectInvestmentResponse,
            method="DELETE",
            url="/v1/project-investment/{id}",
            path_params=path_params,
        )

    def _build_for_get_project_investment(self, id: str) -> Awaitable[m.ProjectInvestmentResponse]:
        """
        Get project investment by ID.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.ProjectInvestmentResponse,
            method="GET",
            url="/v1/project-investment/{id}",
            path_params=path_params,
        )

    def _build_for_list_project_investments(
        self,
    ) -> Awaitable[m.ProjectInvestmentListResponse]:
        """
        Retrieve project investments.
        """
        return self.api_client.request(
            type_=m.ProjectInvestmentListResponse,
            method="GET",
            url="/v1/project-investment/",
        )

    def _build_for_update_project_investment(
        self, id: str, project_investment_update: m.ProjectInvestmentUpdate
    ) -> Awaitable[m.ProjectInvestmentResponse]:
        """
        Update a project investment.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(project_investment_update)

        return self.api_client.request(
            type_=m.ProjectInvestmentResponse,
            method="PUT",
            url="/v1/project-investment/{id}",
            path_params=path_params,
            json=body,
        )


class AsyncProjectInvestmentApi(_ProjectInvestmentApi):
    async def create_project_investment(
        self, project_investment_create: m.ProjectInvestmentCreate
    ) -> m.ProjectInvestmentResponse:
        """
        Create new project_investment.
        """
        return await self._build_for_create_project_investment(project_investment_create=project_investment_create)

    async def delete_project_investment(self, id: str) -> m.ProjectInvestmentResponse:
        """
        Delete a project investment.
        """
        return await self._build_for_delete_project_investment(id=id)

    async def get_project_investment(self, id: str) -> m.ProjectInvestmentResponse:
        """
        Get project investment by ID.
        """
        return await self._build_for_get_project_investment(id=id)

    async def list_project_investments(
        self,
    ) -> m.ProjectInvestmentListResponse:
        """
        Retrieve project investments.
        """
        return await self._build_for_list_project_investments()

    async def update_project_investment(
        self, id: str, project_investment_update: m.ProjectInvestmentUpdate
    ) -> m.ProjectInvestmentResponse:
        """
        Update a project investment.
        """
        return await self._build_for_update_project_investment(
            id=id, project_investment_update=project_investment_update
        )


class SyncProjectInvestmentApi(_ProjectInvestmentApi):
    def create_project_investment(
        self, project_investment_create: m.ProjectInvestmentCreate
    ) -> m.ProjectInvestmentResponse:
        """
        Create new project_investment.
        """
        coroutine = self._build_for_create_project_investment(project_investment_create=project_investment_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_project_investment(self, id: str) -> m.ProjectInvestmentResponse:
        """
        Delete a project investment.
        """
        coroutine = self._build_for_delete_project_investment(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_project_investment(self, id: str) -> m.ProjectInvestmentResponse:
        """
        Get project investment by ID.
        """
        coroutine = self._build_for_get_project_investment(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_project_investments(
        self,
    ) -> m.ProjectInvestmentListResponse:
        """
        Retrieve project investments.
        """
        coroutine = self._build_for_list_project_investments()
        return get_event_loop().run_until_complete(coroutine)

    def update_project_investment(
        self, id: str, project_investment_update: m.ProjectInvestmentUpdate
    ) -> m.ProjectInvestmentResponse:
        """
        Update a project investment.
        """
        coroutine = self._build_for_update_project_investment(
            id=id, project_investment_update=project_investment_update
        )
        return get_event_loop().run_until_complete(coroutine)
