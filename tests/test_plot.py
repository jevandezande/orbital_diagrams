import matplotlib.pyplot as plt
from pytest import mark, raises

from orbital_diagrams.api import EnergyOrbital
from orbital_diagrams.orbitals._base_orbital import BaseOrbital
from orbital_diagrams.plot import cycle_values, plotter, setup_axis, subplots


def test_setup_axis():
    fig, ax = plt.subplots()

    setup_axis(ax, None, xticks=range(100), xlim=(0, 100))
    setup_axis(ax, "BaseOrbital")
    setup_axis(ax, "EnergyOrbital")
    setup_axis(ax, "ComboOrbital")
    setup_axis(ax, "ComboEnergyOrbital")
    setup_axis(ax, "ComboOrbitalGroup")
    setup_axis(ax, "ComboEnergyOrbitalGroup")

    with raises(NotImplementedError):
        setup_axis(ax, "None")


def test_subplots():
    assert len(subplots("BaseOrbital")) == 2
    assert len(subplots("EnergyOrbital")[1]) == 1

    assert subplots("ComboOrbital", 1, 4)[1].shape == (1, 4)
    assert subplots("ComboEnergyOrbital", 3, 5)[1].shape == (3, 5)


@mark.xfail
def test_plotter(tmp_path):
    fig, ((ax,),) = subplots("BaseOrbital")
    plotter(
        [BaseOrbital(), BaseOrbital(), BaseOrbital()],
        title="Hello World",
        style="BaseOrbital",
        plot=(fig, ax),
        xlim=(0, 2),
        xticks_minor=True,
        yticks_minor=2,
        legend=True,
        colors=None,
        markers=None,
        linestyles=None,
        savefig=f"{tmp_path}/BaseOrbitals.png",
    )

    plotter(
        [EnergyOrbital(-1), EnergyOrbital(-2), EnergyOrbital(-3)],
        title="World",
        style="EnergyOrbital",
        plot=None,
        xlim=None,
        xticks=None,
        xticks_minor=1,
        yticks_minor=True,
        legend=False,
        alphas=[0.9, 0.1],
        colors=["b", "k"],
        markers="x",
        linestyles=["-", ":"],
        savefig=f"{tmp_path}/",
    )

    plotter(
        [],
        title="Hello",
        style=type(BaseOrbital()).__name__,
        plot=None,
        xlim=None,
        xticks=None,
        legend=True,
        colors=None,
        markers=None,
        linestyles=None,
        savefig=f"{tmp_path}/",
    )

    plotter(
        [],
        title="Hello",
        style=None,
        plot=None,
        xlim=(0, 10),
        xticks=None,
        legend=False,
        colors=None,
        markers="+",
        linestyles="--",
        savefig=f"{tmp_path}/",
    )

    plotter(
        [],
        title="Hello",
        style=None,
        plot=None,
        xlim=(0, 10),
        xticks=None,
        ylim=(0, 10),
        yticks=(0, 5, 10),
        yticks_minor=True,
        legend=False,
        colors=None,
        alphas=0.5,
        markers="+",
        linestyles="--",
        savefig=f"{tmp_path}/",
    )

    with raises(NotImplementedError):
        plotter([], style="QWERTY")


def test_cycle_values():
    assert next(cycle_values(None)) is None
    assert next(cycle_values(1)) == 1

    it = cycle_values([0, 1, 2])
    assert next(it) == 0
    assert next(it) == 1
    assert next(it) == 2
    assert next(it) == 0
