from typing import Generic, TypeVar

from ..core import EntityManager

T = TypeVar("T")


class LeadReject(EntityManager[T], Generic[T]):
    object_name = "lead-reject"
