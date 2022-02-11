from orbital_diagrams.api import EnergyOrbital


def test_init():
    EnergyOrbital(-1, "a")
    EnergyOrbital(-2, "b")
    EnergyOrbital(-2, "c")
    EnergyOrbital(-2, "c")


def test_eq_lt_gt():
    eo1 = EnergyOrbital(-1, "a")
    eo2 = EnergyOrbital(-2, "b")
    eo3 = EnergyOrbital(-2, "c")
    eo4 = EnergyOrbital(-2, "c")

    assert eo1 == eo1
    assert eo1 != eo2
    assert eo2 != eo3
    assert eo3 == eo4
    assert eo1 > eo2
    assert eo2 < eo3
