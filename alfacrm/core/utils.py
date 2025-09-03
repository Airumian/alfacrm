import json as json_
import re
import typing

import aiohttp

from .exceptions import ApiException, BadRequest, Forbidden, NotFound, Unauthorized

HOSTNAME_REGEX = re.compile(
    r"^(?:https://|http://)?([\w]*)(?:\.s20\.online)?[\w/0_-]*$"
)


def make_url(hostname: str, api_method: str, branch_id: int = 0) -> str:
    """
    Make url for api call
    :param hostname: hostname
    :param api_method: api method
    :param branch_id: branch id
    :return: full url
    """
    if branch_id:
        return f"https://{hostname}/v2api/{branch_id}/{api_method}"
    else:
        return f"https://{hostname}/v2api/{api_method}"


def check_response(
    code: int, body: str, request_info: typing.Optional[aiohttp.RequestInfo] = None
) -> typing.Dict[str, typing.Any]:
    """
    Check response
    :param code: response code
    :param request_info: request info
    :param body: response text
    :return: checked response
    """
    if code >= 500:
        raise ApiException(message=body, request_info=request_info)

    try:
        json_response = json_.loads(body)
    except ValueError:
        json_response = {}
    is_ok = True

    if "errors" in json_response and json_response.get("errors"):
        code = 400

    error_msg = json_response.get("errors") or json_response.get("message") or body

    if code == 400:
        raise BadRequest(request_info=request_info, message=error_msg)
    if code == 401:
        raise Unauthorized(request_info=request_info, message=error_msg)
    if code == 403:
        raise Forbidden(request_info=request_info, message=error_msg)
    if code == 404:
        raise NotFound(request_info=request_info, message=error_msg)

    return json_response


def prepare_dict(
    dict_: typing.Optional[typing.Dict[str, typing.Any]],
) -> typing.Dict[str, typing.Any]:
    """
    Prepare dict for request
    :param dict_: dict for prepare
    :return: prepared dict
    """

    if dict_ is None:
        dict_ = {}
    else:
        dict_ = {name: value for name, value in dict_.items() if value is not None}

    return dict_


def parse_hostname(raw_hostname: str) -> str:
    """
    Parse hostname from raw string

    Examples:
    https://hostname.s20.online -> hostname.s20.online
    hostname.s20.online -> hostname.s20.online
    https://hostname.s20.online/ -> hostname.s20.online
    hostname -> hostname.s20.online
    https://hostname.s20.online/api/* -> hostname.s20.online

    :param raw_hostname: raw hostname string
    :return: parsed hostname
    """
    result = HOSTNAME_REGEX.search(raw_hostname)
    if not result:
        raise ValueError(f"<{raw_hostname}> is not valid AlfaCRM hostname")

    base_hostname = result.group(1)
    return f"{base_hostname}.s20.online"
