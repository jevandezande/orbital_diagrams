from dataclasses import dataclass
from typing import Optional

from ._base_orbital import BaseOrbital


@dataclass
class ComboOrbital(BaseOrbital):
    orbs: list[BaseOrbital]
    weights: Optional[list[float]] = None
