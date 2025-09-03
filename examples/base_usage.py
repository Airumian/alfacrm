import asyncio

from alfacrm import AlfaClient  # Import client for work with alfacrm api
from alfacrm.entities import Customer  # Import customer entity class

HOSTNAME = "demo.s20.online"
EMAIL = "api-email@email.example"
API_KEY = "user-api-token"
BRANCH_ID = 12

HOSTNAME = "ligarobotov.s20.online"
EMAIL = "dev-delta-nsk@ligarobotov.ru"
API_KEY = "07ec70a0-d2e9-11ea-a4f7-0cc47ae3c526"
BRANCH_ID = 12

EMAIL = "alfa-api@ligarobotov.ru"
API_KEY = "3bb0672c-85f5-11e8-8a06-d8cb8abf9305"


async def main():
    # Create AlfaClient object
    client = AlfaClient(
        hostname=HOSTNAME,
        email=EMAIL,
        api_key=API_KEY,
        branch_id=BRANCH_ID,
    )
    try:
        # Check auth (Optionaly)
        if not await client.check_auth():
            raise RuntimeError("Auth error")

        # Get list of entities
        customers = await client.customer.list()
        # Get one row by id
        customer = await client.customer.get(id_=5013)

        # Create new entity
        new_customer = Customer(
            name="Customer",
            email=["customer@email.email"],
            branch_ids=[12],
            is_study=True,
            legal_type=1,
        )
        # Create model in alfacrm
        created_customer = await client.customer.save(new_customer)
        print(created_customer.id)  # Seted id from alfa crm

        created_customer.name = "Edited customer"
        # Update model in alfacrm
        update_customer = await client.customer.save(created_customer)
    finally:
        # Close session
        await client.close()


if __name__ == "__main__":
    # Run async main with asyncio
    asyncio.run(main())
