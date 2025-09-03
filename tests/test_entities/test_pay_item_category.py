from alfacrm.entities import PayItemCategory


def test_pay_item_category():
    pay_item_category = PayItemCategory(
        id=1,
        name="Name",
        weight=3,
    )

    assert pay_item_category.id == 1
    assert pay_item_category.name == "Name"
    assert pay_item_category.weight == 3
