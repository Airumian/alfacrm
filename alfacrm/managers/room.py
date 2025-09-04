from typing import Generic, TypeVar

from ..core import EntityManager

T = TypeVar("T")


class Room(EntityManager[T], Generic[T]):
    object_name = "room"
