from .base import AlfaModel


class PayAccount(AlfaModel):
    id: int | None = None
    branch_id: int | None = None
    name: str | None = None
    user_ids: list[int] | None = None
    is_enabled: bool | None = None
    weight: int | None = None
