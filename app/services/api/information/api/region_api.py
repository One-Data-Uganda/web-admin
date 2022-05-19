# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable, List

from app.services.api.information import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.information.api_client import ApiClient


class _RegionApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_region(self, region_create: m.RegionCreate) -> Awaitable[m.Region]:
        """
        Create new region.
        """
        body = jsonable_encoder(region_create)

        return self.api_client.request(type_=m.Region, method="POST", url="/v1/region/", json=body)

    def _build_for_delete_region(self, id: str) -> Awaitable[m.Region]:
        """
        Delete an region.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.Region,
            method="DELETE",
            url="/v1/region/{id}",
            path_params=path_params,
        )

    def _build_for_get_region(self, id: str) -> Awaitable[m.Region]:
        """
        Get region by ID.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.Region,
            method="GET",
            url="/v1/region/{id}",
            path_params=path_params,
        )

    def _build_for_list_regions(
        self,
    ) -> Awaitable[List[m.Region]]:
        """
        Retrieve countries.
        """
        return self.api_client.request(
            type_=List[m.Region],
            method="GET",
            url="/v1/region/",
        )

    def _build_for_update_region(self, id: str, region_update: m.RegionUpdate) -> Awaitable[m.Region]:
        """
        Update a region.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(region_update)

        return self.api_client.request(
            type_=m.Region, method="PUT", url="/v1/region/{id}", path_params=path_params, json=body
        )


class AsyncRegionApi(_RegionApi):
    async def create_region(self, region_create: m.RegionCreate) -> m.Region:
        """
        Create new region.
        """
        return await self._build_for_create_region(region_create=region_create)

    async def delete_region(self, id: str) -> m.Region:
        """
        Delete an region.
        """
        return await self._build_for_delete_region(id=id)

    async def get_region(self, id: str) -> m.Region:
        """
        Get region by ID.
        """
        return await self._build_for_get_region(id=id)

    async def list_regions(
        self,
    ) -> List[m.Region]:
        """
        Retrieve countries.
        """
        return await self._build_for_list_regions()

    async def update_region(self, id: str, region_update: m.RegionUpdate) -> m.Region:
        """
        Update a region.
        """
        return await self._build_for_update_region(id=id, region_update=region_update)


class SyncRegionApi(_RegionApi):
    def create_region(self, region_create: m.RegionCreate) -> m.Region:
        """
        Create new region.
        """
        coroutine = self._build_for_create_region(region_create=region_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_region(self, id: str) -> m.Region:
        """
        Delete an region.
        """
        coroutine = self._build_for_delete_region(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_region(self, id: str) -> m.Region:
        """
        Get region by ID.
        """
        coroutine = self._build_for_get_region(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_regions(
        self,
    ) -> List[m.Region]:
        """
        Retrieve countries.
        """
        coroutine = self._build_for_list_regions()
        return get_event_loop().run_until_complete(coroutine)

    def update_region(self, id: str, region_update: m.RegionUpdate) -> m.Region:
        """
        Update a region.
        """
        coroutine = self._build_for_update_region(id=id, region_update=region_update)
        return get_event_loop().run_until_complete(coroutine)
