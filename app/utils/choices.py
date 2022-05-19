from app import app
from app.services import (
    account_service,
    accounting_service,
    admin_group_service,
    document_type_service,
    group_service,
    information_service,
    keyword_service,
    list_service,
    network_service,
    role_service,
    sender_service,
    shortcode_service,
    template_service,
)


async def countries():
    rows = await information_service.country_list()
    return [("", "", dict(data_calling_code=""))] + [
        (x.id, x.name, dict(data_calling_code=x.calling_code)) for x in rows.data
    ]


async def roles():
    rows = await role_service.list()
    return [(x.id, x.name) for x in rows.data if x.id != "account_admin"]


async def countries_simple():
    rows = await information_service.country_list()
    return [("", "")] + [(x.id, x.name) for x in rows.data]


async def countries_code():
    rows = await information_service.country_list()
    return [("", "- Select -")] + [(x.calling_code, x.name) for x in rows.data]


async def billing_plans():
    rows = await accounting_service.billing_list()
    return [(x.id, x.id) for x in rows.data]


async def topup_types():
    rows = await accounting_service.list_topup_types()
    return [("", "-- Select --")] + [(x.id, x.name) for x in rows.data if x.state == 1]


async def account_groups(id):
    rows = await group_service.list(id)
    return [("", "-- Select --")] + [(x.id, x.name) for x in rows.data]


async def admin_groups():
    rows = await admin_group_service.list()
    return [("", "-- Select --")] + [(x.id, x.name) for x in rows.data]


async def networks():
    rows = await network_service.list()
    return [("", "-- Select --")] + [(x.id, x.name) for x in rows.data]


async def accounts_chained():
    rows = await account_service.list()
    return [("", "-- Select --", {})] + [
        (
            str(x.id),
            x.kyc.business_name
            if x.kyc.is_company
            else f"{x.kyc.first_name} {x.kyc.last_name}",
            dict(data_chained=f"{x.kyc.is_company}"),
        )
        for x in rows.data
    ]


async def accounts():
    rows = await account_service.list()
    return [
        (
            str(x.id),
            x.kyc.business_name
            if x.kyc.is_company
            else f"{x.kyc.first_name} {x.kyc.last_name}",
        )
        for x in rows.data
    ]


async def templates(user_id):
    rows = await template_service.list(user_id)
    return [(0, "-- Select --")] + [(str(x.id), x.name) for x in rows.data]


async def shortcodes():
    rows = await shortcode_service.list()
    return [("", "-- Select --")] + [(x.id, x.id) for x in rows.data]


async def senders(account_id):
    rows = await sender_service.list_for_account(account_id)
    return [(app.config["DEFAULT_SENDER_ID"], app.config["DEFAULT_SENDER_ID"])] + [
        (x.name, x.name) for x in rows
    ]


async def keyword_aliases():
    rows = await keyword_service.list()
    return [("", "-- Select -- ", {})] + [
        (x.id, x.keyword, dict(data_chained=f"{x.account_id}"))
        for x in rows.data
        if x.status == 1
    ]


async def contact_lists():
    rows = await list_service.list()
    return [("", "-- Select --", {})] + [
        (
            x.id,
            f"{x.name} [{x.count_contacts} contacts]",
            dict(data_chained=f"{x.account_id}"),
        )
        for x in rows.data
    ]


async def document_types_company():
    rows = await document_type_service.list()
    return [(x.id, x.name) for x in rows.data if x.is_company]


async def document_types_individual():
    rows = await document_type_service.list()
    return [("", "-- Select --")] + [
        (x.id, x.name) for x in rows.data if not x.is_company
    ]
