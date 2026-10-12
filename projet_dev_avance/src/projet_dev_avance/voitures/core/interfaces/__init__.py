"""Interfaces (classes abstraites) du projet."""

from .motorisation import Motorisation
from .vehicule import Vehicule
from .repository import Repository

__all__ = [
    "Motorisation",
    "Vehicule",
    "Repository",
]
