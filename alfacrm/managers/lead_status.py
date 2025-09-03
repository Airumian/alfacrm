import typing

from ..core.entity_manager import EntityManager

T = typing.TypeVar("T")


class LeadStatus(EntityManager, typing.Generic[T]):
    object_name = "lead-status"

    async def list(
        self,
        page: int = 0,
        count: int = 100,
        name: typing.Optional[str] = None,
        is_enabled: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.List[T]:
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
