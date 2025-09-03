from .base import AlfaModel


class LeadSource(AlfaModel):
    id: int | None = None
    code: str | None = None
    name: str | None = None
    is_enabled: bool | None = None
    weight: int | None = None
