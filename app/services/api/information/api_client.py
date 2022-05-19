from asyncio import get_event_loop
from json import JSONDecodeError
from typing import Any, Awaitable, Callable, Dict, Generic, Type, TypeVar, overload

from app.services.api.information.api.country_api import AsyncCountryApi, SyncCountryApi
from app.services.api.information.api.country_contact_api import AsyncCountryContactApi, SyncCountryContactApi
from app.services.api.information.api.country_document_api import AsyncCountryDocumentApi, SyncCountryDocumentApi
from app.services.api.information.api.country_sector_api import AsyncCountrySectorApi, SyncCountrySectorApi
from app.services.api.information.api.region_api import AsyncRegionApi, SyncRegionApi
from app.services.api.information.api.sector_api import AsyncSectorApi, SyncSectorApi
from app.services.api.information.api.sector_division_api import AsyncSectorDivisionApi, SyncSectorDivisionApi
from app.services.api.information.api.sector_group_api import AsyncSectorGroupApi, SyncSectorGroupApi
from app.services.api.information.api.sector_industry_api import AsyncSectorIndustryApi, SyncSectorIndustryApi
from app.services.api.information.api.sub_region_api import AsyncSubRegionApi, SyncSubRegionApi
from app.services.api.information.exceptions import ResponseHandlingException, UnexpectedResponse
from httpx import AsyncClient, Request, Response
from pydantic import ValidationError, parse_obj_as

try:
    from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor

    HAVE_OTEL = True
except ImportError:
    HAVE_OTEL = False

ClientT = TypeVar("ClientT", bound="ApiClient")


class AsyncApis(Generic[ClientT]):
    def __init__(self, client: ClientT):
        self.client = client

        self.country_api = AsyncCountryApi(self.client)
        self.country_contact_api = AsyncCountryContactApi(self.client)
        self.country_document_api = AsyncCountryDocumentApi(self.client)
        self.country_sector_api = AsyncCountrySectorApi(self.client)
        self.region_api = AsyncRegionApi(self.client)
        self.sector_api = AsyncSectorApi(self.client)
        self.sector_division_api = AsyncSectorDivisionApi(self.client)
        self.sector_group_api = AsyncSectorGroupApi(self.client)
        self.sector_industry_api = AsyncSectorIndustryApi(self.client)
        self.sub_region_api = AsyncSubRegionApi(self.client)


class SyncApis(Generic[ClientT]):
    def __init__(self, client: ClientT):
        self.client = client

        self.country_api = SyncCountryApi(self.client)
        self.country_contact_api = SyncCountryContactApi(self.client)
        self.country_document_api = SyncCountryDocumentApi(self.client)
        self.country_sector_api = SyncCountrySectorApi(self.client)
        self.region_api = SyncRegionApi(self.client)
        self.sector_api = SyncSectorApi(self.client)
        self.sector_division_api = SyncSectorDivisionApi(self.client)
        self.sector_group_api = SyncSectorGroupApi(self.client)
        self.sector_industry_api = SyncSectorIndustryApi(self.client)
        self.sub_region_api = SyncSubRegionApi(self.client)


T = TypeVar("T")
Send = Callable[[Request], Awaitable[Response]]
MiddlewareT = Callable[[Request, Send], Awaitable[Response]]


class ApiClient:
    def __init__(self, host: str = None, **kwargs: Any) -> None:
        self.host = host
        self.middleware: MiddlewareT = BaseMiddleware()
        self._async_client = AsyncClient(**kwargs)
        if HAVE_OTEL:
            HTTPXClientInstrumentor.instrument_client(self._async_client)

    @overload
    async def request(
        self, *, type_: Type[T], method: str, url: str, path_params: Dict[str, Any] = None, **kwargs: Any
    ) -> T:
        ...

    @overload  # noqa F811
    async def request(
        self, *, type_: None, method: str, url: str, path_params: Dict[str, Any] = None, **kwargs: Any
    ) -> None:
        ...

    async def request(  # noqa F811
        self, *, type_: Any, method: str, url: str, path_params: Dict[str, Any] = None, **kwargs: Any
    ) -> Any:
        if path_params is None:
            path_params = {}
        url = (self.host or "") + url.format(**path_params)
        request = Request(method, url, **kwargs)
        return await self.send(request, type_)

    @overload
    def request_sync(self, *, type_: Type[T], **kwargs: Any) -> T:
        ...

    @overload  # noqa F811
    def request_sync(self, *, type_: None, **kwargs: Any) -> None:
        ...

    def request_sync(self, *, type_: Any, **kwargs: Any) -> Any:  # noqa F811
        """
        This method is not used by the generated apis, but is included for convenience
        """
        return get_event_loop().run_until_complete(self.request(type_=type_, **kwargs))

    async def send(self, request: Request, type_: Type[T]) -> T:
        response = await self.middleware(request, self.send_inner)
        if response.status_code in [200, 201]:
            try:
                return parse_obj_as(type_, response.json())
            except ValidationError as e:
                raise ResponseHandlingException(e)
            except JSONDecodeError:
                return response
        raise UnexpectedResponse.for_response(response)

    async def send_inner(self, request: Request) -> Response:
        try:
            response = await self._async_client.send(request)
        except Exception as e:
            raise ResponseHandlingException(e)
        return response

    def add_middleware(self, middleware: MiddlewareT) -> None:
        current_middleware = self.middleware

        async def new_middleware(request: Request, call_next: Send) -> Response:
            async def inner_send(request: Request) -> Response:
                return await current_middleware(request, call_next)

            return await middleware(request, inner_send)

        self.middleware = new_middleware


class BaseMiddleware:
    async def __call__(self, request: Request, call_next: Send) -> Response:
        return await call_next(request)
