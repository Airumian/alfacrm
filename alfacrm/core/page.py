import typing

T = typing.TypeVar("T")


class Page(typing.Generic[T]):
    def __init__(self, number: int, items: typing.List[T], total: int):
        self.number = number
        self.items = items
        self.total = total
        self.count = len(items)
