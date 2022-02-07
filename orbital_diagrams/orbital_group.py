from dataclasses import dataclass

from ._base_orbital import BaseOrbital


@dataclass
class OrbitalGroup(BaseOrbital):
    orbs: list[BaseOrbital]
