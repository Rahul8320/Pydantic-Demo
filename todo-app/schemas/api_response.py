from http import HTTPStatus
from typing import Any, Optional
from pydantic import BaseModel


class ApiResponse(BaseModel):
    status: HTTPStatus
    message: str
    data: Optional[Any] = None
