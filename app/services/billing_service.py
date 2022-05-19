import datetime
import json
import uuid

from app.core.config import settings
from app.core.logger import log
from app.services import FailureResponseModel
from app.services.api.accounting import models
from app.services.api.accounting.api_client import ApiClient, AsyncApis, SyncApis
from app.services.api.accounting.exceptions import UnexpectedResponse

client = ApiClient(host=settings.ACCOUNTING_SERVICE, timeout=30)
api = AsyncApis(client)
api_sync = SyncApis(client)


async def add(name):
    try:
        r = await api.billing_api.create_billing(
            models.BillingCreate(
                id=name,
            )
        )
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def delete(id):
    try:
        r = await api.billing_api.delete_billing(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def list():
    try:
        r = await api.billing_api.list_billings()
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


async def get(id):
    try:
        r = await api.billing_api.get_billing(id)

        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


async def networks(id):
    try:
        r = await api.billing_api.list_networks_for_billing_id(id)

        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


async def network_add(
    billing_id: str,
    name: str,
    country_id: str,
    prefixes: list,
    network_id: str,
    cost: int,
):
    try:
        body = models.BillingNetworkIn(
            billing_id=billing_id,
            name=name,
            country_id=country_id,
            prefixes=prefixes,
            network_id=network_id,
            cost=cost,
        )
        r = await api.billing_network_api.create_billing_network(body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def network_update(
    id: int,
    billing_id: str,
    name: str,
    country_id: str,
    prefixes: list,
    network_id: str,
    cost: int,
):
    try:
        body = models.BillingNetworkUpdateIn(
            billing_id=billing_id,
            name=name,
            country_id=country_id,
            prefixes=prefixes,
            network_id=network_id,
            cost=cost,
        )
        r = await api.billing_network_api.update_billing_network(id, body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def network_delete(id: int):
    try:
        r = await api.billing_network_api.delete_billing_network(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def network_list():
    try:
        r = await api.billing_network_api.list_billing_networks()
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


async def network_get(id: str):
    try:
        r = await api.billing_network_api.get_billing_network(id)

        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


async def topup_add(
    topdate: datetime.datetime,
    account_id: uuid.UUID,
    credits: int,
    notes: str,
    user_id: uuid.UUID,
):
    try:
        body = models.TopupCreate(
            topup_type_id="business",
            topdate=topdate,
            account_id=account_id,
            credits=credits,
            message=notes,
            user_id=user_id,
            status="successful",
        )

        r = await api.topup_api.create_topup(body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def topup_reverse(id):
    try:
        r = await api.topup.reverse(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def topup_list(params):
    try:
        r = await api.topup.list(params=params)
        log.debug(r)
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


async def topup_get(id):
    try:
        r = await api.topup.retrieve(id)

        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


async def cost(
    msisdn_list: list,
    account_id: uuid.UUID,
    contacts: list,
    message: str,
    sender_id: str,
):
    try:
        body = models.CostCalculateModel(
            msisdn_list=msisdn_list,
            account_id=account_id,
            contacts=contacts,
            message=message,
            sender_id=sender_id,
        )

        r = await api.cost_api.create(body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")
