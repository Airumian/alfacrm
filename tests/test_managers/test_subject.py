import pytest

from alfacrm import entities, managers

SUBJECT_RESPONSE = {
    "page": 0,
    "total": 1,
    "count": 1,
    "items": [
        {
            "id": 1,
            "name": "Name",
            "weight": 4,
        },
    ],
}


@pytest.mark.asyncio
async def test_subject(api_client, aresponses):
    aresponses.add(
        "demo.s20.online", "/v2api/1/subject/index", "POST", SUBJECT_RESPONSE
    )

    subject_object = managers.Subject(
        api_client=api_client,
        entity_class=entities.Subject,
    )

    subjects = await subject_object.list()

    assert len(subjects) == 1

    subject = subjects[0]

    assert subject.id == 1
    assert subject.name == "Name"
    assert subject.weight == 4
