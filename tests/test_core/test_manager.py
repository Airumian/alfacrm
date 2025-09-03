import typing
from typing import Optional

import pytest

from alfacrm import fields
from alfacrm.core.entity import BaseAlfaEntity
from alfacrm.core.entity_manager import BaseManager, EntityManager
from alfacrm.core.exceptions import NotFound


class BaseManagerClass(BaseManager):
    object_name = "customer"


class EntityManagerClass(EntityManager):
    object_name = "customer"


T = typing.TypeVar("T")


class EntityManagerWithUrlParams(EntityManager, typing.Generic[T]):
    object_name = "customer-tariff"

    async def list(
        self, field1: int = 0, page: int = 0, count: int = 100, **kwargs
    ) -> typing.List[T]:
        result = await self._list(
            page=page, count=count, params={"field1": field1}, **kwargs
        )

        return self._result_to_entities(result)

    async def get(
        self,
        id_: int,
        field1: int = 0,
    ) -> T:
        result = await self._get(
            id_=id_,
            params={
                "field1": field1,
            },
        )

        return self._result_to_entity(result)


class BaseAlfaEntityClass(BaseAlfaEntity):
    id: Optional[int] = fields.Integer()
    field1: Optional[int] = fields.Integer()


@pytest.mark.asyncio
async def test_base_manager_list(api_client, aresponses):
    aresponses.add(
        "demo.s20.online",
        "/v2api/1/customer/index",
        "POST",
        {"total": 10, "count": 1, "page": 1, "items": [{"field1": 1}]},
        body_pattern='{"page": 1}',
    )
    a = BaseManagerClass(
        api_client=api_client,
    )

    data = await a._list(page=1, count=1)
    assert data == {"total": 10, "count": 1, "page": 1, "items": [{"field1": 1}]}


@pytest.mark.asyncio
async def test_base_manager_get(api_client, aresponses):
    aresponses.add(
        "demo.s20.online",
        "/v2api/1/customer/index",
        "POST",
        {"total": 1, "count": 1, "page": 0, "items": [{"field1": 1}]},
        body_pattern='{"id": 2}',
    )

    aresponses.add(
        "demo.s20.online",
        "/v2api/1/customer/index",
        "POST",
        {"total": 0, "count": 0, "page": 0, "items": []},
        body_pattern='{"id": 3}',
    )

    a = BaseManagerClass(api_client=api_client)

    data = await a._get(id_=2)
    assert data == {"field1": 1}

    with pytest.raises(NotFound):
        await a._get(id_=3)


@pytest.mark.asyncio
async def test_base_manager_update(api_client, aresponses):
    aresponses.add(
        "demo.s20.online",
        "/v2api/1/customer/update",
        "POST",
        {"success": True, "errors": [], "model": {"id": 2, "field1": 2}},
        body_pattern='{"field1": 2}',
    )

    a = BaseManagerClass(api_client=api_client)

    data = await a._update(id_=2, field1=2)
    assert data == {"id": 2, "field1": 2}


@pytest.mark.asyncio
async def test_base_manager_create(api_client, aresponses):
    aresponses.add(
        "demo.s20.online",
        "/v2api/1/customer/create",
        "POST",
        {"success": True, "errors": [], "model": {"id": 3, "field1": 10}},
        body_pattern='{"field1": 10}',
    )

    a = BaseManagerClass(
        api_client=api_client,
    )
    data = await a._create(field1=10)
    assert data == {"id": 3, "field1": 10}


@pytest.mark.asyncio
async def test_base_manager_save(api_client, aresponses):
    aresponses.add(
        "demo.s20.online",
        "/v2api/1/customer/create",
        "POST",
        {"success": True, "errors": [], "model": {"id": 4, "field1": 11}},
        body_pattern='{"field1": 11}',
    )
    aresponses.add(
        "demo.s20.online",
        "/v2api/1/customer/update",
        "POST",
        {"success": True, "errors": [], "model": {"id": 4, "field1": 12}},
        body_pattern='{"field1": 12}',
    )

    a = BaseManagerClass(
        api_client=api_client,
    )

    new_customer = await a._save(field1=11)
    assert new_customer == {"id": 4, "field1": 11}
    new_customer["field1"] = 12
    updated_customer = await a._save(**new_customer)
    assert updated_customer == {"id": 4, "field1": 12}


@pytest.mark.asyncio
async def test_manager_list(api_client, aresponses):
    aresponses.add(
        "demo.s20.online",
        "/v2api/1/customer/index?per-page=1",
        "POST",
        {"total": 10, "count": 1, "page": 1, "items": [{"id": 1, "field1": 1}]},
        body_pattern='{"page": 1}',
        match_querystring=True,
    )

    a = EntityManagerClass(
        api_client=api_client,
        entity_class=BaseAlfaEntityClass,
    )

    customers = await a.list(page=1, count=1)
    assert len(customers) == 1
    customer = customers[0]
    assert customer.serialize() == {"id": 1, "field1": 1}


@pytest.mark.asyncio
async def test_manager_get(api_client, aresponses):
    aresponses.add(
        "demo.s20.online",
        "/v2api/1/customer/index",
        "POST",
        {"total": 1, "count": 1, "page": 0, "items": [{"id": 2, "field1": 1}]},
        body_pattern='{"id": 2}',
    )

    aresponses.add(
        "demo.s20.online",
        "/v2api/1/customer/index",
        "POST",
        {"total": 0, "count": 0, "page": 0, "items": []},
        body_pattern='{"id": 3}',
    )

    a = EntityManagerClass(
        api_client=api_client,
        entity_class=BaseAlfaEntityClass,
    )

    customer = await a.get(2)
    assert customer.serialize() == {"id": 2, "field1": 1}
    with pytest.raises(NotFound):
        await a.get(3)


@pytest.mark.asyncio
async def test_manager_save(api_client, aresponses):
    aresponses.add(
        "demo.s20.online",
        "/v2api/1/customer/create",
        "POST",
        {"success": True, "errors": [], "model": {"id": 4, "field1": 11}},
        body_pattern='{"field1": 11}',
    )
    aresponses.add(
        "demo.s20.online",
        "/v2api/1/customer/update",
        "POST",
        {"success": True, "errors": [], "model": {"id": 4, "field1": 12}},
        body_pattern='{"field1": 12}',
    )
    a = EntityManagerClass(
        api_client=api_client,
        entity_class=BaseAlfaEntityClass,
    )

    new_customer = BaseAlfaEntityClass(
        field1=11,
    )

    created_customer = await a.save(new_customer)
    assert created_customer.serialize() == {"id": 4, "field1": 11}
    created_customer.field1 = 12
    updated_customer = await a.save(created_customer)
    assert updated_customer.serialize() == {"id": 4, "field1": 12}


@pytest.mark.asyncio
async def test_manager_page(api_client, aresponses):
    aresponses.add(
        "demo.s20.online",
        "/v2api/1/customer/index",
        "POST",
        {
            "total": 10,
            "count": 2,
            "page": 1,
            "items": [{"id": 1, "field1": 1}, {"id": 2, "field1": 2}],
        },
        body_pattern='{"page": 1}',
    )
    a = EntityManagerClass(
        api_client=api_client,
        entity_class=BaseAlfaEntityClass,
    )
    page = await a.page(page=1, count=2)

    assert page.items == [
        BaseAlfaEntityClass(id=1, field1=1),
        BaseAlfaEntityClass(id=2, field1=2),
    ]
    assert page.number == 1
    assert page.total == 10


@pytest.mark.asyncio
async def test_manager_paginator(api_client):
    a = EntityManagerClass(
        api_client=api_client,
        entity_class=BaseAlfaEntityClass,
    )

    paginator = a.paginator(start_page=0, page_size=1)

    assert paginator._object == a


@pytest.mark.asyncio
async def test_alfa_manager_with_url_params(api_client, aresponses):
    aresponses.add(
        "demo.s20.online",
        "/v2api/1/customer-tariff/index?field1=5&per-page=100",
        "POST",
        {"total": 10, "count": 1, "page": 0, "items": [{"id": 1, "field1": 5}]},
        match_querystring=True,
    )

    aresponses.add(
        "demo.s20.online",
        "/v2api/1/customer-tariff/index?field1=6&per-page=100",
        "POST",
        {"total": 10, "count": 1, "page": 0, "items": [{"id": 2, "field1": 6}]},
        match_querystring=True,
        body_pattern='{"id": 2}',
    )

    a = EntityManagerWithUrlParams(
        api_client=api_client,
        entity_class=BaseAlfaEntityClass,
    )

    entities = await a.list(field1=5)
    assert len(entities) == 1

    entity = entities[0]

    assert entity.id == 1
    assert entity.field1 == 5

    entity = await a.get(
        id_=2,
        field1=6,
    )
