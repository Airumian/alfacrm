import typing

from .field import BaseField

T = typing.TypeVar("T")

PROPS_ATTR_NAME = "_props"
VALUES_ATTR_NAME = "_values"
ALIASES_ATTR_NAME = "_aliases"


class AlfaEntityMeta(type):
    def __new__(
        mcs: typing.Type[T],
        name: str,
        bases: typing.Tuple[typing.Type],
        namespace: typing.Dict[str, typing.Any],
        **kwargs: typing.Any,
    ):
        cls = super(AlfaEntityMeta, mcs).__new__(mcs, name, bases, namespace)

        props = {}
        values = {}
        aliases = {}

        for base in bases:
            if not isinstance(base, AlfaEntityMeta):
                continue
            props.update(getattr(base, PROPS_ATTR_NAME))
            aliases.update(getattr(base, ALIASES_ATTR_NAME))

        for name, prop in (
            (name, prop)
            for name, prop in namespace.items()
            if isinstance(prop, BaseField)
        ):
            props[prop.alias] = prop
            if prop.default is not None:
                values[prop.alias] = prop.default
            aliases[name] = prop.alias

        setattr(cls, PROPS_ATTR_NAME, props)
        setattr(cls, ALIASES_ATTR_NAME, aliases)

        return cls


class BaseAlfaEntity(metaclass=AlfaEntityMeta):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.props:
                self.props[key].set_value(self, value, parent=self)
            else:
                self.values[key] = value

        for key, value in self.props.items():
            if value.default and key not in self.values:
                self.values[key] = value.default

    def __str__(self):
        return str(self.serialize())

    def __repr__(self):
        return str(self.serialize())

    @property
    def values(self) -> typing.Dict[str, typing.Any]:
        """
        Get values
        :return:
        """
        if not hasattr(self, VALUES_ATTR_NAME):
            setattr(self, VALUES_ATTR_NAME, {})
        return getattr(self, VALUES_ATTR_NAME)

    @property
    def props(self) -> typing.Dict[str, BaseField]:
        """
        Get props
        :return: dict with props
        """
        return getattr(self, PROPS_ATTR_NAME, {})

    @property
    def props_aliases(self) -> typing.Dict[str, str]:
        """
        Get aliases for props
        :return:
        """
        return getattr(self, ALIASES_ATTR_NAME, {})

    def serialize(self) -> typing.Dict[str, typing.Any]:
        result = {}
        for name, value in self.values.items():
            if value is None:
                continue
            if name in self.props:
                value = self.props[name].export(self)

            result[self.props_aliases.get(name, name)] = value
        return result

    def __eq__(self, other: "BaseAlfaEntity") -> bool:
        return (
            self.serialize() == other.serialize() and self.__class__ == other.__class__
        )


class AlfaEntity(BaseAlfaEntity):
    id: int | None
