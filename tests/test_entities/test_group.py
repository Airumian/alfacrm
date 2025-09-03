import datetime

from alfacrm.entities import Group


def test_init_group():
    group = Group(
        id=1,
        branch_ids=[],
        teacher_ids=[1],
        name="Name",
        level_id=1,
        status_id=2,
        company_id=3,
        streaming_id=5,
        limit=20,
        note="Note",
        b_date=datetime.date(2021, 12, 12),
        e_date=datetime.date(2022, 1, 1),
    )

    assert group.id == 1
    assert group.branch_ids == []
    assert group.teacher_ids == [1]
    assert group.name == "Name"
    assert group.level_id == 1
    assert group.status_id == 2
    assert group.company_id == 3
    assert group.streaming_id == 5
    assert group.limit == 20
    assert group.note == "Note"
    assert group.b_date == datetime.date(2021, 12, 12)
    assert group.e_date == datetime.date(2022, 1, 1)
