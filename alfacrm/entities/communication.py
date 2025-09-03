from pydantic import Field

from .base import AlfaDateTime, AlfaModel


class Communication(AlfaModel):
    id: int | None = None
    type_id: int | None = None
    related_class: str | None = Field(default=None, alias="class")
    related_id: int | None = None
    user_id: int | None = None
    added: AlfaDateTime = None
    comment: str | None = None
