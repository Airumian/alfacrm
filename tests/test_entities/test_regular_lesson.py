import datetime

from alfacrm.entities import RegularLesson


def test_init_regular_lesson():
    regular_lesson = RegularLesson(
        id=1,
        branch_id=2,
        lesson_type_id=3,
        related_class="Group",
        related_id=1,
        subject_id=3,
        streaming=False,
        teacher_ids=[1, 2],
        room_id=1,
        day=1,
        days=[1],
        time_from_v=datetime.time(14, 0),
        time_to_v=datetime.time(15, 0, 0),
        e_date_v=datetime.date(2021, 1, 1),
        b_date_v=datetime.date(2021, 10, 1),
        b_date=datetime.date(2021, 1, 1),
        e_date=datetime.date(2021, 10, 1),
        is_public=True,
    )

    assert regular_lesson.id == 1
    assert regular_lesson.branch_id == 2
    assert regular_lesson.lesson_type_id == 3
    assert regular_lesson.related_class == "Group"
    assert regular_lesson.related_id == 1
    assert regular_lesson.subject_id == 3
    assert regular_lesson.streaming is False
    assert regular_lesson.teacher_ids == [1, 2]
    assert regular_lesson.room_id == 1
    assert regular_lesson.day == 1
    assert regular_lesson.days == [1]
    assert regular_lesson.time_from_v == datetime.time(14, 0)
    assert regular_lesson.time_to_v == datetime.time(15, 0, 0)
    assert regular_lesson.e_date_v == datetime.date(2021, 1, 1)
    assert regular_lesson.b_date_v == datetime.date(2021, 10, 1)
    assert regular_lesson.b_date == datetime.date(2021, 1, 1)
    assert regular_lesson.b_date_v == datetime.date(2021, 10, 1)
    assert regular_lesson.is_public is True
