import datetime

from alfacrm.entities import Task


def test_init_task():
    task = Task(
        id=1,
        company_id=2,
        branch_ids=[1, 2],
        user_id=3,
        assigned_ids=[1, 2, 3],
        group_ids=[4, 5, 6],
        customer_ids=[1],
        title="Title",
        text="Text",
        is_archive=False,
        created_at=datetime.datetime(2021, 11, 12, 22, 35, 0),
        is_done=True,
        is_private=False,
        due_date=datetime.date(2022, 1, 1),
        done_date=datetime.datetime(2021, 11, 15, 13, 0, 0),
        is_public_entry=True,
        is_notify=False,
        priority=1,
    )
    assert task.id == 1
    assert task.company_id == 2
    assert task.branch_ids == [1, 2]
    assert task.user_id == 3
    assert task.assigned_ids == [1, 2, 3]
    assert task.group_ids == [4, 5, 6]
    assert task.customer_ids == [1]
    assert task.title == "Title"
    assert task.text == "Text"
    assert task.is_archive is False
    assert task.created_at == datetime.datetime(2021, 11, 12, 22, 35, 0)
    assert task.is_done is True
    assert task.is_private is False
    assert task.due_date == datetime.date(2022, 1, 1)
    assert task.done_date == datetime.datetime(2021, 11, 15, 13, 0, 0)
    assert task.is_public_entry is True
    assert task.is_notify is False
    assert task.priority
