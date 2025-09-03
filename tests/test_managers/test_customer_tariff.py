import datetime

import pytest

from alfacrm import entities, managers
from tests.conftest import DEFAULT_BRANCH_ID, DEFAULT_HOST, make_response

CUSTOMER_TARIFF_RESPONSE = {
    "page": 0,
    "total": 1,
    "count": 1,
    "items": [
        {
            "id": 1,
            "customer_id": 2,
            "tariff_id": 3,
            "subject_ids": [4],
            "lesson_type_ids": [
                5,
                6,
            ],
            "is_separate_balance": 1,
            "balance": "1024.00",
            "paid_count": 1,
            "paid_till": None,
            "note": "Note",
            "b_date": "01.01.2021",
            "e_date": "01.01.2022",
            "paid_lesson_count": 1,
        }
    ],
}


@pytest.fixture
def customer_tariff_manager(api_client):
    return managers.CustomerTariff(
        api_client=api_client,
        entity_class=entities.CustomerTariff,
    )


@pytest.mark.asyncio
async def test_list_customer_tariff_manager(
    aresponses,
    customer_tariff_manager: managers.CustomerTariff[entities.CustomerTariff],
):
    aresponses.add(
        DEFAULT_HOST,
        f"/v2api/{DEFAULT_BRANCH_ID}/customer-tariff/index?customer_id=1&per-page=100",
        "POST",
        CUSTOMER_TARIFF_RESPONSE,
        match_querystring=True,
    )

    with pytest.raises(ValueError) as context:
        await customer_tariff_manager.list()

    assert str(context.value) == "customer_id is not filled"

    customer_tariffs = await customer_tariff_manager.list(
        customer_id=1,
    )

    assert len(customer_tariffs) == 1

    customer_tariff = customer_tariffs[0]

    check_customer_tariff(customer_tariff)


@pytest.mark.asyncio
async def test_get_customer_tariff_manager(
    aresponses,
    customer_tariff_manager: managers.CustomerTariff[entities.CustomerTariff],
):
    aresponses.add(
        DEFAULT_HOST,
        f"/v2api/{DEFAULT_BRANCH_ID}/customer-tariff/index?customer_id=1&per-page=100",
        "POST",
        CUSTOMER_TARIFF_RESPONSE,
        body_pattern='{"id": 1}',
        match_querystring=True,
    )

    with pytest.raises(ValueError) as context:
        await customer_tariff_manager.get(id_=1)

    assert str(context.value) == "customer_id is not filled"

    customer_tariff = await customer_tariff_manager.get(
        customer_id=1,
        id_=1,
    )
    check_customer_tariff(customer_tariff)


@pytest.mark.asyncio
async def test_save_customer_tariff_manager(
    aresponses,
    customer_tariff_manager: managers.CustomerTariff[entities.CustomerTariff],
):
    aresponses.add(
        DEFAULT_HOST,
        f"/v2api/{DEFAULT_BRANCH_ID}/customer-tariff/create?customer_id=2",
        "POST",
        make_response(model={"id": 1, "customer_id": 2}),
        body_pattern="{}",
        match_querystring=True,
    )
    (
        aresponses.add(
            DEFAULT_HOST,
            f"/v2api/{DEFAULT_BRANCH_ID}/customer-tariff/update?customer_id=2&id=1",
            "POST",
            make_response(model={"id": 1, "customer_id": 2}),
            match_querystring=True,
        ),
    )

    customer_tariff = entities.CustomerTariff()

    created_customer_tariff = await customer_tariff_manager.save(
        customer_tariff, customer_id=2
    )
    assert created_customer_tariff.id == 1

    updated_customer_tariff = await customer_tariff_manager.save(
        created_customer_tariff, customer_id=2
    )
    assert updated_customer_tariff.id == 1


def check_customer_tariff(customer_tariff: entities.CustomerTariff):
    assert customer_tariff.id == 1
    assert customer_tariff.customer_id == 2
    assert customer_tariff.tariff_id == 3
    assert customer_tariff.subject_ids == [4]
    assert customer_tariff.lesson_type_ids == [5, 6]
    assert customer_tariff.is_separate_balance is True
    assert customer_tariff.balance == 1024.0
    assert customer_tariff.paid_till is None
    assert customer_tariff.note == "Note"
    assert customer_tariff.b_date == datetime.date(2021, 1, 1)
    assert customer_tariff.e_date == datetime.date(2022, 1, 1)
    assert customer_tariff.paid_lesson_count == 1
