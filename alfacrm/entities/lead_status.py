from typing import Optional

from .base import AlfaModel


class LeadStatus(AlfaModel):
    id: Optional[int] = None
    name: Optional[str] = None
    is_enabled: Optional[bool] = None
    weight: Optional[int] = None
