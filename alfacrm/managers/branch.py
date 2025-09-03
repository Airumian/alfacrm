import typing

from ..core.entity_manager import EntityManager

T = typing.TypeVar("T")


class Branch(EntityManager, typing.Generic[T]):
    object_name = "branch"

    async def list(
        self,
        page: int = 0,
        count: int = 100,
        name: typing.Optional[str] = None,
        is_active: typing.Optional[bool] = None,
        subject_ids: typing.Optional[typing.List[int]] = None,
        **kwargs,
    ) -> typing.List[T]:
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
