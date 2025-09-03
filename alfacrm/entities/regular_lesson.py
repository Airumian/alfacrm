from typing import List, Optional

from .base import AlfaDate, AlfaModel, AlfaTime


class RegularLesson(AlfaModel):
    id: Optional[int] = None
    branch_id: Optional[int] = None
    lesson_type_id: Optional[int] = None
    related_class: Optional[str] = None
    related_id: Optional[int] = None
    subject_id: Optional[int] = None
    streaming: Optional[bool] = None
    teacher_ids: Optional[List[int]] = None
    room_id: Optional[int] = None
    day: Optional[int] = None
    days: Optional[List[int]] = None
    time_from_v: AlfaTime = None
    time_to_v: AlfaTime = None
    e_date_v: AlfaDate = None
    b_date_v: AlfaDate = None
    b_date: AlfaDate = None
    e_date: AlfaDate = None
    is_public: Optional[bool] = None
