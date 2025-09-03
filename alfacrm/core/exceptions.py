import aiohttp


class AlfaException(Exception):
    def __init__(self, message: str):
        self._message = message

    def __str__(self) -> str:
        return self._message


class ApiException(AlfaException):
    code = 500

    def __init__(self, request_info: aiohttp.RequestInfo | None = None, **kwargs):
        super(ApiException, self).__init__(**kwargs)
        self._request_info = request_info

    def __str__(self):
        request_info_msg = str(self._request_info) if self._request_info else ""
        return f"Code: {self.code} - {self._message} {request_info_msg}"


class BadRequest(ApiException):
    code = 400


class Unauthorized(ApiException):
    code = 401


class Forbidden(ApiException):
    code = 403


class NotFound(ApiException):
    code = 404


class MethodNotAllowed(ApiException):
    code = 405
