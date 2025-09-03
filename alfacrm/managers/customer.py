import typing

from ..core.entity_manager import EntityManager

T = typing.TypeVar("T")


class Customer(EntityManager, typing.Generic[T]):
    object_name = "customer"

    async def list(
        self,
        page: int = 0,
        count: int = 100,
        name: typing.Optional[str] = None,
        is_study: typing.Optional[bool] = None,
        legal_type: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.List[T]:
        """
        Get list customers
        :param name: filter by name
        :param is_study: filter by is_study
        :param page: page
        :param count: count branches of page
        :param legal_type: client type
        :param kwargs: additional filters
        :return: list of branches
        """
        result = await self._list(
            page, count, name=name, is_study=is_study, legal_type=legal_type, **kwargs
        )

        return self._result_to_entities(result)
