from typing import Generic, TypeVar

from ..core import EntityManager

T = TypeVar("T")


class RegularLesson(EntityManager[T], Generic[T]):
    object_name = "regular-lesson"
