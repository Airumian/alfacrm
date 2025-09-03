from .base import AlfaModel


class PayItemCategory(AlfaModel):
    id: int | None = None
    name: str | None = None
    weight: int | None = None
