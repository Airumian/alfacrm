from typing import List, Optional

from .base import AlfaDate, AlfaDateTime, AlfaModel


class CustomerTariff(AlfaModel):
    id: Optional[int] = None
    customer_id: Optional[int] = None
    tariff_id: Optional[int] = None
    subject_ids: Optional[List[int]] = None
    lesson_type_ids: Optional[List[int]] = None
    is_separate_balance: Optional[bool] = None
    balance: Optional[float] = None
    paid_count: Optional[int] = None
    paid_till: AlfaDateTime = None
    note: Optional[str] = None
    b_date: AlfaDate = None
    e_date: AlfaDate = None
    paid_lesson_count: Optional[int] = None
