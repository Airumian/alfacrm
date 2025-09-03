# Alfacrm

**Alfacrm** - is an asynchronous implementation for the [AlfaCRM API](https://alfacrm.pro/rest-api)

## Package is in development

## Installation using pip

```ini
pip install alfacrm
```

*Example:*

```python
import asyncio
from aioalfacrm import AlfaClient
from aioalfacrm.entities import Location

HOSTNAME = 'demo.s20.online'
EMAIL = 'api-email@email.example'
API_KEY = 'user-api-token'
BRANCH_ID = 1


async def main():
    alfa_client = AlfaClient(
        hostname=HOSTNAME,
        email=EMAIL,
        api_key=API_KEY,
        branch_id=BRANCH_ID,
    )
    try:
        # Check auth (Optionaly)
        if not await alfa_client.check_auth():
            print('Authentification error')
            return
        # Get branches
        branches = await alfa_client.branch.list(page=0, count=20)

        # Edit branch
        for branch in branches:
            branch.name = f'{branch.name} - Edited'
            # Save branch
            await alfa_client.branch.save(branch)

        # Create location
        location = Location(
            branch_id=1,
            is_active=True,
            name='New location',
        )
        await alfa_client.location.save(location)

    finally:
        # Close session
        await alfa_client.close()


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # For Windows
asyncio.run(main())


```

## Paginator

```python
# Get all entities
for page in alfa_client. < object >.get_paginator():
    objects = page.items
```

## Custom fields

To work with custom fields, do the following

```python
from aioalfacrm import entities
from aioalfacrm import fields
from typing import Optional


# Extend existing model
class CustomCustomer(entities.Customer):
    custom_field: Optional[int] = fields.Integer()

    # For IDE init support
    def __init__(
            self,
            custom_field: Optional[int] = None,
            *args,
            **kwargs,
    ):
        super(CustomCustomer, self).__init__(custom_field=custom_field, *args, **kwargs)


# Create custom alfa client with new model
from aioalfacrm import AlfaClient
from aioalfacrm import managers


class CustomAlfaClient(AlfaClient):

    def __init__(self, *args, **kwargs):
        super(CustomAlfaClient, self).__init__(*args, **kwargs)

        self.customer = managers.Customer(
            api_client=self.api_client,
            entity_class=CustomCustomer,
        )


# Create custom alfa client
import asyncio

HOSTNAME = 'demo.s20.online'
EMAIL = 'api-email@email.example'
API_KEY = 'user-api-token'
BRANCH_ID = 1


async def main():
    alfa_client = CustomAlfaClient(hostname=HOSTNAME, email=EMAIL, api_key=API_KEY, branch_id=BRANCH_ID)
    try:
        customers = await alfa_client.customer.list()
        for customer in customers:
            print(customer.custom_field)
    finally:
        await alfa_client.close()


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # For Windows
asyncio.run(main())
```
