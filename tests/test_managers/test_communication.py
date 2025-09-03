import datetime

import pytest

from alfacrm import entities, managers
from tests.conftest import DEFAULT_BRANCH_ID, DEFAULT_HOST, make_response

COMMUNICATION_RESPONSE = {
    "page": 0,
    "count": 1,
    "total": 1,
    "items": [
        {
            "id": 1,
            "type_id": 2,
            "class": "Customer",
            "related_id": 3,
            "user_id": 4,
            "added": "2021-01-01 14:00:00",
            "comment": "Comment",
        }
    ],
}


@pytest.fixture
def communication_manager(api_client):
    return managers.Communication(
        api_client=api_client,
        entity_class=entities.Communication,
    )


@pytest.mark.asyncio
async def test_list_communication(
    communication_manager: managers.Communication[entities.Communication],
    aresponses,
):
    aresponses.add(
        DEFAULT_HOST,
        f"/v2api/{DEFAULT_BRANCH_ID}/communication/index?class=Customer&related_id=1&per-page=100",
        "POST",
        COMMUNICATION_RESPONSE,
        match_querystring=True,
    )

    communications = await communication_manager.list(
        related_class="Customer",
        related_id=1,
    )

    assert len(communications) == 1

    communication = communications[0]
    check_communication(communication)


@pytest.mark.asyncio
async def test_get_communication(
    communication_manager: managers.Communication[entities.Communication],
    aresponses,
):
    aresponses.add(
        DEFAULT_HOST,
        f"/v2api/{DEFAULT_BRANCH_ID}/communication/index?class=Customer&related_id=1&per-page=100",
        "POST",
        COMMUNICATION_RESPONSE,
        match_querystring=True,
    )
    communication = await communication_manager.get(
        id_=1,
        related_class="Customer",
        related_id=1,
    )

    check_communication(communication)


@pytest.mark.asyncio
async def test_save_communication(
    communication_manager: managers.Communication[entities.Communication],
    aresponses,
):
    aresponses.add(
        DEFAULT_HOST,
        f"/v2api/{DEFAULT_BRANCH_ID}/communication/create?class=Customer&related_id=1",
        "POST",
        make_response(model={"id": 1, "class": "Customer", "related_id": 1}),
        match_querystring=True,
    )

    comminication = entities.Communication(user_id=2)

    created_communication = await communication_manager.save(
        comminication,
        related_class="Customer",
        related_id=1,
    )

    assert created_communication.id == 1
    assert created_communication.related_class == "Customer"
    assert created_communication.related_id == 1


def check_communication(communication: entities.Communication):
    assert communication.id == 1
    assert communication.type_id == 2
    assert communication.related_class == "Customer"
    assert communication.related_id == 3
    assert communication.added == datetime.datetime(2021, 1, 1, 14, 0, 0)
    assert communication.comment == "Comment"
