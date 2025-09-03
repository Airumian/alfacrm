import pytest

from alfacrm import entities
from alfacrm.managers import Branch

BRANCH_RESPONSE = {
    "page": 0,
    "total": 1,
    "count": 1,
    "items": [
        {
            "id": 1,
            "name": "name",
            "is_active": False,
            "subject_ids": [1, 2, 3],
            "weight": 1,
        }
    ],
}


@pytest.mark.asyncio
async def test_branch(aresponses, api_client):
    aresponses.add("demo.s20.online", "/v2api/1/branch/index", "POST", BRANCH_RESPONSE)
    branch_manager = Branch(
        api_client=api_client,
        entity_class=entities.Branch,
    )

    branches = await branch_manager.list()

    assert len(branches) == 1

    branch = branches[0]

    assert branch.id == 1
    assert branch.name == "name"
    assert branch.is_active is False
    assert branch.subject_ids == [1, 2, 3]
    assert branch.weight == 1
