from alfacrm.entities import StudyStatus


def test_init_study_status():
    study_status = StudyStatus(
        id=1,
        name="name",
        is_enabled=False,
        weight=3,
    )

    assert study_status.id == 1
    assert study_status.name == "name"
    assert study_status.is_enabled is False
    assert study_status.weight == 3
