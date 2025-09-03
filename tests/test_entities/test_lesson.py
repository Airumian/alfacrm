import datetime

from alfacrm.entities import Lesson


def test_init_lesson():
    lesson = Lesson(
        id=1,
        branch_id=2,
        date=datetime.date(2021, 1, 1),
        time_from=datetime.datetime(2021, 1, 1, 13, 0, 0),
        time_to=datetime.datetime(2021, 1, 1, 14, 0, 0),
        lesson_type_id=1,
        status=1,
        subject_id=1,
        room_id=1,
        teacher_ids=[1, 2, 3],
        customer_ids=[4, 2, 1],
        group_ids=[1],
        streaming=False,
        note="",
    )

    assert lesson.id == 1
    assert lesson.branch_id == 2
    assert lesson.date == datetime.date(2021, 1, 1)
    assert lesson.time_from == datetime.datetime(2021, 1, 1, 13, 0, 0)
    assert lesson.time_to == datetime.datetime(2021, 1, 1, 14, 0, 0)
    assert lesson.lesson_type_id == 1
    assert lesson.status == 1
    assert lesson.subject_id == 1
    assert lesson.room_id == 1
    assert lesson.teacher_ids == [1, 2, 3]
    assert lesson.customer_ids == [4, 2, 1]
    assert lesson.group_ids == [1]
    assert lesson.streaming is False
    assert lesson.note == ""
