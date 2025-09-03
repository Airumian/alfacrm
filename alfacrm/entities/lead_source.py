from typing import Optional

from .base import AlfaModel


class LeadSource(AlfaModel):
    id: Optional[int] = None
    code: Optional[str] = None
    name: Optional[str] = None
    is_enabled: Optional[bool] = None
    weight: Optional[int] = None
