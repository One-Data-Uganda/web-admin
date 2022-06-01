import json
import uuid

from app.core.config import settings
from app.core.logger import log
from app.services import FailureResponseModel
from app.services.api.user import models
from app.services.api.user.api_client import ApiClient, AsyncApis, SyncApis
from app.services.api.user.exceptions import UnexpectedResponse

client = ApiClient(host=settings.USER_SERVICE, timeout=30)
api = AsyncApis(client)
api_sync = SyncApis(client)


async def listAll():
    try:
        r = await api.user_api.list_users()
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(
            success=False, message="Internal Error. Please try again"
        )


async def user_json(account_id: uuid.UUID, params: dict):
    try:
        r = await api.user_api.user_account_json(account_id, params)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(
            success=False, message="Internal Error. Please try again"
        )


async def check_email(email):
    try:
        r = await api.user_api.check_email(models.EmailModel(email=email))
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(
            success=False, message="Internal Error. Please try again"
        )


async def check_msisdn(msisdn):
    try:
        r = await api.user_api.check_msisdn(models.MSISDNModel(msisdn=msisdn))
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(
            success=False, message="Internal Error. Please try again"
        )


async def check_password(password):
    try:
        body = models.PasswordModel(password=password)
        r = await api.user_api.check_password(body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(
            success=False, message="Internal Error. Please try again"
        )


async def login(method, value, password):
    r = None
    try:
        body = models.UserLogin(method=method, value=value, password=password)
        r = await api.user_api.login_user(body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(
            success=False, message="Internal Error. Please try again"
        )


async def add(
    account_id: uuid.UUID,
    account_group_id: int,
    password,
    kyc_id=None,
    first_name=None,
    last_name=None,
    email_1=None,
    dob=None,
    gender=None,
    country_id=None,
    msisdn_1=None,
    msisdn_2=None,
    active=None,
):
    try:
        body = models.UserViewCreate(
            account_id=account_id,
            account_group_id=account_group_id,
            kyc_id=kyc_id,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email_1=email_1,
            dob=dob,
            gender=gender,
            country_id=country_id,
            msisdn_1=msisdn_1,
            msisdn_2=msisdn_2,
            active=active,
        )
        log.debug(body)

        r = await api.user_api.create_user(body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(
            success=False, message="Internal Error. Please try again"
        )


async def add_with_kyc(
    kyc_id: uuid.UUID,
    group_id: int,
    password,
    active=None,
):
    try:
        body = models.UserCreate(
            account_group_id=group_id,
            kyc_id=kyc_id,
            password=password,
            active=active,
        )
        log.debug(body)

        r = await api.user_api.create_user_with_kyc(body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(
            success=False, message="Internal Error. Please try again"
        )


async def update(
    id: uuid.UUID,
    account_id: uuid.UUID = None,
    account_group_id: int = None,
    password: str = None,
    kyc_id=None,
    first_name=None,
    last_name=None,
    email_1=None,
    dob=None,
    gender=None,
    country_id=None,
    msisdn_1=None,
    msisdn_2=None,
    active=None,
):
    try:
        body = models.UserViewUpdate(
            account_id=account_id,
            account_group_id=account_group_id,
            kyc_id=kyc_id,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email_1=email_1,
            dob=dob,
            gender=gender,
            country_id=country_id,
            msisdn_1=msisdn_1,
            msisdn_2=msisdn_2,
            active=active,
        )

        log.debug(f"USER UPDATE: {body}")

        r = await api.user_api.update_user(id, body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(
            success=False, message="Internal Error. Please try again"
        )


async def set_password(id: uuid.UUID, password):
    try:
        r = await api.user_api.update_user(id, models.PasswordModel(password=password))
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(
            success=False, message="Internal Error. Please try again"
        )


async def get(id: uuid.UUID):
    try:
        r = await api.user_api.get_user(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(
            success=False, message="Internal Error. Please try again"
        )


async def get_by_kyc(kyc_id: uuid.UUID):
    try:
        r = await api.user_api.get_user_by_kyc(kyc_id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(
            success=False, message="Internal Error. Please try again"
        )


def get_sync(id: uuid.UUID):
    try:
        r = api_sync.user_api.get_user(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(
            success=False, message="Internal Error. Please try again"
        )


async def delete(id: uuid.UUID):
    try:
        r = await api.user_api.delete_user(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(
            success=False, message="Internal Error. Please try again"
        )


async def disable(id: uuid.UUID):
    try:
        r = await api.user_api.disable_user(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(
            success=False, message="Internal Error. Please try again"
        )


async def enable(id: uuid.UUID):
    try:
        r = await api.user_api.enable_user(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(
            success=False, message="Internal Error. Please try again"
        )
