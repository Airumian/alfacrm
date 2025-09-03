from typing import Optional

from pydantic import Field

from .base import AlfaDateTime, AlfaModel


class Communication(AlfaModel):
    id: Optional[int] = None
    type_id: Optional[int] = None
    related_class: Optional[str] = Field(default=None, alias="class")
    related_id: Optional[int] = None
    user_id: Optional[int] = None
    added: AlfaDateTime = None
    comment: Optional[str] = None
