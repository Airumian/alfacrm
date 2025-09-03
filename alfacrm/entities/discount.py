from typing import List, Optional

from .base import AlfaDate, AlfaModel


class Discount(AlfaModel):
    id: Optional[int] = None
    branch_id: Optional[int] = None
    customer_id: Optional[int] = None
    discount_type: Optional[int] = None
    amount: Optional[int] = None
    note: Optional[str] = None
    subject_ids: Optional[List[int]] = None
    lesson_type_ids: Optional[List[int]] = None
    begin: AlfaDate = None
    end: AlfaDate = None
