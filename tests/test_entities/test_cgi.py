import datetime

from alfacrm.entities import CGI


def test_init_cgi():
    cgi = CGI(
        id=1,
        customer_id=2,
        group_id=3,
        b_date=datetime.date(2021, 1, 1),
        e_date=datetime.date(2022, 1, 1),
    )

    assert cgi.id == 1
    assert cgi.customer_id == 2
    assert cgi.group_id == 3
    assert cgi.b_date == datetime.date(2021, 1, 1)
    assert cgi.e_date == datetime.date(2022, 1, 1)
