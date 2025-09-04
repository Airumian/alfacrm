from typing import Generic, TypeVar

from ..core import EntityManager

T = TypeVar("T")


class Tariff(EntityManager[T], Generic[T]):
    object_name = "tariff"
