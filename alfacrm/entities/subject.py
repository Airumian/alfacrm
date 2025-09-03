from .base import AlfaModel


class Subject(AlfaModel):
    id: int | None = None
    name: str | None = None
    weight: int | None = None
