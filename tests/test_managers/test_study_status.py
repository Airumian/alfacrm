import pytest

from alfacrm import entities, managers

STUDY_STATUS_RESPONSE = {
    "page": 0,
    "total": 1,
    "count": 1,
    "items": [
        {
            "id": 1,
            "name": "Name",
            "is_enabled": 1,
            "weight": 3,
        },
    ],
}


@pytest.mark.asyncio
async def test_study_status(api_client, aresponses):
    aresponses.add(
        "demo.s20.online", "/v2api/1/study-status/index", "POST", STUDY_STATUS_RESPONSE
    )

    study_status_manager = managers.StudyStatus(
        api_client=api_client,
        entity_class=entities.StudyStatus,
    )

    study_statuses = await study_status_manager.list()

    assert len(study_statuses) == 1
    study_status = study_statuses[0]

    assert study_status.id == 1
    assert study_status.name == "Name"
    assert study_status.is_enabled is True
    assert study_status.weight == 3
