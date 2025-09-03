from alfacrm.core.entity import BaseAlfaEntity
from alfacrm.fields import Integer


class AnotherClass:
    pass


class BaseAlfaClass(BaseAlfaEntity, AnotherClass):
    field1 = Integer()
    field2 = Integer(alias="field2_alias")
    field3 = Integer(default=10)
    field4 = Integer()


class FirstClass(BaseAlfaEntity):
    field1 = Integer()


class SecondClass(BaseAlfaEntity):
    field2 = Integer()


def test_init_alfa_object():
    a = BaseAlfaClass(
        field1=1,
        field2=2,
        field4=None,
    )
    assert a.values == {"field1": 1, "field2": 2, "field3": 10, "field4": None}
    assert a.props_aliases == {
        "field1": "field1",
        "field2": "field2_alias",
        "field3": "field3",
        "field4": "field4",
    }


def test_alfa_object_serialize():
    a = BaseAlfaClass(field1=1, field2=2, field4=None)

    serialized_object = a.serialize()
    assert serialized_object == {"field1": 1, "field2_alias": 2, "field3": 10}
    assert str(a) == str({"field1": 1, "field2_alias": 2, "field3": 10})
    assert repr(a) == str({"field1": 1, "field2_alias": 2, "field3": 10})


def test_eq():
    first_1 = FirstClass(
        field1=1,
    )

    first_2 = FirstClass(field1=1)

    first_3 = FirstClass(
        field1=2,
    )

    second_1 = SecondClass(
        field=1,
    )

    assert first_1 == first_1
    assert first_1 == first_2
    assert first_1 != first_3
    assert first_1 != second_1
