import pytest

from alfacrm import entities, managers

LOCATION_RESPONSE = {
    "page": 0,
    "total": 1,
    "count": 1,
    "items": [
        {"id": 1, "branch_id": 2, "name": "Name", "is_active": 1, "weight": 0},
    ],
}


@pytest.mark.asyncio
async def test_location(api_client, aresponses):
    aresponses.add(
        "demo.s20.online", "/v2api/1/location/index", "POST", LOCATION_RESPONSE
    )

    location_manager = managers.Location(
        api_client=api_client,
        entity_class=entities.Location,
    )

    locations = await location_manager.list()

    assert len(locations) == 1

    location = locations[0]

    assert location.id == 1
    assert location.branch_id == 2
    assert location.name == "Name"
    assert location.is_active is True
    assert location.weight == 0
