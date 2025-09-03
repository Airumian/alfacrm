from typing import Optional

from .base import AlfaDate, AlfaModel


class CGI(AlfaModel):
    id: Optional[int] = None
    customer_id: Optional[int] = None
    group_id: Optional[int] = None
    b_date: AlfaDate = None
    e_date: AlfaDate = None
