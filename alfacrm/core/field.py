import abc
import typing

from .exceptions import FieldNotEditable


class BaseField(metaclass=abc.ABCMeta):
    """Base field"""

    def __init__(
        self,
        base: typing.Optional["BaseField"] = None,
        default: typing.Any = None,
        alias: str | None = None,
        editable: bool = True,
    ):
        self.base_field = base
        self.default = default
        self.alias = alias
        self.editable = editable

    def __set_name__(self, owner, name):
        if self.alias is None:
            self.alias = name

    def set_value(self, instance, value: typing.Any, parent=None):
        value = self.deserialize(value)
        instance.values[self.alias] = value

    def get_value(self, instance):
        return instance.values.get(self.alias, self.default)

    def __set__(self, instance, value: typing.Any):
        if not self.editable:
            raise FieldNotEditable(message=f"<{self.alias}> is not editable")

        self.set_value(instance, value)

    def __get__(self, instance, owner: typing.Any):
        return self.get_value(instance)

    @abc.abstractmethod
    def serialize(self, value: typing.Any) -> typing.Any:
        pass  # pragma: no cover

    @abc.abstractmethod
    def deserialize(self, value: typing.Any) -> typing.Any:
        pass  # pragma: no cover

    def export(self, instance):
        """
        Alias for `serialize` but for current Object instance
        :param instance:
        :return:
        """
        return self.serialize(self.get_value(instance))
