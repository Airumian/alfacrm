from typing import Generic, TypeVar

from ..core.entity_manager import EntityManager

T = TypeVar("T")


class StudyStatus(EntityManager[T], Generic[T]):
    object_name = "study-status"

    async def list(
        self,
        page: int = 0,
        count: int = 100,
        name: str | None = None,
        **kwargs,
    ) -> list[T]:
        """
        Get list study statuses
        :param name: filter by name
        :param page: page
        :param count: count branches of page
        :param kwargs: additional filters
        :return: list of branches
        """
        result = await self._list(page, count, name=name, **kwargs)

        return self._result_to_entities(result)
