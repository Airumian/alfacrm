from alfacrm.entities import LessonType


def test_init_lesson_type():
    lesson_type = LessonType(
        id=1,
        name="Name",
        type=2,
        icon="icon",
        is_active=True,
        sort=100,
    )

    assert lesson_type.id == 1
    assert lesson_type.name == "Name"
    assert lesson_type.lesson_type == 2
    assert lesson_type.icon == "icon"
    assert lesson_type.is_active is True
    assert lesson_type.sort == 100
