from pydantic import Field

from .base import AlfaModel


class LessonType(AlfaModel):
    id: int | None = None
    name: str | None = None
    lesson_type: int | None = Field(default=None, alias="type")
    icon: str | None = None
    is_active: bool | None = None
    sort: int | None = None
