# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from app.services.api.project import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.project.api_client import ApiClient


class _ProjectTeamApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_project_team(
        self, project_team_create: m.ProjectTeamCreate
    ) -> Awaitable[m.ProjectTeamResponse]:
        """
        Create new project_team.
        """
        body = jsonable_encoder(project_team_create)

        return self.api_client.request(type_=m.ProjectTeamResponse, method="POST", url="/v1/project-team/", json=body)

    def _build_for_delete_project_team(self, id: str) -> Awaitable[m.ProjectTeamResponse]:
        """
        Delete a project team.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.ProjectTeamResponse,
            method="DELETE",
            url="/v1/project-team/{id}",
            path_params=path_params,
        )

    def _build_for_get_project_team(self, id: str) -> Awaitable[m.ProjectTeamResponse]:
        """
        Get project team by ID.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.ProjectTeamResponse,
            method="GET",
            url="/v1/project-team/{id}",
            path_params=path_params,
        )

    def _build_for_list_project_teams(
        self,
    ) -> Awaitable[m.ProjectTeamListResponse]:
        """
        Retrieve project teams.
        """
        return self.api_client.request(
            type_=m.ProjectTeamListResponse,
            method="GET",
            url="/v1/project-team/",
        )

    def _build_for_update_project_team(
        self, id: str, project_team_update: m.ProjectTeamUpdate
    ) -> Awaitable[m.ProjectTeamResponse]:
        """
        Update a project team.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(project_team_update)

        return self.api_client.request(
            type_=m.ProjectTeamResponse, method="PUT", url="/v1/project-team/{id}", path_params=path_params, json=body
        )


class AsyncProjectTeamApi(_ProjectTeamApi):
    async def create_project_team(self, project_team_create: m.ProjectTeamCreate) -> m.ProjectTeamResponse:
        """
        Create new project_team.
        """
        return await self._build_for_create_project_team(project_team_create=project_team_create)

    async def delete_project_team(self, id: str) -> m.ProjectTeamResponse:
        """
        Delete a project team.
        """
        return await self._build_for_delete_project_team(id=id)

    async def get_project_team(self, id: str) -> m.ProjectTeamResponse:
        """
        Get project team by ID.
        """
        return await self._build_for_get_project_team(id=id)

    async def list_project_teams(
        self,
    ) -> m.ProjectTeamListResponse:
        """
        Retrieve project teams.
        """
        return await self._build_for_list_project_teams()

    async def update_project_team(self, id: str, project_team_update: m.ProjectTeamUpdate) -> m.ProjectTeamResponse:
        """
        Update a project team.
        """
        return await self._build_for_update_project_team(id=id, project_team_update=project_team_update)


class SyncProjectTeamApi(_ProjectTeamApi):
    def create_project_team(self, project_team_create: m.ProjectTeamCreate) -> m.ProjectTeamResponse:
        """
        Create new project_team.
        """
        coroutine = self._build_for_create_project_team(project_team_create=project_team_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_project_team(self, id: str) -> m.ProjectTeamResponse:
        """
        Delete a project team.
        """
        coroutine = self._build_for_delete_project_team(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_project_team(self, id: str) -> m.ProjectTeamResponse:
        """
        Get project team by ID.
        """
        coroutine = self._build_for_get_project_team(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_project_teams(
        self,
    ) -> m.ProjectTeamListResponse:
        """
        Retrieve project teams.
        """
        coroutine = self._build_for_list_project_teams()
        return get_event_loop().run_until_complete(coroutine)

    def update_project_team(self, id: str, project_team_update: m.ProjectTeamUpdate) -> m.ProjectTeamResponse:
        """
        Update a project team.
        """
        coroutine = self._build_for_update_project_team(id=id, project_team_update=project_team_update)
        return get_event_loop().run_until_complete(coroutine)
