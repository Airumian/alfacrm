from pydantic import Field

from .base import AlfaDateTime, AlfaModel


class Tariff(AlfaModel):
    id: int | None = None
    tariff_type: int | None = Field(default=None, alias="type")
    name: str | None = None
    price: float | None = None
    lesson_count: int | None = None
    duration: int | None = None
    added: AlfaDateTime = None
    branch_ids: list[int] | None = None
