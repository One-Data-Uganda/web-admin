# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from app.services.api.project import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.project.api_client import ApiClient


class _PowerScheduleApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_power_schedule(
        self, power_schedule_create: m.PowerScheduleCreate
    ) -> Awaitable[m.PowerScheduleResponse]:
        """
        Create new power_schedule.
        """
        body = jsonable_encoder(power_schedule_create)

        return self.api_client.request(
            type_=m.PowerScheduleResponse, method="POST", url="/v1/power-schedule/", json=body
        )

    def _build_for_delete_power_schedule(self, id: str) -> Awaitable[m.PowerScheduleResponse]:
        """
        Delete a power schedule.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.PowerScheduleResponse,
            method="DELETE",
            url="/v1/power-schedule/{id}",
            path_params=path_params,
        )

    def _build_for_get_power_schedule(self, id: str) -> Awaitable[m.PowerScheduleResponse]:
        """
        Get power schedule by ID.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.PowerScheduleResponse,
            method="GET",
            url="/v1/power-schedule/{id}",
            path_params=path_params,
        )

    def _build_for_list_power_schedules(
        self,
    ) -> Awaitable[m.PowerScheduleListResponse]:
        """
        Retrieve power schedules.
        """
        return self.api_client.request(
            type_=m.PowerScheduleListResponse,
            method="GET",
            url="/v1/power-schedule/",
        )

    def _build_for_update_power_schedule(
        self, id: str, power_schedule_update: m.PowerScheduleUpdate
    ) -> Awaitable[m.PowerScheduleResponse]:
        """
        Update a power schedule.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(power_schedule_update)

        return self.api_client.request(
            type_=m.PowerScheduleResponse,
            method="PUT",
            url="/v1/power-schedule/{id}",
            path_params=path_params,
            json=body,
        )


class AsyncPowerScheduleApi(_PowerScheduleApi):
    async def create_power_schedule(self, power_schedule_create: m.PowerScheduleCreate) -> m.PowerScheduleResponse:
        """
        Create new power_schedule.
        """
        return await self._build_for_create_power_schedule(power_schedule_create=power_schedule_create)

    async def delete_power_schedule(self, id: str) -> m.PowerScheduleResponse:
        """
        Delete a power schedule.
        """
        return await self._build_for_delete_power_schedule(id=id)

    async def get_power_schedule(self, id: str) -> m.PowerScheduleResponse:
        """
        Get power schedule by ID.
        """
        return await self._build_for_get_power_schedule(id=id)

    async def list_power_schedules(
        self,
    ) -> m.PowerScheduleListResponse:
        """
        Retrieve power schedules.
        """
        return await self._build_for_list_power_schedules()

    async def update_power_schedule(
        self, id: str, power_schedule_update: m.PowerScheduleUpdate
    ) -> m.PowerScheduleResponse:
        """
        Update a power schedule.
        """
        return await self._build_for_update_power_schedule(id=id, power_schedule_update=power_schedule_update)


class SyncPowerScheduleApi(_PowerScheduleApi):
    def create_power_schedule(self, power_schedule_create: m.PowerScheduleCreate) -> m.PowerScheduleResponse:
        """
        Create new power_schedule.
        """
        coroutine = self._build_for_create_power_schedule(power_schedule_create=power_schedule_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_power_schedule(self, id: str) -> m.PowerScheduleResponse:
        """
        Delete a power schedule.
        """
        coroutine = self._build_for_delete_power_schedule(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_power_schedule(self, id: str) -> m.PowerScheduleResponse:
        """
        Get power schedule by ID.
        """
        coroutine = self._build_for_get_power_schedule(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_power_schedules(
        self,
    ) -> m.PowerScheduleListResponse:
        """
        Retrieve power schedules.
        """
        coroutine = self._build_for_list_power_schedules()
        return get_event_loop().run_until_complete(coroutine)

    def update_power_schedule(self, id: str, power_schedule_update: m.PowerScheduleUpdate) -> m.PowerScheduleResponse:
        """
        Update a power schedule.
        """
        coroutine = self._build_for_update_power_schedule(id=id, power_schedule_update=power_schedule_update)
        return get_event_loop().run_until_complete(coroutine)
