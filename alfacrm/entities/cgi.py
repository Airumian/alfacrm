from .base import AlfaDate, AlfaModel


class CGI(AlfaModel):
    id: int | None = None
    customer_id: int | None = None
    group_id: int | None = None
    b_date: AlfaDate = None
    e_date: AlfaDate = None
