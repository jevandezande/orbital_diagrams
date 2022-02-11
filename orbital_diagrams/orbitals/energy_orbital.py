from dataclasses import dataclass

from ._base_orbital import BaseOrbital


@dataclass(order=True)
class EnergyOrbital(BaseOrbital):
    energy: float
    label: str = ""
