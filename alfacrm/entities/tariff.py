from typing import List, Optional

from pydantic import Field

from .base import AlfaDateTime, AlfaModel


class Tariff(AlfaModel):
    id: Optional[int] = None
    tariff_type: Optional[int] = Field(default=None, alias="type")
    name: Optional[str] = None
    price: Optional[float] = None
    lesson_count: Optional[int] = None
    duration: Optional[int] = None
    added: AlfaDateTime = None
    branch_ids: Optional[List[int]] = None
