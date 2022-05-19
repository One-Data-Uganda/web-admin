import json
import uuid

from app.core.config import settings
from app.core.logger import log
from app.services import FailureResponseModel
from app.services.api.project import models
from app.services.api.project.api_client import ApiClient, AsyncApis, SyncApis
from app.services.api.project.exceptions import UnexpectedResponse

client = ApiClient(host=settings.PROJECT_SERVICE, timeout=30)
api = AsyncApis(client)
api_sync = SyncApis(client)


async def auditJSON(project_id: uuid.UUID, params: dict):
    try:
        r = await api.audit_api.project_audit_json(project_id, params)
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return {}


async def add(
    country_id,
    msisdn_1,
    email_1,
    address,
    is_company,
    active,
    business_name=None,
    short_name=None,
    website=None,
    first_name=None,
    last_name=None,
):
    try:
        body = models.ProjectViewCreate(
            business_name=business_name,
            short_name=short_name,
            country_id=country_id,
            msisdn_1=msisdn_1,
            email_1=email_1,
            address=address,
            is_company=is_company,
            billing_id=billing_id,
            website=website,
            active=active,
            first_name=first_name,
            last_name=last_name,
        )
        r = await api.project_api.create_project(body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def update(
    id,
    dob,
    tin,
    queue,
    country_id,
    msisdn_1,
    email_1,
    address_1,
    is_company,
    billing_id,
    active,
    warning_level=None,
    warning_email=None,
    business_name=None,
    gender=None,
    first_name=None,
    last_name=None,
):
    try:
        body = models.ProjectViewUpdate(
            business_name=business_name,
            dob=dob,
            tin=tin,
            queue=queue,
            country_id=country_id,
            msisdn_1=msisdn_1,
            email_1=email_1,
            address_1=address_1,
            is_company=is_company,
            billing_id=billing_id,
            gender=gender,
            active=active,
            warning_level=warning_level,
            warning_email=warning_email,
            first_name=first_name,
            last_name=last_name,
        )

        log.debug(f"PROJECT UPDATE: {body}")

        r = await api.project_api.update_project(id, body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def enable(id):
    try:
        r = await api.project_api.enable_project(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def disable(id):
    try:
        r = await api.project_api.disable_project(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def get(id):
    try:
        r = await api.project_api.get_project(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def list():
    try:
        r = await api.project_api.list_projects()
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def delete(id):
    try:
        r = await api.project_api.delete_project(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def search(params):
    try:
        r = await api.project_api.search_projects(params)

        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return {}


async def search_individual(params):
    try:
        r = await api.project_api.search_individual(params)

        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return {}


async def check_business_name(name):
    try:
        r = await api.kyc_api.get_by_business_name(name)

        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def add(
    country_id,
    msisdn_1,
    email_1,
    address,
    is_company,
    active,
    business_name=None,
    short_name=None,
    website=None,
    first_name=None,
    last_name=None,
):
    try:
        body = models.ProjectViewCreate(
            country_id=country_id,
            msisdn_1=msisdn_1,
            email_1=email_1,
            address=address,
            is_company=is_company,
            active=active,
            business_name=business_name,
            short_name=short_name,
            website=website,
            first_name=first_name,
            last_name=last_name,
        )
        r = await api.project_api.create_project(body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def add_contact(
    project_id,
    msisdn_1,
    email_1,
    address,
    first_name,
    last_name,
    position,
    country_id,
    website,
):
    try:
        body = models.KYCCreate(
            country_id=country_id,
            msisdn_1=msisdn_1,
            email_1=email_1,
            address=address,
            is_company=False,
            active=active,
            first_name=first_name,
            last_name=last_name,
            website=website,
        )

        r = await api.kyc_api.create_kyc(body)

        body = models.ContactPersonCreate(
            project_id=project_id,
            kyc_id=r.data.id,
            position=position
        )

        r = await api.project_api.add_contact_person(body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def add_countries(
    obj_in: dict
):
    try:
        r = await api.project_api.add_countries(obj_in)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def add_industries(
    obj_in: dict
):
    try:
        r = await api.project_api.add_industries(obj_in)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")
