from pytest import fixture

from orbital_diagrams import OrbitalGroup
from orbital_diagrams._base_orbital import BaseOrbital


@fixture
def orbs_4():
    return [BaseOrbital() for _ in range(4)]


def test_init(orbs_4):
    og = OrbitalGroup(orbs_4)
    assert list(orbs_4) == og.orbs


def test_iter(orbs_4):
    og = OrbitalGroup(orbs_4)
    assert list(og) == og.orbs


def test_str(orbs_4):
    og = OrbitalGroup(orbs_4)
    assert str(og) == f"<OrbitalGroup {list(og)}>"
