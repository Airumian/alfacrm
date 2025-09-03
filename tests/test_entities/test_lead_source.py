from alfacrm.entities import LeadSource


def test_init_lead_source():
    lead_source = LeadSource(
        id=1,
        code="123",
        name="name",
        is_enabled=True,
        weight=1,
    )

    assert lead_source.id == 1
    assert lead_source.code == "123"
    assert lead_source.name == "name"
    assert lead_source.is_enabled is True
    assert lead_source.weight == 1
