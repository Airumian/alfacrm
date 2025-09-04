from typing import Generic, TypeVar

from ..core import EntityManager

T = TypeVar("T")


class Task(EntityManager[T], Generic[T]):
    object_name = "task"
