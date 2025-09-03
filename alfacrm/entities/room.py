from typing import Optional

from .base import AlfaModel


class Room(AlfaModel):
    id: Optional[int] = None
    branch_id: Optional[int] = None
    location_id: Optional[int] = None
    streaming_id: Optional[int] = None
    color_id: Optional[int] = None
    name: Optional[str] = None
    note: Optional[str] = None
    is_enabled: Optional[bool] = None
    weight: Optional[int] = None
