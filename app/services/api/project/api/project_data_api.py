# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from app.services.api.project import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.project.api_client import ApiClient


class _ProjectDataApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_project_data(
        self, project_data_create: m.ProjectDataCreate
    ) -> Awaitable[m.ProjectDataResponse]:
        """
        Create new project_data.
        """
        body = jsonable_encoder(project_data_create)

        return self.api_client.request(type_=m.ProjectDataResponse, method="POST", url="/v1/project-data/", json=body)

    def _build_for_delete_project_data(self, id: str) -> Awaitable[m.ProjectDataResponse]:
        """
        Delete a project data.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.ProjectDataResponse,
            method="DELETE",
            url="/v1/project-data/{id}",
            path_params=path_params,
        )

    def _build_for_get_project_data(self, id: str) -> Awaitable[m.ProjectDataResponse]:
        """
        Get project data by ID.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.ProjectDataResponse,
            method="GET",
            url="/v1/project-data/{id}",
            path_params=path_params,
        )

    def _build_for_list_project_datas(
        self,
    ) -> Awaitable[m.ProjectDataListResponse]:
        """
        Retrieve project datas.
        """
        return self.api_client.request(
            type_=m.ProjectDataListResponse,
            method="GET",
            url="/v1/project-data/",
        )

    def _build_for_update_project_data(
        self, id: str, project_data_update: m.ProjectDataUpdate
    ) -> Awaitable[m.ProjectDataResponse]:
        """
        Update a project data.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(project_data_update)

        return self.api_client.request(
            type_=m.ProjectDataResponse, method="PUT", url="/v1/project-data/{id}", path_params=path_params, json=body
        )


class AsyncProjectDataApi(_ProjectDataApi):
    async def create_project_data(self, project_data_create: m.ProjectDataCreate) -> m.ProjectDataResponse:
        """
        Create new project_data.
        """
        return await self._build_for_create_project_data(project_data_create=project_data_create)

    async def delete_project_data(self, id: str) -> m.ProjectDataResponse:
        """
        Delete a project data.
        """
        return await self._build_for_delete_project_data(id=id)

    async def get_project_data(self, id: str) -> m.ProjectDataResponse:
        """
        Get project data by ID.
        """
        return await self._build_for_get_project_data(id=id)

    async def list_project_datas(
        self,
    ) -> m.ProjectDataListResponse:
        """
        Retrieve project datas.
        """
        return await self._build_for_list_project_datas()

    async def update_project_data(self, id: str, project_data_update: m.ProjectDataUpdate) -> m.ProjectDataResponse:
        """
        Update a project data.
        """
        return await self._build_for_update_project_data(id=id, project_data_update=project_data_update)


class SyncProjectDataApi(_ProjectDataApi):
    def create_project_data(self, project_data_create: m.ProjectDataCreate) -> m.ProjectDataResponse:
        """
        Create new project_data.
        """
        coroutine = self._build_for_create_project_data(project_data_create=project_data_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_project_data(self, id: str) -> m.ProjectDataResponse:
        """
        Delete a project data.
        """
        coroutine = self._build_for_delete_project_data(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_project_data(self, id: str) -> m.ProjectDataResponse:
        """
        Get project data by ID.
        """
        coroutine = self._build_for_get_project_data(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_project_datas(
        self,
    ) -> m.ProjectDataListResponse:
        """
        Retrieve project datas.
        """
        coroutine = self._build_for_list_project_datas()
        return get_event_loop().run_until_complete(coroutine)

    def update_project_data(self, id: str, project_data_update: m.ProjectDataUpdate) -> m.ProjectDataResponse:
        """
        Update a project data.
        """
        coroutine = self._build_for_update_project_data(id=id, project_data_update=project_data_update)
        return get_event_loop().run_until_complete(coroutine)
