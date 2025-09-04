from typing import Generic, TypeVar

from ..core import EntityManager

T = TypeVar("T")


class PayAccount(EntityManager[T], Generic[T]):
    object_name = "pay-account"
