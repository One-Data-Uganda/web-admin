import datetime
import json
from uuid import UUID

from app.core.config import settings
from app.core.logger import log
from app.services import FailureResponseModel
from app.services.api.accounting import models
from app.services.api.accounting.api_client import ApiClient, AsyncApis, SyncApis
from app.services.api.accounting.exceptions import UnexpectedResponse

client = ApiClient(host=settings.ACCOUNTING_SERVICE, timeout=240)
api = AsyncApis(client)
api_sync = SyncApis(client)


async def billing_add(name):
    try:
        body = models.BillingCreate(
            id=name,
        )

        r = await api.billing_api.create_billing(body)
        return r.body
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def billing_delete(id):
    try:
        r = await api.billing_api.delete_billing(id)
        return r.body
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def billing_list():
    try:
        r = await api.billing_api.list_billings()
        log.debug(r)
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


async def billing_get(id):
    try:
        r = await api.billing_api.get_billing(id)

        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


async def billing_networks(billing_id):
    try:
        r = await api.billing_api.list_networks_for_billing_id(billing_id)

        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


async def networkfloat_add(fdate, network_id, amount, notes, user_id):
    try:
        body = models.NetworkFloatCreate(
            fdate=fdate,
            network_id=network_id,
            amount=amount,
            notes=notes,
            user_id=user_id,
        )

        r = await api.network_float_api.create_network_float(body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def networkfloat_delete(id):
    try:
        r = await api.network_float_api.delete_network_float(id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def networkfloat_list():
    try:
        r = await api.network_float_api.list_network_floats()
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


async def networkfloat_get(id):
    try:
        r = await api.network_float_api.get_network_float(id)

        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return None


async def topup_add(
    account_id: UUID, credits: int, msisdn: str, user_id: UUID, cost: int
):
    try:
        body = models.TopupCreate(
            topup_type_id="self",
            topdate=datetime.datetime.now(),
            account_id=account_id,
            credits=credits,
            msisdn=msisdn,
            user_id=user_id,
            cost=cost,
            status="pending",
        )
        r = await api.topup_api.create_topup(body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def topup_list(account_id: UUID):
    try:
        r = await api.topup_api.list_topups_for_account(account_id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def cost(
    msisdn_list: list, account_id: UUID, contacts: list, message: str, sender_id: str
):
    try:
        body = models.CostCalculateModel(
            msisdn_list=msisdn_list,
            account_id=account_id,
            contacts=contacts,
            message=message,
            sender_id=sender_id,
        )
        r = await api.cost_api.get_costs(body)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


def cost_sync(
    identifier: UUID,
):
    try:
        r = api_sync.cost_api.get_costs_background(identifier)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")


async def get_statement(
    account_id: UUID, from_date: datetime.date, to_date: datetime.date
):
    body = models.StatementModel(
        account_id=account_id, from_date=from_date, to_date=to_date
    )
    try:
        r = await api.statement_api.get_statement(body)
        return r
    except Exception as e:
        log.error(e)
        return None


async def closingBalanceJSON(account_id: UUID, params: dict):
    try:
        r = await api.reports_api.closing_balance_json(account_id, params)
        return r
    except Exception as e:
        log.error(e, exc_info=True)
        return {}


async def task(task_id):
    try:
        r = await api.tasks_api.get_task_state(task_id)
        return r
    except UnexpectedResponse as e:
        x = json.loads(e.content)
        return FailureResponseModel(success=False, message=x["message"])
    except Exception as e:
        log.error(e, exc_info=True)
        return FailureResponseModel(success=False, message="System Error")
