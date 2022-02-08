from pytest import approx, fixture, mark, raises

from orbital_diagrams import ComboOrbitalGroup, OrbitalGroup
from orbital_diagrams._base_orbital import BaseOrbital


@fixture
def orbs_2():
    return [BaseOrbital() for _ in range(2)]


@fixture
def orb_group_1():
    return OrbitalGroup([BaseOrbital()])


@fixture
def orb_group_2():
    return OrbitalGroup([BaseOrbital() for _ in range(2)])


@fixture
def combo_orb_group_3(orb_group_2):
    connections3 = [
        [[1, 0], [1, 0]],
        [[1, 0], [-1, 0]],
        [[0, 1], [0, 1]],
        [[0, 1], [0, -1]],
    ]
    return ComboOrbitalGroup(
        [orb_group_2, orb_group_2],
        connections3,
    )


@mark.xfail
def test_init(orb_group_1, orb_group_2):
    connections1 = [[[1], [1]], [[1], [-1]]]
    ComboOrbitalGroup([orb_group_1, orb_group_1], connections1)

    connections2 = [[[1, 0], [1, 0]], [[1, 0], [-1, 0]]]
    ComboOrbitalGroup([orb_group_2, orb_group_2], connections2)

    connections3 = [
        [[1, 0], [1, 0]],
        [[1, 0], [-1, 0]],
        [[0, 1], [0, 1]],
        [[0, 1], [0, -1]],
    ]
    ComboOrbitalGroup(
        [orb_group_2, orb_group_2],
        connections3,
    )

    with raises(ValueError):
        connections4 = [
            [[1, 0], [1, 0]],
            [[1, 0], [-1, 0]],
            [[0, 1], [0, 1]],
            [[0, 0], [0, 0]],
        ]
        ComboOrbitalGroup(
            [orb_group_2, orb_group_2],
            connections4,
        )


@mark.xfail
def test_len(combo_orb_group_2, combo_orb_group_3):
    assert len(combo_orb_group_2) == 2
    assert len(combo_orb_group_3) == 4


@mark.xfail
def test_iter(combo_orb_group_2, combo_orb_group_3):
    sqrt2 = approx(1 / (2 ** 0.5))

    combo_orbs_2 = [combo_orb for combo_orb in combo_orb_group_2]
    assert combo_orbs_2.reference_orbitals == [orb_group_2, orb_group_2]
    assert combo_orbs_2[0].weights == [sqrt2, sqrt2]
    assert combo_orbs_2[1].weights == [sqrt2, -sqrt2]

    combo_orbs_3 = [combo_orb for combo_orb in combo_orb_group_3]
    assert combo_orbs_3.reference_orbitals == [orb_group_2, orb_group_2]
    assert combo_orbs_3[0].weights == [sqrt2, sqrt2, 0, 0]
    assert combo_orbs_3[1].weights == [sqrt2, -sqrt2, 0, 0]
    assert combo_orbs_3[2].weights == [0, 0, sqrt2, sqrt2]
    assert combo_orbs_3[3].weights == [0, 0, sqrt2, -sqrt2]


@mark.xfail
def test_str(orbs_4):
    pass


@mark.xfail
def test_orbs(combo_orb_group_2, combo_orb_group_3):
    assert len(combo_orb_group_2.orbs) == 2
    assert len(combo_orb_group_3.orbs) == 4

    assert combo_orb_group_2.orbs == [orb for orb in combo_orb_group_2]
    assert combo_orb_group_3.orbs == [orb for orb in combo_orb_group_3]
