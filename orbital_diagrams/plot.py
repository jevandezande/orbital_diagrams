from itertools import cycle

from matplotlib import ticker

from ._typing import (
    Any,
    Axes,
    Iterable,
    Opt_Iter_Float,
    Opt_Iter_Str,
    Opt_Plot,
    Optional,
    Plot,
    Sequence,
)
from .orbitals._base_orbital import BaseOrbital


def plotter(
    orbitals: Iterable[BaseOrbital],
    title: Optional[str] = None,
    style: Optional[str] = None,
    plot: Opt_Plot = None,
    xlim: Optional[tuple[float, float]] = None,
    xticks: Optional[tuple[float, float]] = None,
    xticks_minor: Iterable | bool = True,
    xlabel: Optional[str] = None,
    ylim: Optional[tuple[float, float]] = None,
    yticks: Optional[Iterable] = None,
    yticks_minor: Iterable | bool = True,
    ylabel: Optional[str] = None,
    labels: Opt_Iter_Str = None,
    colors: Opt_Iter_Str = None,
    alphas: Opt_Iter_Float = None,
    markers: Opt_Iter_Str = None,
    linestyles: Opt_Iter_Str = None,
    linewidths: Opt_Iter_Float = None,
    legend: bool = True,
    savefig: Optional[str] = None,
) -> Plot:
    """
    Plot an iterable of Orbitals

    :param orbitals: orbitals to plot
    :param title: title of the plot
    :param style: plot-style (e.g. ???), if None, generated by type(orbitals[0]).__name__
    :param plot: where to plot, generates new figure if None
    :param x*: x-axis setup parameters
    :param y*: y-axis setup parameters
    :param labels: labels for the orbitals, if None, str(orbital)
    :param colors: colors to plot the orbitals
    :param alphas: transparency settings to use
    :param markers: markers to plot the orbitals
    :param linestyles: linestyles to plot the orbitals
    :param linewidths: linewidths to plot the orbitals
    :param legend: whether to plot a legend
    :param savefig: where to save the figure
    :return: figure and axes
    """
    pass


def plot_orbitals(
    orbitals: Sequence[BaseOrbital],
    style: str,
    ax: Axes,
    labels: Opt_Iter_Str = None,
    colors: Opt_Iter_Str = None,
    alphas: Opt_Iter_Float = None,
    markers: Opt_Iter_Str = None,
    linestyles: Opt_Iter_Str = None,
    linewidths: Opt_Iter_Float = None,
):
    """
    Plot Orbitals on an axis.

    :param orbitals: the Orbitals to be plotted
    :param ax: the axis on which to plot
    :param style: the plot style
    :param labels: labels for the Orbitals, if None, str(Orbital)
    :param colors: the colors to use
    :param alphas: transparency settings to use
    :param markers: the markers to use at each point on the plot
    :param linestyles: the styles of line to use
    :param linewidths: the widths of line to use
    """
    pass


def plot_orbital(
    orbital: BaseOrbital,
    style: str,
    ax: Axes,
    label: Optional[str] = None,
    color: Optional[str] = None,
    marker: Optional[str] = None,
    linestyle: Optional[str] = None,
    linewidth: Optional[float] = None,
    alpha: Optional[float] = None,
):
    """
    Plot an Orbital on an axis.

    :param orbital: the orbital to be plotted
    :param style: the plot style; if None, generates based on the type(Orbital)
    :param ax: the axis on which to plot
    :param label: label for the Orbital; if None, str(Orbital)
    :param color: the color to use
    :param marker: the marker to use at each point on the plot
    :param linestyle: the style of line to use
    :param linewidth: the width of line to use
    :param alpha: transparency setting
    :param peaks: peak highlighting parameters
    """
    pass


def subplots(style: str, *args, setup_axis_kw: Optional[dict] = None, **kwargs) -> Plot:
    """
    Make a (non-squeezed) subplots
    """
    pass


def setup_axis(  # noqa: C901
    ax: Iterable | Axes,
    style: Optional[str] = None,
    title: Optional[str] = None,
    xlim: Optional[tuple[float, float]] = None,
    xticks: Optional[tuple[float, float]] = None,
    xticks_minor: Iterable | bool = True,
    xlabel: Optional[str] = None,
    ylim: Optional[tuple[float, float]] = None,
    yticks: Optional[tuple[float, float]] = None,
    yticks_minor: Iterable | bool = True,
    ylabel: Optional[str] = None,
):
    """
    Setup the axis labels and limits.
    Autogenerates based on style for any variable set to None.

    :param ax: axis to setup
    :param style: style to use
    :param title: title of the axis
    :param *lim: limits for *-axis values
    :param *ticks: *-axis ticks
    :param *ticks_minor: *-axis minor ticks
    :param *label: label for the *-axis
    """
    if not isinstance(ax, Axes):
        for sub_ax in ax:
            setup_axis(
                sub_ax,
                style,
                title,
                xlim,
                xticks,
                xticks_minor,
                xlabel,
                ylim,
                yticks,
                yticks_minor,
                ylabel,
            )

    else:
        # Update values that are None
        up = lambda v, d: d if v is None else v

        if style:
            if style == "BaseOrbital":
                pass
            elif style == "EnergyOrbital":
                ylabel = up(ylabel, "Energy")
            elif style == "ComboOrbital":
                pass
            elif style == "ComboEnergyOrbital":
                ylabel = up(ylabel, "Energy")
            elif style == "OrbitalGroup":
                pass
            elif style == "EnergyOrbitalGroup":
                ylabel = up(ylabel, "Energy")
            elif style == "ComboOrbitalGroup":
                pass
            elif style == "ComboEnergyOrbitalGroup":
                ylabel = up(ylabel, "Energy")
            else:
                raise NotImplementedError(
                    f"{style=} is not yet implemented, buy a developer a coffee."
                )

        ax.set_title(title)

        if xticks is not None:
            ax.set_xticks(xticks)
        if xticks_minor is True:
            ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
        elif xticks_minor is not None:
            ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(xticks_minor))
        if yticks is not None:
            ax.set_yticks(yticks)
        if yticks_minor is True:
            ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
        elif yticks_minor is not None:
            ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(yticks_minor))

        if xlim is not None:
            ax.set_xlim(*xlim)
        if ylim is not None:
            ax.set_ylim(*ylim)

        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)


def cycle_values(values: Any) -> Iterable:
    """
    Make a cycle iterator of values.

    :param values: a value or list of values to be cycled.
    :return: iterator of cycled values
    """
    if not isinstance(values, Iterable):
        values = [values]
    yield from cycle(values)
