from alfacrm.entities import Location


def test_init_location():
    location = Location(
        id=1,
        branch_id=1,
        is_active=True,
        name="name",
    )

    assert location.id == 1
    assert location.branch_id == 1
    assert location.is_active is True
    assert location.name == "name"
