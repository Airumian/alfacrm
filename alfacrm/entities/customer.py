from .base import AlfaDate, AlfaDateTime, AlfaModel


class Customer(AlfaModel):
    id: int | None = None
    name: str | None = None
    branch_ids: list[int] | None = None
    teacher_ids: list[int] | None = None
    is_study: bool | None = None
    study_status_id: int | None = None
    lead_status_id: int | None = None
    lead_reject_id: int | None = None
    lead_source_id: int | None = None
    assigned_id: int | None = None
    legal_type: int | None = None
    legal_name: str | None = None
    company_id: int | None = None
    dob: AlfaDate = None
    balance: float | None = None
    balance_base: float | None = None
    balance_bonus: float | None = None
    last_attend_date: AlfaDate = None
    b_date: AlfaDateTime = None
    e_date: AlfaDate = None
    paid_count: int | None = None
    paid_lesson_count: int | None = None
    paid_lesson_date: AlfaDateTime = None
    next_lesson_date: AlfaDateTime = None
    paid_till: AlfaDateTime = None
    phone: list[str] | None = None
    email: list[str] | None = None
    web: list[str] | None = None
    addr: list[str] | None = None
    note: str | None = None
    color: str | None = None
