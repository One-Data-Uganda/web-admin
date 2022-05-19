import datetime
import json
import uuid

from app.core.config import settings
from app.core.logger import log
from app.services import FailureResponseModel
from app.services.api.user import models  # noqa
from app.services.api.user.api_client import ApiClient, AsyncApis
from app.services.api.user.exceptions import UnexpectedResponse

client = ApiClient(host=settings.USER_SERVICE, timeout=30)
api = AsyncApis(client)


async def get(id: uuid.UUID):
    try:
        r = await api.kyc_api.get_kyc(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def update(
    id: uuid.UUID,
    msisdn_1: str = None,
    email_1: str = None,
    address_1: str = None,
    country_id: str = None,
    dob: datetime.date = None,
    business_name: str = None,
    tin: str = None,
    first_name: str = None,
    other_names: str = None,
    last_name: str = None,
    gender: str = None,
    email_2: str = None,
    email_3: str = None,
    msisdn_2: str = None,
    msisdn_3: str = None,
):
    data = models.KYCUpdate(
        msisdn_1=msisdn_1,
        msisdn_2=msisdn_2,
        msisdn_3=msisdn_3,
        email_1=email_1,
        email_2=email_2,
        email_3=email_3,
        address_1=address_1,
        country_id=country_id,
        business_name=business_name,
        first_name=first_name,
        other_names=other_names,
        last_name=last_name,
        gender=gender,
        dob=dob,
        tin=tin,
    )
    try:
        r = await api.kyc_api.update_kyc(id, data)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def check_email(email: str):
    try:
        r = await api.kyc_api.get_by_email(email)

        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def check_msisdn(msisdn: str):
    try:
        r = await api.kyc_api.get_by_msisdn(msisdn)

        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def get_document(id: uuid.UUID):
    try:
        r = await api.kyc_document_api.get_kyc_document(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def add_document(kyc_id, name, document_type_id, uploaded_file):
    try:
        r = await api.kyc_document_api.add_kyc_document(
            kyc_id, name, document_type_id, uploaded_file
        )
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def update_document(id, uploaded_file):
    try:
        r = await api.kyc_document_api.update_kyc_document(id, uploaded_file)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")
