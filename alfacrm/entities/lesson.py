from typing import List, Optional

from .base import AlfaDate, AlfaDateTime, AlfaModel


class Lesson(AlfaModel):
    id: Optional[int] = None
    branch_id: Optional[int] = None
    date: AlfaDate = None
    time_from: AlfaDateTime = None
    time_to: AlfaDateTime = None
    lesson_type_id: Optional[int] = None
    status: Optional[int] = None
    subject_id: Optional[int] = None
    room_id: Optional[int] = None
    teacher_ids: Optional[List[int]] = None
    customer_ids: Optional[List[int]] = None
    group_ids: Optional[List[int]] = None
    streaming: Optional[bool] = None
    note: Optional[str] = None
