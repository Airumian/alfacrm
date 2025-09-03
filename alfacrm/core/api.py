import typing
from enum import Enum

import aiohttp

from .auth import AuthManager
from .utils import check_response, make_url


class ApiMethod(Enum):
    LIST = "index"
    CREATE = "create"
    UPDATE = "update"


class ApiClient:
    """Class for work with API"""

    def __init__(
        self,
        hostname: str,
        branch_id: int,
        auth_manager: AuthManager,
        session: aiohttp.ClientSession,
    ):
        self._hostname = hostname
        self._auth_manager = auth_manager
        self._session = session
        self._branch_id = branch_id

    def get_url_for_method(self, object_name: str, method: str) -> str:
        api_method = f"{object_name}/{method}"
        return make_url(self._hostname, api_method, self._branch_id)

    async def request(
        self,
        url: str,
        json: typing.Optional[typing.Dict[str, typing.Any]] = None,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
    ):
        """
        Request on API
        :param url: URL
        :param json: json data
        :param params: url dict_
        :return: response
        """
        headers = await self._auth_manager.get_auth_headers()
        async with self._session.post(
            url, json=json, params=params, headers=headers
        ) as response:
            return check_response(
                response.status, await response.text(), response.request_info
            )
