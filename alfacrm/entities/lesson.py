from .base import AlfaDate, AlfaDateTime, AlfaModel


class Lesson(AlfaModel):
    id: int | None = None
    branch_id: int | None = None
    date: AlfaDate = None
    time_from: AlfaDateTime = None
    time_to: AlfaDateTime = None
    lesson_type_id: int | None = None
    status: int | None = None
    subject_id: int | None = None
    room_id: int | None = None
    teacher_ids: list[int] | None = None
    customer_ids: list[int] | None = None
    group_ids: list[int] | None = None
    streaming: bool | list[str] | None = None
    note: str | None = None
