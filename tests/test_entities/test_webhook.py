import datetime

from alfacrm.entities import Webhook


def test_init_webhook():
    webhook = Webhook(
        branch_id=1,
        event="create",
        entity="Pay",
        entity_id=2,
        fields_old=[],  # noqa
        fields_new={
            "customer_id": 3,
        },
        fields_rel=[],  # noqa
        user_id=5,
        datetime=datetime.datetime(2021, 1, 1, 15, 1, 1),
    )

    assert webhook.branch_id == 1
    assert webhook.event == "create"
    assert webhook.entity == "Pay"
    assert webhook.entity_id == 2
    assert webhook.fields_old == {}
    assert webhook.fields_new == {"customer_id": 3}
    assert webhook.fields_rel == {}
    assert webhook.user_id == 5
    assert webhook.datetime == datetime.datetime(2021, 1, 1, 15, 1, 1)
