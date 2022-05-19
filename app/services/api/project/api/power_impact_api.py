# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from app.services.api.project import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.project.api_client import ApiClient


class _PowerImpactApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_power_impact(
        self, power_impact_create: m.PowerImpactCreate
    ) -> Awaitable[m.PowerImpactResponse]:
        """
        Create new power_impact.
        """
        body = jsonable_encoder(power_impact_create)

        return self.api_client.request(type_=m.PowerImpactResponse, method="POST", url="/v1/power-impact/", json=body)

    def _build_for_delete_power_impact(self, id: str) -> Awaitable[m.PowerImpactResponse]:
        """
        Delete a power impact.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.PowerImpactResponse,
            method="DELETE",
            url="/v1/power-impact/{id}",
            path_params=path_params,
        )

    def _build_for_get_power_impact(self, id: str) -> Awaitable[m.PowerImpactResponse]:
        """
        Get power impact by ID.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.PowerImpactResponse,
            method="GET",
            url="/v1/power-impact/{id}",
            path_params=path_params,
        )

    def _build_for_list_power_impacts(
        self,
    ) -> Awaitable[m.PowerImpactListResponse]:
        """
        Retrieve power impacts.
        """
        return self.api_client.request(
            type_=m.PowerImpactListResponse,
            method="GET",
            url="/v1/power-impact/",
        )

    def _build_for_update_power_impact(
        self, id: str, power_impact_update: m.PowerImpactUpdate
    ) -> Awaitable[m.PowerImpactResponse]:
        """
        Update a power impact.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(power_impact_update)

        return self.api_client.request(
            type_=m.PowerImpactResponse, method="PUT", url="/v1/power-impact/{id}", path_params=path_params, json=body
        )


class AsyncPowerImpactApi(_PowerImpactApi):
    async def create_power_impact(self, power_impact_create: m.PowerImpactCreate) -> m.PowerImpactResponse:
        """
        Create new power_impact.
        """
        return await self._build_for_create_power_impact(power_impact_create=power_impact_create)

    async def delete_power_impact(self, id: str) -> m.PowerImpactResponse:
        """
        Delete a power impact.
        """
        return await self._build_for_delete_power_impact(id=id)

    async def get_power_impact(self, id: str) -> m.PowerImpactResponse:
        """
        Get power impact by ID.
        """
        return await self._build_for_get_power_impact(id=id)

    async def list_power_impacts(
        self,
    ) -> m.PowerImpactListResponse:
        """
        Retrieve power impacts.
        """
        return await self._build_for_list_power_impacts()

    async def update_power_impact(self, id: str, power_impact_update: m.PowerImpactUpdate) -> m.PowerImpactResponse:
        """
        Update a power impact.
        """
        return await self._build_for_update_power_impact(id=id, power_impact_update=power_impact_update)


class SyncPowerImpactApi(_PowerImpactApi):
    def create_power_impact(self, power_impact_create: m.PowerImpactCreate) -> m.PowerImpactResponse:
        """
        Create new power_impact.
        """
        coroutine = self._build_for_create_power_impact(power_impact_create=power_impact_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_power_impact(self, id: str) -> m.PowerImpactResponse:
        """
        Delete a power impact.
        """
        coroutine = self._build_for_delete_power_impact(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_power_impact(self, id: str) -> m.PowerImpactResponse:
        """
        Get power impact by ID.
        """
        coroutine = self._build_for_get_power_impact(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_power_impacts(
        self,
    ) -> m.PowerImpactListResponse:
        """
        Retrieve power impacts.
        """
        coroutine = self._build_for_list_power_impacts()
        return get_event_loop().run_until_complete(coroutine)

    def update_power_impact(self, id: str, power_impact_update: m.PowerImpactUpdate) -> m.PowerImpactResponse:
        """
        Update a power impact.
        """
        coroutine = self._build_for_update_power_impact(id=id, power_impact_update=power_impact_update)
        return get_event_loop().run_until_complete(coroutine)
