from .base import AlfaDateTime, AlfaDict, AlfaModel


class Log(AlfaModel):
    id: int | None = None
    entity: str
    entity_id: int
    user_id: int
    event: int
    fields_old: AlfaDict
    fields_new: AlfaDict
    fields_rel: AlfaDict
    date_time: AlfaDateTime
