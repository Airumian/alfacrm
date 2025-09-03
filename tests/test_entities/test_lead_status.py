from alfacrm.entities import LeadStatus


def test_init_lead_status():
    lead_status = LeadStatus(
        id=1,
        name="name",
        is_enabled=True,
        weight=2,
    )

    assert lead_status.id == 1
    assert lead_status.name == "name"
    assert lead_status.is_enabled is True
    assert lead_status.weight == 2
