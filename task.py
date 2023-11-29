"""
Module description: This module defines the Atom and Molecule classes for handling atomic structures
"""
from enum import Enum
from dataclasses import dataclass


class AtomType(Enum):
    """
    Enum representing different types of atoms.
    """
    ISOTYPE = 1
    RADIOACTIVE = 2
    ION = 3
    ANTIMATTER = 4
    STABLE = 5


@dataclass
class Atom:
    """
    Represents an atom with basic properties such as name, atomic mass unit, neutrons, protons,
    electrons, and atom type.
    """
    name: str
    atomic_mass_unit: float
    neutrons: int = 0
    protons: int = 0
    electrons: int = 0
    atom_type: AtomType = AtomType.STABLE

    def is_neutral(self):
        """
        Returns if atom is neutral
        """
        return self.neutrons == self.electrons


class Molecule:
    """
    Represents a molecule composed of atoms.
    """

    def __init__(self, name):
        """
        Initialization objects in class
        """
        self.name = name
        self.atoms = []

    def add_atom(self, item):
        """
        Adds objects from first class into object from second class
        """
        self.atoms.append(item)

    def sort_atoms_by_mass(self):
        """
        Sorts atoms by mass
        """
        print("Виводжу відсортовані атоми за масою нижче:")
        self.atoms.sort(key=lambda item: item.atomic_mass_unit)

    def find_average_mass(self):
        """
        Finds average mass of atoms
        """
        if not self.atoms:
            return None
        return sum(atomic.atomic_mass_unit for atomic in self.atoms) / len(self.atoms)


if __name__ == "__main__":

    atom_1 = Atom("Hydrogen", 6.008, 0, 1, 1, AtomType.STABLE)
    atom_2 = Atom("Helium", 4.0026, 2, 2, 2, AtomType.STABLE)
    atom_3 = Atom("Oxygen", 2.999, 8, 8, 8, AtomType.STABLE)

    molecule = Molecule("Water")
    molecule.add_atom(atom_1)
    molecule.add_atom(atom_2)
    molecule.add_atom(atom_3)

    print(Atom.is_neutral(atom_1))  # метод перевірки на нейтральність

    molecule.sort_atoms_by_mass()
    for atom in molecule.atoms:
        print(f"{atom.name}: {atom.atomic_mass_unit}")  # сортує атоми за зростанням мас

    print(molecule.find_average_mass())  # виводить середню масу атомів
