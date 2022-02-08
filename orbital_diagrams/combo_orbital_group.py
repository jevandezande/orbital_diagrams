from dataclasses import dataclass

from .orbital_group import OrbitalGroup


@dataclass
class ComboOrbitalGroup(OrbitalGroup):
    """
    A group of combo orbitals drawing from the same basis of orbitals

    :param reference_orbitals: Orbitals from which to construct ComboOrbitals
    :param connections: the weights for each ComboOrbital
        rows correspond to the ComboOrbital and the columns correspond to the weight of the connection
        N_ComboOrbitals x N_OrbitalGroups x len(OrbitalGroup)
    """

    def __init__(self, reference_orbitals: list[OrbitalGroup], connections: list[list[list]]):
        self.reference_orbitals = reference_orbitals
        self.connections = connections
