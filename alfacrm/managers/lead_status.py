from typing import Generic, TypeVar

from ..core.entity_manager import EntityManager

T = TypeVar("T")


class LeadStatus(EntityManager[T], Generic[T]):
    object_name = "lead-status"

    async def list(
        self,
        page: int = 0,
        count: int = 100,
        name: str | None = None,
        is_enabled: bool | None = None,
        **kwargs,
    ) -> list[T]:
        """
        Get list lead statuses
        :param name: filter by name
        :param count: count branches of page
        :param page: page
        :param is_enabled: filter by is_enabled
        :param kwargs: additional filters
        :return: list of branches
        """
        result = await self._list(
            page, count, name=name, is_enabled=is_enabled, **kwargs
        )

        return self._result_to_entities(result)
