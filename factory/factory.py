"""Factory floor"""

# Standard Library
# from random import choice, sample
from typing import Union

# Local
from .item import Weapon, Armor


class Forge:
    def __init__(self, rarity_weights=(50, 25, 15, 6, 3, 1)):
        self.rarity_weights = rarity_weights
        self.rarities = ("crude", "common", "uncommon",
                         "rare", "legendary", "mythical")

    def __call__(self, *args: str) -> Union[Weapon, Armor]:
        """
        Forges a Weapon or Armor item.

        Args can follow this grammar:
            [class | subclass | type | subtype | (subclass, type)]

        For descriptions of these arguments, see helpers.constants
        """
        pass
