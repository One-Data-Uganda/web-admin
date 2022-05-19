# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from app.services.api.project import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.project.api_client import ApiClient


class _PowerApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_power(self, power_create: m.PowerCreate) -> Awaitable[m.PowerResponse]:
        """
        Create new power.
        """
        body = jsonable_encoder(power_create)

        return self.api_client.request(type_=m.PowerResponse, method="POST", url="/v1/power/", json=body)

    def _build_for_delete_power(self, id: str) -> Awaitable[m.PowerResponse]:
        """
        Delete a power.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.PowerResponse,
            method="DELETE",
            url="/v1/power/{id}",
            path_params=path_params,
        )

    def _build_for_get_power(self, id: str) -> Awaitable[m.PowerResponse]:
        """
        Get power by ID.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.PowerResponse,
            method="GET",
            url="/v1/power/{id}",
            path_params=path_params,
        )

    def _build_for_list_powers(
        self,
    ) -> Awaitable[m.PowerListResponse]:
        """
        Retrieve powers.
        """
        return self.api_client.request(
            type_=m.PowerListResponse,
            method="GET",
            url="/v1/power/",
        )

    def _build_for_update_power(self, id: str, power_update: m.PowerUpdate) -> Awaitable[m.PowerResponse]:
        """
        Update a power.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(power_update)

        return self.api_client.request(
            type_=m.PowerResponse, method="PUT", url="/v1/power/{id}", path_params=path_params, json=body
        )


class AsyncPowerApi(_PowerApi):
    async def create_power(self, power_create: m.PowerCreate) -> m.PowerResponse:
        """
        Create new power.
        """
        return await self._build_for_create_power(power_create=power_create)

    async def delete_power(self, id: str) -> m.PowerResponse:
        """
        Delete a power.
        """
        return await self._build_for_delete_power(id=id)

    async def get_power(self, id: str) -> m.PowerResponse:
        """
        Get power by ID.
        """
        return await self._build_for_get_power(id=id)

    async def list_powers(
        self,
    ) -> m.PowerListResponse:
        """
        Retrieve powers.
        """
        return await self._build_for_list_powers()

    async def update_power(self, id: str, power_update: m.PowerUpdate) -> m.PowerResponse:
        """
        Update a power.
        """
        return await self._build_for_update_power(id=id, power_update=power_update)


class SyncPowerApi(_PowerApi):
    def create_power(self, power_create: m.PowerCreate) -> m.PowerResponse:
        """
        Create new power.
        """
        coroutine = self._build_for_create_power(power_create=power_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_power(self, id: str) -> m.PowerResponse:
        """
        Delete a power.
        """
        coroutine = self._build_for_delete_power(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_power(self, id: str) -> m.PowerResponse:
        """
        Get power by ID.
        """
        coroutine = self._build_for_get_power(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_powers(
        self,
    ) -> m.PowerListResponse:
        """
        Retrieve powers.
        """
        coroutine = self._build_for_list_powers()
        return get_event_loop().run_until_complete(coroutine)

    def update_power(self, id: str, power_update: m.PowerUpdate) -> m.PowerResponse:
        """
        Update a power.
        """
        coroutine = self._build_for_update_power(id=id, power_update=power_update)
        return get_event_loop().run_until_complete(coroutine)
