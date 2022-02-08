from orbital_diagrams import OrbitalGroup
from orbital_diagrams._base_orbital import BaseOrbital


def gen_orb_group(size):
    return OrbitalGroup([BaseOrbital() for _ in range(size)])


def test_init():
    orbs = [BaseOrbital() for _ in range(4)]
    og = OrbitalGroup(orbs)
    assert og.orbs == orbs


def test_len():
    assert len(gen_orb_group(4)) == 4


def test_iter():
    og = gen_orb_group(4)
    assert list(og) == og.orbs


def test_str():
    og = gen_orb_group(4)
    assert str(og) == f"<OrbitalGroup {list(og)}>"
