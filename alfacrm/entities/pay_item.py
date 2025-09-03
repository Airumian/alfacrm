from typing import List, Optional

from .base import AlfaModel


class PayItem(AlfaModel):
    id: Optional[int] = None
    branch_ids: Optional[List[int]] = None
    category_id: Optional[int] = None
    pay_type_ids: Optional[List[int]] = None
    name: Optional[str] = None
    weight: Optional[int] = None
