from .base import AlfaModel


class Room(AlfaModel):
    id: int | None = None
    branch_id: int | None = None
    location_id: int | None = None
    streaming_id: int | None = None
    color_id: int | None = None
    name: str | None = None
    note: str | None = None
    is_enabled: bool | None = None
    weight: int | None = None
