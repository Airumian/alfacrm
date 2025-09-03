import pytest

from alfacrm import entities, managers

LEAD_SOURCE_RESPONSE = {
    "page": 0,
    "total": 1,
    "count": 1,
    "items": [
        {
            "id": 1,
            "name": "Name",
            "code": "Code",
            "is_enabled": 1,
            "weight": 1,
        }
    ],
}


@pytest.mark.asyncio
async def test_lead_source(api_client, aresponses):
    aresponses.add(
        "demo.s20.online", "/v2api/1/lead-source/index", "POST", LEAD_SOURCE_RESPONSE
    )

    lead_source_manager = managers.LeadSource(
        api_client=api_client,
        entity_class=entities.LeadSource,
    )

    lead_sources = await lead_source_manager.list()

    assert len(lead_sources) == 1

    lead_source = lead_sources[0]

    assert lead_source.id == 1
    assert lead_source.name == "Name"
    assert lead_source.code == "Code"
    assert lead_source.is_enabled is True
    assert lead_source.weight == 1
