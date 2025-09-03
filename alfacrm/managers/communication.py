import typing

from ..core import EntityManager

T = typing.TypeVar("T")


class Communication(EntityManager, typing.Generic[T]):
    object_name = "communication"

    async def list(
        self,
        related_class: str | None = None,
        related_id: int | None = None,
        page: int = 0,
        count: int = 100,
        *args,
        **kwargs,
    ) -> list[T]:
        result = await self._list(
            page=page,
            count=count,
            params={
                "class": related_class,
                "related_id": related_id,
            },
            **kwargs,
        )

        return self._result_to_entities(result)

    async def get(
        self,
        id_: int,
        related_class: str | None = None,
        related_id: int | None = None,
        **kwargs,
    ) -> T:
        result = await self._get(
            id_=id_,
            params={
                "class": related_class,
                "related_id": related_id,
            },
            **kwargs,
        )

        return self._result_to_entity(result)

    async def save(
        self,
        model: T,
        related_class: str | None = None,
        related_id: int | None = None,
    ) -> T:
        result = await self._save(
            params={
                "class": related_class,
                "related_id": related_id,
            },
            **model.serialize(),
        )
        return self._result_to_entity(result)
