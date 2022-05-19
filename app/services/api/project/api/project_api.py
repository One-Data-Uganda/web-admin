# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable
from uuid import UUID

from app.services.api.project import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.project.api_client import ApiClient


class _ProjectApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_project(self, project_create: m.ProjectCreate) -> Awaitable[m.ProjectResponse]:
        """
        Create new project.
        """
        body = jsonable_encoder(project_create)

        return self.api_client.request(type_=m.ProjectResponse, method="POST", url="/v1/project/", json=body)

    def _build_for_delete_project(self, id: UUID) -> Awaitable[m.ProjectResponse]:
        """
        Delete a project.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.ProjectResponse,
            method="DELETE",
            url="/v1/project/{id}",
            path_params=path_params,
        )

    def _build_for_get_project(self, id: UUID) -> Awaitable[m.ProjectResponse]:
        """
        Get project by ID.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.ProjectResponse,
            method="GET",
            url="/v1/project/{id}",
            path_params=path_params,
        )

    def _build_for_list_projects(
        self,
    ) -> Awaitable[m.ProjectListResponse]:
        """
        Retrieve projects.
        """
        return self.api_client.request(
            type_=m.ProjectListResponse,
            method="GET",
            url="/v1/project/",
        )

    def _build_for_update_project(self, id: UUID, project_update: m.ProjectUpdate) -> Awaitable[m.ProjectResponse]:
        """
        Update a project.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(project_update)

        return self.api_client.request(
            type_=m.ProjectResponse, method="PUT", url="/v1/project/{id}", path_params=path_params, json=body
        )


class AsyncProjectApi(_ProjectApi):
    async def create_project(self, project_create: m.ProjectCreate) -> m.ProjectResponse:
        """
        Create new project.
        """
        return await self._build_for_create_project(project_create=project_create)

    async def delete_project(self, id: UUID) -> m.ProjectResponse:
        """
        Delete a project.
        """
        return await self._build_for_delete_project(id=id)

    async def get_project(self, id: UUID) -> m.ProjectResponse:
        """
        Get project by ID.
        """
        return await self._build_for_get_project(id=id)

    async def list_projects(
        self,
    ) -> m.ProjectListResponse:
        """
        Retrieve projects.
        """
        return await self._build_for_list_projects()

    async def update_project(self, id: UUID, project_update: m.ProjectUpdate) -> m.ProjectResponse:
        """
        Update a project.
        """
        return await self._build_for_update_project(id=id, project_update=project_update)


class SyncProjectApi(_ProjectApi):
    def create_project(self, project_create: m.ProjectCreate) -> m.ProjectResponse:
        """
        Create new project.
        """
        coroutine = self._build_for_create_project(project_create=project_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_project(self, id: UUID) -> m.ProjectResponse:
        """
        Delete a project.
        """
        coroutine = self._build_for_delete_project(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_project(self, id: UUID) -> m.ProjectResponse:
        """
        Get project by ID.
        """
        coroutine = self._build_for_get_project(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_projects(
        self,
    ) -> m.ProjectListResponse:
        """
        Retrieve projects.
        """
        coroutine = self._build_for_list_projects()
        return get_event_loop().run_until_complete(coroutine)

    def update_project(self, id: UUID, project_update: m.ProjectUpdate) -> m.ProjectResponse:
        """
        Update a project.
        """
        coroutine = self._build_for_update_project(id=id, project_update=project_update)
        return get_event_loop().run_until_complete(coroutine)
