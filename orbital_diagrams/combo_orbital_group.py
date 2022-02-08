from dataclasses import dataclass
from typing import Iterator

from .combo_orbital import ComboOrbital
from .orbital_group import OrbitalGroup


@dataclass
class ComboOrbitalGroup(OrbitalGroup):
    """
    A group of combo orbitals drawing from the same basis of orbitals

    :param ref_orb_groups: Orbitals from which to construct ComboOrbitals
    :param connections: the weights for each ComboOrbital
        rows correspond to the ComboOrbital and the columns correspond to the weight of the connection
        N_ComboOrbitals x N_OrbitalGroups x len(OrbitalGroup)
    """

    ref_orb_groups: list[OrbitalGroup]  # N_groups x len(group)
    connections: list[list[list[float]]]  # N_orbs x N_groups x len(group)

    def __init__(
        self,
        ref_orb_groups: list[OrbitalGroup],
        connections: list[list[list[float]]],
        normalize=True,
    ):
        self.ref_orb_groups = ref_orb_groups
        self.connections = connections

        if len(ref_orb_groups) != len(connections[0]):
            raise ValueError(
                "Expected the same number of rows of connections as groups of reference orbitals, got:"
                f"{len(ref_orb_groups)=} != {len(connections[0])=}"
            )

        normed_connections: list[list[list[float]]] = []
        for orb_connections in connections:
            for orb_group, group_cons in zip(ref_orb_groups, orb_connections):
                if len(orb_group) != len(group_cons):
                    raise ValueError("Mismatched dimensions of ref_orb_groups and connections")
                if not any(group_cons):
                    raise ValueError("An orbital's weights cannot all be 0.")
            if normalize:
                normed_connections.append([])
                norm = sum(w ** 2 for group_cons in orb_connections for w in group_cons) ** 0.5
                normed_connections[-1] += [
                    [w / norm for w in group_cons] for group_cons in orb_connections
                ]

        if normalize:
            self.connections = normed_connections

    def __iter__(self) -> Iterator[ComboOrbital]:
        for i in range(len(self)):
            yield self[i]

    def __len__(self) -> int:
        return len(self.connections)

    def __getitem__(self, index):
        if not (0 <= index < len(self)):
            raise IndexError("List index out of range.")

        combo_orbs = (
            (orbital, weight)
            for orbs_weights in zip(self.ref_orb_groups, self.connections[index])
            for orbital, weight in zip(*orbs_weights)
            if weight
        )

        return ComboOrbital(*zip(*combo_orbs))

    @property
    def orbs(self):
        return [orb for orb in self]
