from typing import Optional

from .base import AlfaModel


class StudyStatus(AlfaModel):
    id: Optional[int] = None
    name: Optional[str] = None
    is_enabled: Optional[bool] = None
    weight: Optional[int] = None
