from alfacrm.entities import Room


def test_init_room():
    room = Room(
        id=1,
        branch_id=2,
        location_id=3,
        streaming_id=4,
        color_id=5,
        name="Name",
        note="Note",
        is_enabled=False,
        weight=5,
    )

    assert room.id == 1
    assert room.branch_id == 2
    assert room.location_id == 3
    assert room.streaming_id == 4
    assert room.color_id == 5
    assert room.name == "Name"
    assert room.note == "Note"
    assert room.is_enabled is False
    assert room.weight == 5
