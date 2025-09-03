from .base import AlfaModel


class StudyStatus(AlfaModel):
    id: int | None = None
    name: str | None = None
    is_enabled: bool | None = None
    weight: int | None = None
