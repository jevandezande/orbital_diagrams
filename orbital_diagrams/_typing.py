from typing import Any, Iterable, Optional, Sequence, TypeAlias, TypeVar

from matplotlib.axes import Axes
from matplotlib.figure import Figure
from numpy import ndarray

Opt_Iter_Str: TypeAlias = Optional[Iterable[str] | str]
Opt_Iter_Float: TypeAlias = Optional[Iterable[float] | float]

Plot: TypeAlias = tuple[Figure, Axes]
Opt_Plot: TypeAlias = Optional[tuple[Figure, Axes]]

ArrayLike: TypeAlias = list | ndarray


__all__ = [
    "ArrayLike",
    "Any",
    "Axes",
    "Iterable",
    "Opt_Iter_Float",
    "Opt_Iter_Str",
    "Opt_Plot",
    "Optional",
    "Plot",
    "Sequence",
    "TypeVar",
]
