from app.core.logger import log  # noqa
from app.services import (
    account_service,
    admin_group_service,
    document_type_service,
    group_service,
    information_service,
    role_service,
    sector_service,
)


async def countries():
    rows = await information_service.country_list()
    return [("", "", dict(data_calling_code=""))] + [
        (x.id, x.name, dict(data_calling_code=x.calling_code)) for x in rows.data
    ]


async def countries_simple():
    rows = await information_service.country_list()
    return [("", "")] + [(x.id, x.name) for x in rows.data]


async def sector_industries():
    rows = await sector_service.sector_industries()
    return [(x.id, x.name) for x in rows.data]


async def sector_groups():
    rows = await sector_service.sector_groups()
    return [(x.id, x.name) for x in rows.data]


async def sector_divisions():
    rows = await sector_service.sector_divisions()
    return [(x.id, x.name) for x in rows.data]


async def sectors():
    rows = await sector_service.sectors()
    return [(x.id, x.name) for x in rows.data]


async def account_groups(id):
    rows = await group_service.list(id)
    return [(x.id, x.name) for x in rows.data]


async def roles():
    rows = await role_service.list()
    return [(x.id, x.name) for x in rows.data if x.id != "account_admin"]
