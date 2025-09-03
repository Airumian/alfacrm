from .base import AlfaDate, AlfaDateTime, AlfaModel


class Task(AlfaModel):
    id: int | None = None
    company_id: int | None = None
    branch_ids: list[int] | None = None
    user_id: int | None = None
    assigned_ids: list[int] | None = None
    group_ids: list[int] | None = None
    customer_ids: list[int] | None = None
    title: str | None = None
    text: str | None = None
    is_archive: bool | None = None
    created_at: AlfaDateTime = None
    is_done: bool | None = None
    is_private: bool | None = None
    due_date: AlfaDate = None
    done_date: AlfaDateTime = None
    is_public_entry: bool | None = None
    is_notify: bool | None = None
    priority: int | None = None
