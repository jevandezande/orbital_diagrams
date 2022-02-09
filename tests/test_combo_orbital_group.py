from pytest import approx, fixture, raises

from orbital_diagrams import ComboOrbitalGroup, OrbitalGroup
from orbital_diagrams._base_orbital import BaseOrbital

SQRT2 = approx(1 / (2 ** 0.5))
NSQRT2 = approx(-1 / (2 ** 0.5))


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
def combo_orb_group_2(orb_group_2):
    connections3 = [
        [[1, 0], [1, 0]],
        [[1, 0], [-1, 0]],
    ]
    return ComboOrbitalGroup(
        [orb_group_2, orb_group_2],
        connections3,
    )


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
            [[0, 0], [0, 0]],  # Having all 0 coefficients for an orbital is not allowed
        ]
        ComboOrbitalGroup(
            [orb_group_2, orb_group_2],
            connections4,
        )


def test_len(combo_orb_group_2, combo_orb_group_3):
    assert len(combo_orb_group_2) == 2
    assert len(combo_orb_group_3) == 4


def test_iter(orb_group_2, combo_orb_group_2, combo_orb_group_3):
    # combo_orbs_2 = [combo_orb for combo_orb in combo_orb_group_2]
    assert combo_orb_group_2.ref_orb_groups == [orb_group_2, orb_group_2]
    assert combo_orb_group_2[0].weights == [SQRT2, SQRT2]
    assert combo_orb_group_2[1].weights == [SQRT2, NSQRT2]

    combo_orbs_3 = [combo_orb for combo_orb in combo_orb_group_3]
    assert combo_orb_group_3.ref_orb_groups == [orb_group_2, orb_group_2]
    assert combo_orb_group_3.connections == [
        [[SQRT2, 0], [SQRT2, 0]],
        [[SQRT2, 0], [NSQRT2, 0]],
        [[0, SQRT2], [0, SQRT2]],
        [[0, SQRT2], [0, NSQRT2]],
    ]
    assert combo_orb_group_3[0].weights == [SQRT2, SQRT2]
    assert combo_orb_group_3[1].weights == [SQRT2, NSQRT2]
    assert combo_orbs_3[2].weights == [SQRT2, SQRT2]
    assert combo_orbs_3[3].weights == [SQRT2, NSQRT2]


def test__getitem__(combo_orb_group_2, combo_orb_group_3):
    combo_orb_group_2[-2]
    combo_orb_group_2[-1]
    combo_orb_group_2[0]
    combo_orb_group_2[1]

    with raises(IndexError):
        combo_orb_group_2[2]
    with raises(IndexError):
        combo_orb_group_2[-3]


def test_orbs(combo_orb_group_2, combo_orb_group_3):
    assert len(combo_orb_group_2.orbs) == 2
    assert len(combo_orb_group_3.orbs) == 4

    assert combo_orb_group_2.orbs == [orb for orb in combo_orb_group_2]
    assert combo_orb_group_3.orbs == [orb for orb in combo_orb_group_3]
