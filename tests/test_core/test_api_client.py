from typing import Optional

import aiohttp
import pytest

from alfacrm.core import ApiClient, AuthManager


def test_init_api_client(auth_manager: AuthManager, session):
    api_client = ApiClient(
        hostname="demo.s20.online",
        branch_id=1,
        auth_manager=auth_manager,
        session=session,
    )

    assert api_client._hostname == "demo.s20.online"
    assert api_client._branch_id == 1
    assert api_client._auth_manager == auth_manager
    assert api_client._session == session


@pytest.mark.parametrize(
    "hostname,branch_id,object_name,method,result",
    [
        (
            "demo.s20.online",
            None,
            "customer",
            "update",
            "https://demo.s20.online/v2api/customer/update",
        ),
        (
            "test.s20.online",
            1,
            "location",
            "create",
            "https://test.s20.online/v2api/1/location/create",
        ),
    ],
)
def test_get_url_for_method(
    auth_manager: AuthManager,
    hostname: str,
    branch_id: Optional[int],
    object_name: str,
    method: str,
    result: str,
    session,
):
    api_client = ApiClient(
        hostname=hostname,
        branch_id=branch_id,
        auth_manager=auth_manager,
        session=session,
    )
    result_url = api_client.get_url_for_method(object_name, method)
    assert result_url == result


@pytest.mark.asyncio
async def test_request(aresponses, auth_manager, session):
    aresponses.add(
        "demo.s20.online", "/v2api/auth/login", "POST", {"token": "api-token"}
    )
    aresponses.add(
        "demo.s20.online",
        "/v2api/1/location/index",
        "POST",
        {"message": "ok"},
        body_pattern='{"param2": 2}',
    )

    api_client = ApiClient(
        hostname="demo.s20.online",
        branch_id=1,
        auth_manager=auth_manager,
        session=session,
    )
    request_url = api_client.get_url_for_method("location", "index")
    response_json = await api_client.request(request_url, json={"param2": 2})

    assert response_json == {"message": "ok"}
