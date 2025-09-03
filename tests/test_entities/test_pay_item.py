from alfacrm.entities import PayItem


def test_init_pay_item():
    pay_item = PayItem(
        id=1,
        branch_ids=[1, 2],
        category_id=1,
        pay_type_ids=[2, 3],
        name="Name",
        weight=1,
    )

    assert pay_item.id == 1
    assert pay_item.branch_ids == [1, 2]
    assert pay_item.category_id == 1
    assert pay_item.pay_type_ids == [2, 3]
    assert pay_item.name == "Name"
    assert pay_item.weight == 1
