from .base import AlfaModel


class Location(AlfaModel):
    id: int | None = None
    branch_id: int | None = None
    is_active: bool | None = None
    name: str | None = None
    weight: int | None = None
