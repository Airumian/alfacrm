from .base import AlfaModel


class PayItem(AlfaModel):
    id: int | None = None
    branch_ids: list[int] | None = None
    category_id: int | None = None
    pay_type_ids: list[int] | None = None
    name: str | None = None
    weight: int | None = None
