from .base import AlfaDateTime, AlfaDict, AlfaModel


class Webhook(AlfaModel):
    branch_id: int
    event: str
    entity: str
    entity_id: int
    fields_old: AlfaDict
    fields_new: AlfaDict
    fields_rel: AlfaDict
    user_id: int
    datetime: AlfaDateTime
