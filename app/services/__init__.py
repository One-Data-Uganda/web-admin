from pydantic import BaseModel


class FailureResponseModel(BaseModel):
    success: bool
    message: str
