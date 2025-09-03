import math
import typing

from . import entity_manager
from .page import Page

T = typing.TypeVar("T")


class Paginator(typing.Generic[T]):
    def __init__(
        self,
        alfa_object: "entity_manager.EntityManager",
        start_page: int = 0,
        page_size: int = 20,
        filters: dict[str, typing.Any] | None = None,
    ):
        self._page_number = start_page
        self._page: Page[T] | None = None
        self._total = 0
        self._page_size = page_size
        if filters is None:
            filters = {}
        self._filters = filters
        self._object = alfa_object

    def __aiter__(self) -> typing.Iterable[Page[T]]:
        return self  # noqa

    async def __anext__(self) -> Page[T]:
        if self._total and self._page_number >= self.total_page:
            raise StopAsyncIteration

        page = await self._object.page(
            page=self._page_number,
            count=self._page_size,
            **self._filters,
        )
        self._total = page.total
        self._page_number += 1
        return page

    @property
    def total_page(self) -> int:
        """
        Get total page by total count and page size
        :return:
        """
        return math.ceil(self._total / self._page_size)
