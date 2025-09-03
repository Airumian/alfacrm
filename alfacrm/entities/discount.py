from .base import AlfaDate, AlfaModel


class Discount(AlfaModel):
    id: int | None = None
    branch_id: int | None = None
    customer_id: int | None = None
    discount_type: int | None = None
    amount: int | None = None
    note: str | None = None
    subject_ids: list[int] | None = None
    lesson_type_ids: list[int] | None = None
    begin: AlfaDate = None
    end: AlfaDate = None
