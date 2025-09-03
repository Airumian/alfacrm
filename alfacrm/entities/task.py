from typing import List, Optional

from .base import AlfaDate, AlfaDateTime, AlfaModel


class Task(AlfaModel):
    id: Optional[int] = None
    company_id: Optional[int] = None
    branch_ids: Optional[List[int]] = None
    user_id: Optional[int] = None
    assigned_ids: Optional[List[int]] = None
    group_ids: Optional[List[int]] = None
    customer_ids: Optional[List[int]] = None
    title: Optional[str] = None
    text: Optional[str] = None
    is_archive: Optional[bool] = None
    created_at: AlfaDateTime = None
    is_done: Optional[bool] = None
    is_private: Optional[bool] = None
    due_date: AlfaDate = None
    done_date: AlfaDateTime = None
    is_public_entry: Optional[bool] = None
    is_notify: Optional[bool] = None
    priority: Optional[int] = None
