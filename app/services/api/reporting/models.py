from datetime import date
from typing import Any  # noqa
from uuid import UUID

from pydantic import BaseModel, Field


class FailureResponseModel(BaseModel):
    success: "bool" = Field(..., alias="success")
    message: "str" = Field(..., alias="message")


class StatementModel(BaseModel):
    account_id: "UUID" = Field(..., alias="account_id")
    account_name: "str" = Field(..., alias="account_name")
    from_date: "date" = Field(..., alias="from_date")
    to_date: "date" = Field(..., alias="to_date")
    email: "str" = Field(..., alias="email")
