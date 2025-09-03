from typing import Optional

from .base import AlfaModel


class Location(AlfaModel):
    id: Optional[int] = None
    branch_id: Optional[int] = None
    is_active: Optional[bool] = None
    name: Optional[str] = None
    weight: Optional[int] = None
