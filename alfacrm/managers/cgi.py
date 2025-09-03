import typing

from ..core import EntityManager

T = typing.TypeVar("T")


class CGI(EntityManager, typing.Generic[T]):
    object_name = "cgi"

    async def list(
        self,
        page: int = 0,
        count: int = 100,
        customer_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        *args,
        **kwargs,
    ) -> typing.List[T]:
        if customer_id is None and group_id is None:
            raise ValueError("Need customer_id or group_id")

        result = await self._list(
            page=page,
            count=count,
            params={
                "customer_id": customer_id,
                "group_id": group_id,
            },
            **kwargs,
        )

        return self._result_to_entities(result)

    async def get(
        self,
        id_: int,
        customer_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> T:
        if customer_id is None and group_id is None:
            raise ValueError("Need customer_id or group_id")
        result = await self._get(
            id_=id_,
            params={
                "customer_id": customer_id,
                "group_id": group_id,
            },
            **kwargs,
        )

        return self._result_to_entity(result)
