from .base import AlfaModel


class LeadStatus(AlfaModel):
    id: int | None = None
    name: str | None = None
    is_enabled: bool | None = None
    weight: int | None = None
