import pytest

try:
    from unittest.mock import AsyncMock as CoroutineMock
    from unittest.mock import patch
except ImportError:
    from asynctest import CoroutineMock, patch

from alfacrm import AlfaClient


def add_auth_request(aresponses):
    aresponses.add(
        "demo.s20.online", "/v2api/auth/login", "POST", {"token": "api-token"}
    )


@pytest.mark.asyncio
async def test_init(session):
    client = AlfaClient(
        hostname="demo.s20.online",
        email="test@test.example",
        api_key="api-key",
        branch_id=1,
        session=session,
    )
    assert client.hostname == "demo.s20.online"
    assert client.email == "test@test.example"
    assert client.api_key == "api-key"
    assert client.branch_id == 1
    assert client._session == session


@pytest.mark.asyncio
async def test_close(session):
    client = AlfaClient(
        hostname="demo.s20.online",
        email="test@test.example",
        api_key="api_key",
        branch_id=1,
        session=session,
    )

    with patch(
        "aiohttp.ClientSession.close", new_callable=CoroutineMock
    ) as mocked_close:
        await client.close()
        mocked_close.assert_awaited()


@pytest.mark.asyncio
async def test_auth(aresponses):
    add_auth_request(aresponses)
    client = AlfaClient(
        hostname="demo.s20.online",
        email="test@test.example",
        api_key="api_key",
        branch_id=1,
    )

    await client.auth()
    assert client.auth_manager.token.value == "api-token"

    await client.close()


@pytest.mark.asyncio
async def test_correct_check_auth(aresponses, session):
    aresponses.add(
        "auth.s20.online",
        "/v2api/auth/login",
        "POST",
        response=aresponses.Response(
            status=403,
            body="{'name': 'Forbidden', 'message': 'Not Authorized', 'code': 0, 'status': 403}",
        ),
    )
    client = AlfaClient(
        hostname="auth.s20.online",
        email="test@test.example",
        api_key="api_key",
        branch_id=1,
        session=session,
    )

    assert await client.check_auth() is False


@pytest.mark.asyncio
async def test_incorrect_check_auth(aresponses, session):
    add_auth_request(aresponses)
    client = AlfaClient(
        hostname="demo.s20.online",
        email="test@test.example",
        api_key="api_key",
        branch_id=1,
        session=session,
    )

    assert await client.check_auth() is True
