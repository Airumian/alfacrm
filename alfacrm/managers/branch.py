from typing import Generic, TypeVar

from ..core.entity_manager import EntityManager

T = TypeVar("T")


class Branch(EntityManager[T], Generic[T]):
    object_name = "branch"

    async def list(
        self,
        page: int = 0,
        count: int = 100,
        name: str | None = None,
        is_active: bool | None = None,
        subject_ids: list[int] | None = None,
        **kwargs,
    ) -> list[T]:
        """
        Get list branches
        :param name: filter by name
        :param is_active: filter by is_active
        :param subject_ids: filter by subject_ids
        :param page: page
        :param count: count branches of page
        :param kwargs: additional filters
        :return: list of branches
        """
        result = await self._list(
            page,
            count,
            name=name,
            is_active=is_active,
            subject_ids=subject_ids,
            **kwargs,
        )
        return self._result_to_entities(result)
