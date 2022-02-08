from dataclasses import dataclass, field
from typing import Iterator

from ._base_orbital import BaseOrbital


@dataclass
class ComboOrbital(BaseOrbital):
    orbs: list[BaseOrbital]
    weights: list[float] = field(default_factory=list)

    def __post_init__(self):
        orbs, weights = self.orbs, self.weights

        if len(orbs) != len(weights):
            raise ValueError(
                f"Received mismatched orbitals and weights: {len(orbs)=} != {len(weights)=}"
            )

        if weights is None:
            self.weights = [1 / len(orbs) ** 0.5] * len(orbs)
        else:
            norm = sum(w ** 2 for w in self.weights) ** 0.5
            self.weights = [w / norm for w in weights]

    def __iter__(self) -> Iterator[tuple[BaseOrbital, float]]:
        yield from zip(self.orbs, self.weights)

    def __str__(self) -> str:
        return "<ComboOrbital " + " ".join(f"{w:+5.2f} {orb}" for orb, w in self) + ">"
