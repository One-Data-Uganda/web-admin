# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable, List

from app.services.api.information import models as m
from fastapi.encoders import jsonable_encoder

if TYPE_CHECKING:
    from app.services.api.information.api_client import ApiClient


class _SubRegionApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_create_sub_region(self, sub_region_create: m.SubRegionCreate) -> Awaitable[m.SubRegion]:
        """
        Create new sub_region.
        """
        body = jsonable_encoder(sub_region_create)

        return self.api_client.request(type_=m.SubRegion, method="POST", url="/v1/sub-region/", json=body)

    def _build_for_delete_sub_region(self, id: str) -> Awaitable[m.SubRegion]:
        """
        Delete an sub_region.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.SubRegion,
            method="DELETE",
            url="/v1/sub-region/{id}",
            path_params=path_params,
        )

    def _build_for_get_sub_region(self, id: str) -> Awaitable[m.SubRegion]:
        """
        Get sub_region by ID.
        """
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=m.SubRegion,
            method="GET",
            url="/v1/sub-region/{id}",
            path_params=path_params,
        )

    def _build_for_list_sub_regions(
        self,
    ) -> Awaitable[List[m.SubRegion]]:
        """
        Retrieve sub_regions.
        """
        return self.api_client.request(
            type_=List[m.SubRegion],
            method="GET",
            url="/v1/sub-region/",
        )

    def _build_for_update_sub_region(self, id: str, sub_region_update: m.SubRegionUpdate) -> Awaitable[m.SubRegion]:
        """
        Update a sub_region.
        """
        path_params = {"id": str(id)}

        body = jsonable_encoder(sub_region_update)

        return self.api_client.request(
            type_=m.SubRegion, method="PUT", url="/v1/sub-region/{id}", path_params=path_params, json=body
        )


class AsyncSubRegionApi(_SubRegionApi):
    async def create_sub_region(self, sub_region_create: m.SubRegionCreate) -> m.SubRegion:
        """
        Create new sub_region.
        """
        return await self._build_for_create_sub_region(sub_region_create=sub_region_create)

    async def delete_sub_region(self, id: str) -> m.SubRegion:
        """
        Delete an sub_region.
        """
        return await self._build_for_delete_sub_region(id=id)

    async def get_sub_region(self, id: str) -> m.SubRegion:
        """
        Get sub_region by ID.
        """
        return await self._build_for_get_sub_region(id=id)

    async def list_sub_regions(
        self,
    ) -> List[m.SubRegion]:
        """
        Retrieve sub_regions.
        """
        return await self._build_for_list_sub_regions()

    async def update_sub_region(self, id: str, sub_region_update: m.SubRegionUpdate) -> m.SubRegion:
        """
        Update a sub_region.
        """
        return await self._build_for_update_sub_region(id=id, sub_region_update=sub_region_update)


class SyncSubRegionApi(_SubRegionApi):
    def create_sub_region(self, sub_region_create: m.SubRegionCreate) -> m.SubRegion:
        """
        Create new sub_region.
        """
        coroutine = self._build_for_create_sub_region(sub_region_create=sub_region_create)
        return get_event_loop().run_until_complete(coroutine)

    def delete_sub_region(self, id: str) -> m.SubRegion:
        """
        Delete an sub_region.
        """
        coroutine = self._build_for_delete_sub_region(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def get_sub_region(self, id: str) -> m.SubRegion:
        """
        Get sub_region by ID.
        """
        coroutine = self._build_for_get_sub_region(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def list_sub_regions(
        self,
    ) -> List[m.SubRegion]:
        """
        Retrieve sub_regions.
        """
        coroutine = self._build_for_list_sub_regions()
        return get_event_loop().run_until_complete(coroutine)

    def update_sub_region(self, id: str, sub_region_update: m.SubRegionUpdate) -> m.SubRegion:
        """
        Update a sub_region.
        """
        coroutine = self._build_for_update_sub_region(id=id, sub_region_update=sub_region_update)
        return get_event_loop().run_until_complete(coroutine)
