from asyncio import get_event_loop
from json import JSONDecodeError
from typing import Any, Awaitable, Callable, Dict, Generic, Type, TypeVar, overload

from app.services.api.user.api.account_api import AsyncAccountApi, SyncAccountApi
from app.services.api.user.api.account_country_api import AsyncAccountCountryApi, SyncAccountCountryApi
from app.services.api.user.api.account_industry_api import AsyncAccountIndustryApi, SyncAccountIndustryApi
from app.services.api.user.api.admin_api import AsyncAdminApi, SyncAdminApi
from app.services.api.user.api.admin_group_api import AsyncAdminGroupApi, SyncAdminGroupApi
from app.services.api.user.api.api_api import AsyncApiApi, SyncApiApi
from app.services.api.user.api.audit_api import AsyncAuditApi, SyncAuditApi
from app.services.api.user.api.contact_person_api import AsyncContactPersonApi, SyncContactPersonApi
from app.services.api.user.api.country_api import AsyncCountryApi, SyncCountryApi
from app.services.api.user.api.document_type_api import AsyncDocumentTypeApi, SyncDocumentTypeApi
from app.services.api.user.api.group_api import AsyncGroupApi, SyncGroupApi
from app.services.api.user.api.kyc_api import AsyncKycApi, SyncKycApi
from app.services.api.user.api.role_api import AsyncRoleApi, SyncRoleApi
from app.services.api.user.api.user_api import AsyncUserApi, SyncUserApi
from app.services.api.user.api.user_preference_api import AsyncUserPreferenceApi, SyncUserPreferenceApi
from app.services.api.user.exceptions import ResponseHandlingException, UnexpectedResponse
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

        self.account_api = AsyncAccountApi(self.client)
        self.account_country_api = AsyncAccountCountryApi(self.client)
        self.account_industry_api = AsyncAccountIndustryApi(self.client)
        self.admin_api = AsyncAdminApi(self.client)
        self.admin_group_api = AsyncAdminGroupApi(self.client)
        self.api_api = AsyncApiApi(self.client)
        self.audit_api = AsyncAuditApi(self.client)
        self.contact_person_api = AsyncContactPersonApi(self.client)
        self.country_api = AsyncCountryApi(self.client)
        self.document_type_api = AsyncDocumentTypeApi(self.client)
        self.group_api = AsyncGroupApi(self.client)
        self.kyc_api = AsyncKycApi(self.client)
        self.role_api = AsyncRoleApi(self.client)
        self.user_api = AsyncUserApi(self.client)
        self.user_preference_api = AsyncUserPreferenceApi(self.client)


class SyncApis(Generic[ClientT]):
    def __init__(self, client: ClientT):
        self.client = client

        self.account_api = SyncAccountApi(self.client)
        self.account_country_api = SyncAccountCountryApi(self.client)
        self.account_industry_api = SyncAccountIndustryApi(self.client)
        self.admin_api = SyncAdminApi(self.client)
        self.admin_group_api = SyncAdminGroupApi(self.client)
        self.api_api = SyncApiApi(self.client)
        self.audit_api = SyncAuditApi(self.client)
        self.contact_person_api = SyncContactPersonApi(self.client)
        self.country_api = SyncCountryApi(self.client)
        self.document_type_api = SyncDocumentTypeApi(self.client)
        self.group_api = SyncGroupApi(self.client)
        self.kyc_api = SyncKycApi(self.client)
        self.role_api = SyncRoleApi(self.client)
        self.user_api = SyncUserApi(self.client)
        self.user_preference_api = SyncUserPreferenceApi(self.client)


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
