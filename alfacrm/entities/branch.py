from .base import AlfaModel


class Branch(AlfaModel):
    id: int | None = None
    name: str | None = None
    is_active: bool | None = None
    subject_ids: list[int] | None = None
    weight: int | None = None
