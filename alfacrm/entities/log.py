from typing import Any, Dict, Optional

from .base import AlfaDateTime, AlfaModel, AlfaDict


class Log(AlfaModel):
    id: Optional[int] = None
    entity: str
    entity_id: int
    user_id: int
    event: int
    fields_old: AlfaDict
    fields_new: AlfaDict
    fields_rel: AlfaDict
    date_time: AlfaDateTime
