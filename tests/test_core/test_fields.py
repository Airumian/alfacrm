import datetime
from typing import Any, Dict, List

import pytest

from alfacrm import fields
from alfacrm.core import AlfaEntity
from alfacrm.core.exceptions import FieldNotEditable


class AlfaEntityClass(AlfaEntity):
    integer_field: int = fields.Integer()
    float_field: float = fields.Float()
    bool_field: bool = fields.Bool()
    string_field: str = fields.String()
    datetime_field: datetime.datetime = fields.DateTimeField()
    date_field: datetime.date = fields.DateField()
    list_field: List[int] = fields.ListField(fields.Integer())
    time_field: datetime.time = fields.TimeField()
    dict_field: Dict[str, Any] = fields.DictField()
    not_editable_field: int = fields.Integer(editable=False)


def test_integer_field():
    a = AlfaEntityClass()

    a.integer_field = None
    assert a.integer_field is None
    a.integer_field = 10
    assert a.integer_field == 10
    a.integer_field = "10"
    assert a.integer_field == 10
    a.integer_field = 11.2
    assert a.integer_field == 11
    assert a.props["integer_field"].export(a) == 11
    with pytest.raises(ValueError):
        a.integer_field = "string"


def test_float_field():
    a = AlfaEntityClass()
    a.float_field = None
    assert a.float_field is None
    a.float_field = 10.2
    assert a.float_field == 10.2
    a.float_field = 10
    assert a.float_field == 10.0
    a.float_field = "10.2"
    assert a.float_field == 10.2
    assert a.props["float_field"].export(a) == 10.2
    with pytest.raises(ValueError):
        a.float_field = "str"


def test_bool_field():
    a = AlfaEntityClass()
    a.bool_field = None
    assert a.bool_field is None
    a.bool_field = False
    assert a.bool_field is False
    a.bool_field = True
    assert a.bool_field is True
    a.bool_field = "str"  # Not empty string is True
    assert a.bool_field is True
    a.bool_field = ""  # Empty string is False
    assert a.bool_field is False

    assert a.props["bool_field"].export(a) is False


def test_string_field():
    a = AlfaEntityClass()

    a.string_field = None
    assert a.string_field is None
    a.string_field = "string"
    assert a.string_field == "string"

    assert a.props["string_field"].export(a) == "string"


def test_date_field():
    a = AlfaEntityClass()

    a.date_field = None
    assert a.date_field is None

    a.date_field = "01.01.2021"
    assert a.date_field == datetime.date(year=2021, month=1, day=1)

    a.date_field = "2021-01-01"
    assert a.date_field == datetime.date(year=2021, month=1, day=1)

    a.date_field = datetime.date(year=2021, month=1, day=1)
    assert a.date_field == datetime.date(year=2021, month=1, day=1)

    a.date_field = datetime.datetime(year=2021, month=1, day=1, hour=20, minute=20)
    assert a.date_field == datetime.date(year=2021, month=1, day=1)
    assert a.props["date_field"].export(a) == "2021-01-01"
    with pytest.raises(ValueError):
        a.date_field = "not-date-string"


def test_datetime_field():
    a = AlfaEntityClass()

    a.datetime_field = None
    assert a.datetime_field is None

    a.datetime_field = "2021-01-01 14:00:00"
    assert a.datetime_field == datetime.datetime(2021, 1, 1, 14, 0, 0)

    a.datetime_field = datetime.datetime(2021, 1, 1, 14, 0, 0)
    assert a.datetime_field == datetime.datetime(2021, 1, 1, 14, 0, 0)
    assert a.props["datetime_field"].export(a) == "2021-01-01T14:00:00"

    with pytest.raises(ValueError):
        a.datetime_field = "not-datetime-string"


def test_list_field():
    a = AlfaEntityClass()

    a.list_field = None
    assert a.list_field is None

    a.list_field = [1, 2, 3]
    assert a.list_field == [1, 2, 3]
    assert a.props["list_field"].export(a) == [1, 2, 3]

    with pytest.raises(ValueError):
        a.list_field = [1, "not-digit"]


def test_time_field():
    a = AlfaEntityClass()

    a.time_field = None
    assert a.time_field is None

    a.time_field = "2021-01-01 14:00:00"
    assert a.time_field == datetime.time(14, 0, 0)

    a.time_field = datetime.datetime(2021, 2, 1, 13, 0, 1)
    assert a.time_field == datetime.time(13, 0, 1)

    a.time_field = datetime.time(12, 1, 30)
    assert a.time_field == datetime.time(12, 1, 30)

    a.time_field = "14:00"
    assert a.time_field == datetime.time(14, 0, 0)

    a.time_field = "14:01:02"
    assert a.time_field == datetime.time(14, 1, 2)

    assert a.props["time_field"].export(a) == "14:01:02"

    with pytest.raises(ValueError):
        a.time_field = "not time string"


def test_dict_field():
    a = AlfaEntityClass()

    a.dict_field = None
    assert a.dict_field is None

    a.dict_field = ""
    assert a.dict_field == {}

    a.dict_field = []
    assert a.dict_field == {}

    a.dict_field = {
        "d_field1": 10,
        "d_field2": "value",
    }

    assert a.dict_field == {"d_field1": 10, "d_field2": "value"}

    a.dict_field = '{"dict_field": "value"}'
    assert a.dict_field == {"dict_field": "value"}

    assert a.props["dict_field"].export(a) == {"dict_field": "value"}

    with pytest.raises(ValueError) as context:
        a.dict_field = "123"

    assert str(context.value) == "<123> is not dict"

    with pytest.raises(ValueError) as context:
        a.dict_field = "{field"

    assert str(context.value) == "<{field> is not dict"


def test_not_editable_field():
    a = AlfaEntityClass(
        not_editable_field=2,
    )

    assert a.not_editable_field == 2

    with pytest.raises(FieldNotEditable) as context:
        a.not_editable_field = 4

    assert str(context.value) == "<not_editable_field> is not editable"
