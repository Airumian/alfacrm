from typing import Generic, TypeVar

from ..core import EntityManager

T = TypeVar("T")


class Pay(EntityManager[T], Generic[T]):
    object_name = "pay"
