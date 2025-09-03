from .base import AlfaDate, AlfaModel


class Pay(AlfaModel):
    id: int | None = None
    branch_id: int | None = None
    location_id: int | None = None
    customer_id: int | None = None
    pay_type_id: int | None = None
    pay_account_id: int | None = None
    pay_item_id: int | None = None
    teacher_id: int | None = None
    commodity_id: int | None = None
    ctt_id: int | None = None
    document_date: AlfaDate = None
    income: float | None = None
    payer_name: str | None = None
    note: str | None = None
    is_confirmed: bool | None = None
    custom_md_order: str | None = None
    custom_order_description: str | None = None
