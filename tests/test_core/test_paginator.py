from typing import List, Optional

import pytest

from alfacrm import fields
from alfacrm.core import EntityManager, Page, Paginator
from alfacrm.core.entity import BaseAlfaEntity


class EntityManagerClass(EntityManager):
    object_name = "customer"


class BaseAlfaEntityClass(BaseAlfaEntity):
    id: Optional[int] = fields.Integer()
    field1: Optional[int] = fields.Integer()


def add_auth_request(aresponses):
    aresponses.add(
        "demo.s20.online", "/v2api/auth/login", "POST", {"token": "api-token"}
    )


def test_init_page():
    page = Page(
        number=1,
        items=[1, 2, 3],
        total=10,
    )

    assert page.number == 1
    assert page.items == [1, 2, 3]
    assert page.total == 10


def test_init_paginator(aresponses, api_client):
    manager = EntityManagerClass(
        api_client,
        entity_class=BaseAlfaEntityClass,
    )

    paginator = Paginator(
        alfa_object=manager,
        start_page=0,
        page_size=20,
    )

    assert paginator._object == manager
    assert paginator._page_number == 0
    assert paginator._page_size == 20
    assert paginator._page is None
    assert paginator._total == 0


@pytest.mark.asyncio
async def test_paginator(aresponses, api_client):
    add_auth_request(aresponses)
    aresponses.add(
        "demo.s20.online",
        "/v2api/1/customer/index",
        "POST",
        {"total": 3, "count": 1, "page": 0, "items": [{"id": 1, "field1": 1}]},
        body_pattern='{"page": 0}',
    )
    aresponses.add(
        "demo.s20.online",
        "/v2api/1/customer/index",
        "POST",
        {"total": 3, "count": 1, "page": 1, "items": [{"id": 2, "field1": 2}]},
        body_pattern='{"page": 1}',
    )
    aresponses.add(
        "demo.s20.online",
        "/v2api/1/customer/index",
        "POST",
        {"total": 3, "count": 1, "page": 2, "items": [{"id": 3, "field1": 3}]},
        body_pattern='{"page": 2}',
    )

    crud_object = EntityManagerClass(
        api_client,
        entity_class=BaseAlfaEntityClass,
    )

    paginator: Paginator[BaseAlfaEntityClass] = Paginator(
        alfa_object=crud_object,
        start_page=0,
        page_size=1,
    )
    all_pages: List[Page[BaseAlfaEntityClass]] = []
    async for page in paginator:
        all_pages.append(page)

    assert paginator.total_page == 3

    assert len(all_pages) == 3
    assert all_pages[0].total == 3
    assert all_pages[0].number == 0
    assert all_pages[0].items == [BaseAlfaEntityClass(id=1, field1=1)]

    assert all_pages[1].total == 3
    assert all_pages[1].number == 1
    assert all_pages[1].items == [BaseAlfaEntityClass(id=2, field1=2)]

    assert all_pages[2].total == 3
    assert all_pages[2].number == 2
    assert all_pages[2].items == [BaseAlfaEntityClass(id=3, field1=3)]
