import datetime

from alfacrm.entities import Communication


def test_init_communication():
    communication = Communication(
        id=1,
        type_id=2,
        related_id=3,
        user_id=4,
        added=datetime.datetime(2021, 1, 1, 14, 0, 0),
        comment="Comment",
        **{
            "class": "Customer",
        },
    )

    assert communication.id == 1
    assert communication.type_id == 2
    assert communication.related_class == "Customer"
    assert communication.related_id == 3
    assert communication.user_id == 4
    assert communication.added == datetime.datetime(2021, 1, 1, 14, 0, 0)
    assert communication.comment == "Comment"
