import typing

from ..core.entity_manager import EntityManager

T = typing.TypeVar("T")


class Location(EntityManager, typing.Generic[T]):
    object_name = "location"

    async def list(
        self,
        page: int = 0,
        count: int = 100,
        name: str | None = None,
        is_active: bool | None = None,
        **kwargs,
    ) -> list[T]:
        """
        Get list locations
        :param name: filter by name
        :param is_active: filter by is_active
        :param page: page
        :param count: count branches of page
        :param kwargs: additional filters
        :return: list of branches
        """
        result = await self._list(page, count, name=name, is_active=is_active, **kwargs)

        return self._result_to_entities(result)
