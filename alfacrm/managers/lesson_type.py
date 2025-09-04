from typing import Generic, TypeVar

from ..core import EntityManager

T = TypeVar("T")


class LessonType(EntityManager[T], Generic[T]):
    object_name = "lesson-type"
