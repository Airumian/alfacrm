import pytest

from alfacrm import entities, managers

LEAD_STATUS_RESPONSE = {
    "page": 0,
    "total": 1,
    "count": 1,
    "items": [
        {
            "id": 1,
            "name": "Name",
            "is_enabled": 0,
            "weight": 2,
        }
    ],
}


@pytest.mark.asyncio
async def test_lead_status(api_client, aresponses):
    aresponses.add(
        "demo.s20.online", "/v2api/1/lead-status/index", "POST", LEAD_STATUS_RESPONSE
    )

    lead_status_manager = managers.LeadStatus(
        api_client=api_client,
        entity_class=entities.LeadStatus,
    )

    lead_statuses = await lead_status_manager.list()

    assert len(lead_statuses) == 1

    lead_status = lead_statuses[0]

    assert lead_status.id == 1
    assert lead_status.name == "Name"
    assert lead_status.is_enabled is False
    assert lead_status.weight == 2
