from alfacrm.entities import Branch


def test_init_branch():
    branch = Branch(
        id=1,
        name="First branch",
        is_active=True,
        subject_ids=[1, 2, 3],
        weight=1,
    )

    assert branch.id == 1
    assert branch.name == "First branch"
    assert branch.is_active is True
    assert branch.subject_ids == [1, 2, 3]
    assert branch.weight == 1
