import datetime

from alfacrm.entities import Tariff


def test_init_tariff():
    tariff = Tariff(
        id=1,
        type=1,
        name="Name",
        price=9.0,
        lesson_count=4,
        duration=20,
        added=datetime.datetime(2021, 11, 12, 22, 58, 0),
        branch_ids=[1],
    )

    assert tariff.id == 1
    assert tariff.tariff_type == 1
    assert tariff.name == "Name"
    assert tariff.price == 9.0
    assert tariff.lesson_count == 4
    assert tariff.duration == 20
    assert tariff.added == datetime.datetime(2021, 11, 12, 22, 58, 0)
    assert tariff.branch_ids == [1]
