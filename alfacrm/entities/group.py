from .base import AlfaDate, AlfaModel


class Group(AlfaModel):
    id: int | None = None
    branch_ids: list[int] | None = None
    teacher_ids: list[int] | None = None
    name: str | None = None
    level_id: int | None = None
    status_id: int | None = None
    company_id: int | None = None
    streaming_id: int | None = None
    limit: int | None = None
    note: str | None = None
    b_date: AlfaDate = None
    e_date: AlfaDate = None
