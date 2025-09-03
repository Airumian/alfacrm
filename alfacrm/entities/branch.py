from typing import List, Optional

from .base import AlfaModel


class Branch(AlfaModel):
    id: Optional[int] = None
    name: Optional[str] = None
    is_active: Optional[bool] = None
    subject_ids: Optional[List[int]] = None
    weight: Optional[int] = None
