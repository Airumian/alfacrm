import typing

from ..core.entity_manager import EntityManager

T = typing.TypeVar("T")


class LeadSource(EntityManager, typing.Generic[T]):
    object_name = "lead-source"

    async def list(
        self,
        page: int = 0,
        count: int = 100,
        name: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        is_enabled: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.List[T]:
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
