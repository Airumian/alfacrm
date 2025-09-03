import datetime

from alfacrm.entities import Discount


def test_init_discount():
    discount = Discount(
        id=1,
        branch_id=2,
        customer_id=3,
        discount_type=4,
        amount=100,
        note="Note",
        subject_ids=[2],
        lesson_type_ids=[3],
        begin=datetime.date(2021, 1, 1),
        end=datetime.date(2022, 1, 1),
    )

    assert discount.id == 1
    assert discount.branch_id == 2
    assert discount.customer_id == 3
    assert discount.discount_type == 4
    assert discount.amount == 100
    assert discount.note == "Note"
    assert discount.subject_ids == [2]
    assert discount.lesson_type_ids == [3]
    assert discount.begin == datetime.date(2021, 1, 1)
    assert discount.end == datetime.date(2022, 1, 1)
