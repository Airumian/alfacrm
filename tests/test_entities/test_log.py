import datetime

from alfacrm.entities import Log


def test_init_log():
    log = Log(
        entity="Entity",
        entity_id=1,
        user_id=2,
        event=1,
        fields_old=[],  # noqa
        fields_new={
            "field_1": "value1",
            "field_2": 2,
        },
        fields_rel="",  # noqa
        date_time=datetime.datetime(2021, 1, 1, 14, 0, 0),
    )

    assert log.entity == "Entity"
    assert log.entity_id == 1
    assert log.user_id == 2
    assert log.event == 1
    assert log.fields_old == {}
    assert log.fields_new == {"field_1": "value1", "field_2": 2}
    assert log.fields_rel == {}
    assert log.date_time == datetime.datetime(2021, 1, 1, 14, 0, 0)
