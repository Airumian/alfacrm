from .base import AlfaDate, AlfaDateTime, AlfaModel


class CustomerTariff(AlfaModel):
    id: int | None = None
    customer_id: int | None = None
    tariff_id: int | None = None
    subject_ids: list[int] | None = None
    lesson_type_ids: list[int] | None = None
    is_separate_balance: bool | None = None
    balance: float | None = None
    paid_count: int | None = None
    paid_till: AlfaDateTime = None
    note: str | None = None
    b_date: AlfaDate = None
    e_date: AlfaDate = None
    paid_lesson_count: int | None = None
