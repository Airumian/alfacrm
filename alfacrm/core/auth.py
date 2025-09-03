import time

import aiohttp as aiohttp

from .utils import check_response, make_url

# Default token lifetime 14 minutes
DEFAULT_LIFETIME = 60 * 14
AUTH_HEADER_FIELD = "X-ALFACRM-TOKEN"


class Token:
    """Class for storage token info"""

    def __init__(self, value: str, expired_at: float):
        self.value = value
        self.expired_at = expired_at

    def is_expired(self) -> bool:
        return self.expired_at <= time.time()


class AuthManager:
    """Class for work with authentification in AlfaCRM"""

    def __init__(
        self,
        email: str,
        api_key: str,
        hostname: str,
        session: aiohttp.ClientSession,
        token_lifetime: int = DEFAULT_LIFETIME,
    ):
        """
        :param email: API User email
        :param api_key: API User api key
        :param hostname: user url
        :param session: aiohttp session
        :param token_lifetime: token lifetime
        """
        self._hostname = hostname
        self._email = email
        self._api_key = api_key
        self._session = session
        self._token_lifetime = token_lifetime
        self._token = Token("", 0)  # Empty token

    async def _get_token(self) -> Token:
        """
        Call auth api and get auth token token
        :return:
        """
        payload = {"email": self._email, "api_key": self._api_key}
        auth_url = make_url(self._hostname, "auth/login")
        async with self._session.post(auth_url, json=payload) as response:
            data = check_response(
                response.status, await response.text(), response.request_info
            )
            self._token = data["token"]
            return Token(
                value=data["token"],
                expired_at=time.time() + self._token_lifetime,
            )

    async def refresh_token(self):
        """
        Refrech auth token
        :return:
        """
        new_token = await self._get_token()
        self._token = new_token

    async def get_token(self) -> Token:
        """
        Get token with auto refresh
        :return:
        """
        # Update token if it expired
        if self._token.is_expired():
            await self.refresh_token()
        return self._token

    async def get_auth_headers(self) -> dict[str, str]:
        """
        Make auth header
        :return: auth header
        """

        token = await self.get_token()

        return {AUTH_HEADER_FIELD: token.value}

    @property
    def token(self) -> Token:
        return self._token
