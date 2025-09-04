from typing import Generic, TypeVar

from ..core import EntityManager

T = TypeVar("T")


class Discount(EntityManager[T], Generic[T]):
    object_name = "discount"
