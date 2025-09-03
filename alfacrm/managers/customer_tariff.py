import typing

from ..core import EntityManager

T = typing.TypeVar("T")


class CustomerTariff(EntityManager, typing.Generic[T]):
    object_name = "customer-tariff"

    async def list(
        self,
        customer_id: int | None = None,
        page: int = 0,
        count: int = 100,
        *args,
        **kwargs,
    ) -> list[T]:
        if customer_id is None:
            raise ValueError("customer_id is not filled")
        result = await self._list(
            page=page,
            count=count,
            params={
                "customer_id": customer_id,
            },
            **kwargs,
        )

        return self._result_to_entities(result)

    async def get(
        self,
        id_: int,
        customer_id: int | None = None,
        **kwargs,
    ) -> T:
        if customer_id is None:
            raise ValueError("customer_id is not filled")
        result = await self._get(
            id_=id_,
            params={
                "customer_id": customer_id,
            },
            **kwargs,
        )

        return self._result_to_entity(result)

    async def save(
        self,
        model: T,
        customer_id: int | None = None,
    ) -> T:
        result = await self._save(
            params={
                "customer_id": customer_id,
            },
            **model.serialize(),
        )

        return self._result_to_entity(result)
