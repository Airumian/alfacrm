from typing import List, Optional

from .base import AlfaDate, AlfaModel


class Group(AlfaModel):
    id: Optional[int] = None
    branch_ids: Optional[List[int]] = None
    teacher_ids: Optional[List[int]] = None
    name: Optional[str] = None
    level_id: Optional[int] = None
    status_id: Optional[int] = None
    company_id: Optional[int] = None
    streaming_id: Optional[int] = None
    limit: Optional[int] = None
    note: Optional[str] = None
    b_date: AlfaDate = None
    e_date: AlfaDate = None
