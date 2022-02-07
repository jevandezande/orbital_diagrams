from pytest import fixture, mark

from orbital_diagrams import OrbitalGroup
from orbital_diagrams._base_orbital import BaseOrbital


@fixture
def orbs_4():
    return [BaseOrbital() for _ in range(4)]


def test_init(orbs_4):
    og = OrbitalGroup(orbs_4)
    assert og.orbs == orbs_4


@mark.xfail
def test_iter(orbs_4):
    og = OrbitalGroup(orbs_4)
    assert list(og) == og.orbs


@mark.xfail
def test_str(orbs_4):
    og = OrbitalGroup(orbs_4)
    assert str(og) == "<OrbitalGroup {list(og)}>"
