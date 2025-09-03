from alfacrm.core.exceptions import AioAlfaException, ApiException


def test_init_aio_alfa_exception():
    exception = AioAlfaException(
        message="Exception message",
    )

    assert exception._message == "Exception message"

    assert str(exception) == "Exception message"


def test_init_api_exception():
    exception = ApiException(
        message="Exception message",
        request_info="Fake request info",  # noqa
    )

    assert exception.code == 500
    assert exception._message == "Exception message"
    assert exception._request_info == "Fake request info"

    assert str(exception) == "Code: 500 - Exception message Fake request info"
