from typing import Optional

from pydantic import Field

from .base import AlfaModel


class LessonType(AlfaModel):
    id: Optional[int] = None
    name: Optional[str] = None
    lesson_type: Optional[int] = Field(default=None, alias="type")
    icon: Optional[str] = None
    is_active: Optional[bool] = None
    sort: Optional[int] = None
