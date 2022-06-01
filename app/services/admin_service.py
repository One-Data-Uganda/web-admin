import datetime
import json
import uuid

import httpx

from app.core.config import settings
from app.core.logger import log
from app.services import FailureResponseModel
from app.services.api.user import models
from app.services.api.user.api_client import ApiClient, AsyncApis, SyncApis
from app.services.api.user.exceptions import UnexpectedResponse

client = ApiClient(host=settings.USER_SERVICE, timeout=30)
api = AsyncApis(client)
api_sync = SyncApis(client)


async def find(username, email):
    try:
        r = await api.admin_api.find(body={"username": username, "email": email})
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(
            success=False, message="Internal Error. Please try again"
        )


async def admin_json(params: dict):
    try:
        r = await api.admin_api.admin_json(params)
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return {}


async def check_username(username):
    try:
        r = await api.admin_api.check_username(body={"username": username})
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
        r = await api.admin_api.check_password(body)
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
        body = models.MSISDNModel(msisdn=msisdn)
        r = await api.admin_api.check_admin_msisdn(body)
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
        body = models.EmailModel(email=email)
        r = await api.admin_api.check_admin_email(body)
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
        body = models.AdminLogin(method=method, value=value, password=password)
        r = await api.admin_api.login_admin(body)
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
    first_name: str,
    last_name: str,
    gender: str,
    dob: datetime.date,
    country_id: str,
    msisdn: str,
    email: str,
    password: str,
    admin_group_id: int,
    document_type_id: int = None,
    document_id_no: str = None,
):
    try:
        body = models.AdminCreate(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            dob=dob,
            country_id=country_id,
            msisdn=msisdn,
            email=email,
            document_type_id=document_type_id,
            document_id_no=document_id_no,
            admin_group_id=admin_group_id,
            password=password,
            active=False,
        )

        r = await api.admin_api.create_admin(body)
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
    first_name: str,
    last_name: str,
    gender: str,
    dob: datetime.date,
    msisdn: str,
    email: str,
    admin_group_id: int = None,
    country_id: str = None,
    active: bool = None,
    password: str = None,
    document_type_id: int = None,
    document_id_no: str = None,
):
    try:
        body = models.AdminUpdate(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            dob=dob,
            country_id=country_id,
            msisdn=msisdn,
            email=email,
            document_type_id=document_type_id,
            document_id_no=document_id_no,
            admin_group_id=admin_group_id,
            password=password,
            active=active,
        )

        r = await api.admin_api.update_admin(id, body)
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
        r = await api.admin_api.update_admin(id, {"password": password})
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
        r = await api.admin_api.get_admin(id)
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
        with httpx.Client() as client:
            r = client.get(f"{settings.USER_SERVICE}/v1/admin/{id}")
        return r.json()
    except Exception as e:
        log.error(e, exc_info=True)
        return {"success": False, "message": "Internal Error. Please try again"}


async def delete(id: uuid.UUID):
    try:
        r = await api.admin_api.delete_admin(id)
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
        r = await api.admin_api.disable_admin(id)
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
        r = await api.admin_api.enable(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(
            success=False, message="Internal Error. Please try again"
        )
