from alfacrm.entities import PayAccount


def test_init_account():
    pay_account = PayAccount(
        id=1,
        branch_id=2,
        name="Name",
        user_ids=[2],
        is_enabled=False,
        weight=2,
    )

    assert pay_account.id == 1
    assert pay_account.branch_id == 2
    assert pay_account.name == "Name"
    assert pay_account.user_ids == [2]
    assert pay_account.is_enabled is False
    assert pay_account.weight == 2
