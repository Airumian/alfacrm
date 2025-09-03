from typing import List, Optional

from .base import AlfaModel


class PayAccount(AlfaModel):
    id: Optional[int] = None
    branch_id: Optional[int] = None
    name: Optional[str] = None
    user_ids: Optional[List[int]] = None
    is_enabled: Optional[bool] = None
    weight: Optional[int] = None
