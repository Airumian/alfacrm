import asyncio

from alfacrm import AlfaClient, managers
from alfacrm.entities import Customer

HOSTNAME = "demo.s20.online"
EMAIL = "api-email@email.example"
API_KEY = "user-api-token"
BRANCH_ID = 1


# Extend existing model
class CustomCustomer(Customer):
    custom_field: int | None

    # For IDE init support
    def __init__(self, custom_field: int | None = None, *args, **kwargs):
        super(CustomCustomer, self).__init__(custom_field=custom_field, *args, **kwargs)


# Create custom alfa client with new model


class CustomAlfaClient(AlfaClient):
    def __init__(self, *args, **kwargs):
        super(CustomAlfaClient, self).__init__(*args, **kwargs)

        self.customer = managers.Customer(
            api_client=self.api_client,
            model_class=CustomCustomer,
        )


# Create custom alfa client


async def main():
    alfa_client = CustomAlfaClient(
        hostname=HOSTNAME,
        email=EMAIL,
        api_key=API_KEY,
        branch_id=BRANCH_ID,
    )
    try:
        customers = await alfa_client.customer.list()
        for customer in customers:
            print(customer.custom_field)
    finally:
        await alfa_client.close()


asyncio.run(main())
