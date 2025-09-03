from typing import List, Optional

from .base import AlfaDate, AlfaDateTime, AlfaModel


class Customer(AlfaModel):
    id: Optional[int] = None
    name: Optional[str] = None
    branch_ids: Optional[List[int]] = None
    teacher_ids: Optional[List[int]] = None
    is_study: Optional[bool] = None
    study_status_id: Optional[int] = None
    lead_status_id: Optional[int] = None
    lead_reject_id: Optional[int] = None
    lead_source_id: Optional[int] = None
    assigned_id: Optional[int] = None
    legal_type: Optional[int] = None
    legal_name: Optional[str] = None
    company_id: Optional[int] = None
    dob: AlfaDate = None
    balance: Optional[float] = None
    balance_base: Optional[float] = None
    balance_bonus: Optional[float] = None
    last_attend_date: AlfaDate = None
    b_date: AlfaDateTime = None
    e_date: AlfaDate = None
    paid_count: Optional[int] = None
    paid_lesson_count: Optional[int] = None
    paid_lesson_date: AlfaDateTime = None
    next_lesson_date: AlfaDateTime = None
    paid_till: AlfaDateTime = None
    phone: Optional[List[str]] = None
    email: Optional[List[str]] = None
    web: Optional[List[str]] = None
    addr: Optional[List[str]] = None
    note: Optional[str] = None
    color: Optional[str] = None
