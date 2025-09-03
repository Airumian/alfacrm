import pathlib
import sys
from typing import Any, Optional

import aiohttp
import pytest

from alfacrm.core import ApiClient, AuthManager

root_dir = pathlib.Path(".").resolve()
sys.path.append(str(root_dir))


DEFAULT_HOST = "demo.s20.online"
DEFAULT_EMAIL = "test@test.test"
DEFAULT_API_KEY = "api-key"
DEFAULT_BRANCH_ID = 1


def make_response(
    success: bool = True,
    errors: Optional[list[str]] = None,
    model: dict[str, Any] = None,
) -> dict:
    if errors is None:
        errors = []
    if model is None:
        model = {}

    return {"success": success, "errors": errors, "model": model}


@pytest.fixture
@pytest.mark.asyncio
async def session():
    session = aiohttp.ClientSession()
    yield session
    await session.close()


@pytest.fixture(autouse=True)
def add_auth_request(aresponses):
    aresponses.add(
        "demo.s20.online",
        "/v2api/auth/login",
        "POST",
        {"token": "api-token"},
    )


@pytest.fixture
def auth_manager(session):
    return AuthManager(
        email=DEFAULT_EMAIL,
        api_key=DEFAULT_API_KEY,
        hostname=DEFAULT_HOST,
        session=session,
    )


@pytest.fixture
def api_client(auth_manager: AuthManager, session):
    return ApiClient(
        hostname=DEFAULT_HOST,
        branch_id=DEFAULT_BRANCH_ID,
        auth_manager=auth_manager,
        session=session,
    )
