from pytest import fixture, raises

from orbital_diagrams import OrbitalGroup
from orbital_diagrams._base_orbital import BaseOrbital


def gen_orb_group(size):
    return OrbitalGroup([BaseOrbital() for _ in range(size)])


@fixture
def og_4():
    return gen_orb_group(4)


def test_init():
    orbs = [BaseOrbital() for _ in range(4)]
    og = OrbitalGroup(orbs)
    assert og.orbs == orbs


def test_len(og_4):
    assert len(og_4) == 4


def test_iter(og_4):
    assert list(og_4) == og_4.orbs


def test__getitem__(og_4):
    for i in range(-4, 4):
        assert og_4[i] == BaseOrbital()

    with raises(IndexError):
        og_4[-5]
    with raises(IndexError):
        og_4[4]


def test_str(og_4):
    assert str(og_4) == f"<OrbitalGroup {list(og_4)}>"
