from unittest.mock import MagicMock, patch

import pytest

from alfacrm.core.auth import AUTH_HEADER_FIELD, AuthManager


@pytest.mark.asyncio
async def test_init(aresponses, session):
    auth_manager = AuthManager(
        email="test@test.test",
        api_key="api-key",
        hostname="demo.s20.online",
        session=session,
        token_lifetime=15,
    )

    assert auth_manager._email == "test@test.test"
    assert auth_manager._api_key == "api-key"
    assert auth_manager._token_lifetime == 15
    # Prevent warning
    await session.close()


@pytest.mark.asyncio
async def test_refresh_token(aresponses, auth_manager, session):
    aresponses.add(
        "demo.s20.online", "/v2api/auth/login", "post", {"token": "api-token"}
    )
    await auth_manager.refresh_token()
    assert auth_manager._token.value == "api-token"
    await session.close()


@pytest.mark.asyncio
async def test_auto_refresh_token(aresponses, session):
    aresponses.add(
        "auth.s20.online", "/v2api/auth/login", "post", {"token": "first-api-token"}
    )
    aresponses.add(
        "auth.s20.online", "/v2api/auth/login", "post", {"token": "second-api-token"}
    )

    auth_manager = AuthManager(
        email="test@test.test",
        api_key="api-key",
        hostname="auth.s20.online",
        session=session,
        token_lifetime=15,
    )

    assert auth_manager._token.value == ""
    with patch("time.time", MagicMock(return_value=0)):
        await auth_manager.get_token()
        assert auth_manager.token.value == "first-api-token"
        assert auth_manager.token.expired_at == 15

    with patch("time.time", return_value=20):
        await auth_manager.get_token()
        assert auth_manager.token.value == "second-api-token"
        assert auth_manager.token.expired_at == 35


@pytest.mark.asyncio
async def test_get_auth_headers(aresponses, auth_manager):
    aresponses.add(
        "demo.s20.online", "/v2api/auth/login", "post", {"token": "api-token"}
    )

    await auth_manager.refresh_token()

    headers = await auth_manager.get_auth_headers()

    assert headers == {AUTH_HEADER_FIELD: "api-token"}
