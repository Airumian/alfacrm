import datetime
from typing import Optional

from .base import AlfaDate, AlfaModel


class Pay(AlfaModel):
    id: Optional[int] = None
    branch_id: Optional[int] = None
    location_id: Optional[int] = None
    customer_id: Optional[int] = None
    pay_type_id: Optional[int] = None
    pay_account_id: Optional[int] = None
    pay_item_id: Optional[int] = None
    teacher_id: Optional[int] = None
    commodity_id: Optional[int] = None
    ctt_id: Optional[int] = None
    document_date: AlfaDate = None
    income: Optional[float] = None
    payer_name: Optional[str] = None
    note: Optional[str] = None
    is_confirmed: Optional[bool] = None
    custom_md_order: Optional[str] = None
    custom_order_description: Optional[str] = None
