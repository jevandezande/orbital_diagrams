from dataclasses import dataclass
from typing import Iterator

from ._base_orbital import BaseOrbital


@dataclass
class OrbitalGroup(BaseOrbital):
    orbs: list[BaseOrbital]

    def __iter__(self) -> Iterator[BaseOrbital]:
        yield from self.orbs

    def __str__(self) -> str:
        return f"<OrbitalGroup {self.orbs}>"
