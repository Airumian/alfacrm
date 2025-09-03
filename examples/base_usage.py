import asyncio
import os

from alfacrm import AlfaClient

ALFACRM_API_KEY = os.getenv("ALFACRM_API_KEY")
ALFACRM_EMAIL = os.getenv("ALFACRM_EMAIL")
ALFACRM_BASE_URL = os.getenv("ALFACRM_BASE_URL")
ALFACRM_DEFAULT_BRANCH_ID = 1


async def main():
    client = AlfaClient(
        hostname=ALFACRM_BASE_URL,
        email=ALFACRM_EMAIL,
        api_key=ALFACRM_API_KEY,
        branch_id=ALFACRM_DEFAULT_BRANCH_ID,
    )
    try:
        await client.check_auth()
        print(await client.lesson.get(1))
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
