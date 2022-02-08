from dataclasses import dataclass
from typing import Iterator

from ._base_orbital import BaseOrbital


@dataclass
class OrbitalGroup(BaseOrbital):
    orbs: list[BaseOrbital]

    def __len__(self) -> int:
        return len(self.orbs)

    def __iter__(self) -> Iterator[BaseOrbital]:
        yield from self.orbs

    def __str__(self) -> str:
        return f"<{type(self).__name__} {self.orbs}>"
