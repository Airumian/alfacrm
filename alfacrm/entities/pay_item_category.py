from typing import Optional

from .base import AlfaModel


class PayItemCategory(AlfaModel):
    id: Optional[int] = None
    name: Optional[str] = None
    weight: Optional[int] = None
