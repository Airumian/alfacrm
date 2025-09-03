import datetime

from alfacrm.entities import Pay


def test_init_pay():
    pay = Pay(
        id=1,
        branch_id=2,
        location_id=3,
        customer_id=4,
        pay_type_id=5,
        pay_account_id=6,
        pay_item_id=7,
        teacher_id=8,
        commodity_id=9,
        ctt_id=10,
        document_date=datetime.date(2021, 1, 1),
        income=701.1,
        payer_name="Payer Name",
        note="Note",
        is_confirmed=False,
        custom_md_order="custom md order",
        custom_order_description="custom order desciption",
    )

    assert pay.id == 1
    assert pay.branch_id == 2
    assert pay.location_id == 3
    assert pay.customer_id == 4
    assert pay.pay_type_id == 5
    assert pay.pay_account_id == 6
    assert pay.pay_item_id == 7
    assert pay.teacher_id == 8
    assert pay.commodity_id == 9
    assert pay.ctt_id == 10
    assert pay.document_date == datetime.date(2021, 1, 1)
    assert pay.income == 701.1
    assert pay.payer_name == "Payer Name"
    assert pay.note == "Note"
    assert pay.is_confirmed is False
    assert pay.custom_md_order == "custom md order"
    assert pay.custom_order_description == "custom order desciption"
