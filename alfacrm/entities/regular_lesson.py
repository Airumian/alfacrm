from .base import AlfaDate, AlfaModel, AlfaTime


class RegularLesson(AlfaModel):
    id: int | None = None
    branch_id: int | None = None
    lesson_type_id: int | None = None
    related_class: str | None = None
    related_id: int | None = None
    subject_id: int | None = None
    streaming: bool | None = None
    teacher_ids: list[int] | None = None
    room_id: int | None = None
    day: int | None = None
    days: list[int] | None = None
    time_from_v: AlfaTime = None
    time_to_v: AlfaTime = None
    e_date_v: AlfaDate = None
    b_date_v: AlfaDate = None
    b_date: AlfaDate = None
    e_date: AlfaDate = None
    is_public: bool | None = None
