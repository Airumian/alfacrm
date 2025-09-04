from typing import Generic, TypeVar

from ..core.entity_manager import EntityManager

T = TypeVar("T")


class LeadSource(EntityManager[T], Generic[T]):
    object_name = "lead-source"

    async def list(
        self,
        page: int = 0,
        count: int = 100,
        name: str | None = None,
        code: str | None = None,
        is_enabled: bool | None = None,
        **kwargs,
    ) -> list[T]:
        """
        Get list customers
        :param page: page
        :param count: count branches of page
        :param name: filter by name
        :param code: filter by code
        :param is_enabled: filter by is_enabled
        :param kwargs: additional filters
        :return: list of branches
        """
        result = await self._list(
            page, count, code=code, is_enabled=is_enabled, name=name, **kwargs
        )
        return self._result_to_entities(result)
