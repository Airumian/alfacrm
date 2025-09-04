from typing import Generic, TypeVar

from ..core.entity_manager import EntityManager

T = TypeVar("T")


class Group(EntityManager[T], Generic[T]):
    object_name = "group"
