import typing

from alfacrm.core.entity_manager import EntityManager

T = typing.TypeVar("T")


class Subject(EntityManager, typing.Generic[T]):
    object_name = "subject"

    async def list(
        self,
        page: int = 0,
        count: int = 100,
        name: str | None = None,
        **kwargs,
    ) -> list[T]:
        """
        Get list customers
        :param page: page
        :param count: count branches of page
        :param name: filter by name
        :param kwargs: additional filters
        :return: list of branches
        """
        result = await self._list(page, count, name=name, **kwargs)

        return self._result_to_entities(result)
