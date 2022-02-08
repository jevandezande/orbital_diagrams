from pytest import approx, fixture

from orbital_diagrams import ComboOrbital
from orbital_diagrams._base_orbital import BaseOrbital


@fixture
def orbs_4():
    return [BaseOrbital() for _ in range(4)]


def test_init(orbs_4):
    co = ComboOrbital(orbs_4, [1] * 4)
    assert co.weights == approx([0.5] * 4)


def test_iter(orbs_4):
    co = ComboOrbital(orbs_4, [1] * 4)
    orbs, weights = zip(*co)
    assert list(orbs) == orbs_4
    assert weights == approx([0.5] * 4)


def test_str(orbs_4):
    co = ComboOrbital(orbs_4, [1] * 4)
    assert str(co) == "<ComboOrbital " + " ".join(f"{w:+5.2f} {orb}" for orb, w in co) + ">"
