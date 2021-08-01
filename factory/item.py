# Standard Library
from typing import Any
from random import choice

# Third party
import yaml

# Local
import data.string_templates as templates


class ItemBase:
    """Base class for Item"""
    def __init__(self, *, item_type=None,
                          item_class=None,
                          item_subclass=None,
                          item_make=None):
        with open("ItemFactory/data/items.yml") as item_data:
            item_types = yaml.safe_load(item_data.read())

        # Needs two-way dictionaries, lookup needs to start at 'make'
        # Likely need enumeration
        # self.item_type = self.get_data(item_types, item_type)

        # item_classes = item_types[item_type]
        # self.item_class = self.get_data(item_classes, item_class)

        # item_subclasses = item_classes[self.item_class]
        # self.item_subclass = self.get_data(item_subclasses, item_subclass)

        # item_makes = item_subclasses[self.item_subclass]
        # self.item_make = self.get_data(item_makes, item_make)

    def get_data(d: dict, key: Any) -> str:
        return {None: choice(d.keys())}.get(key, key)


class ItemAttributes(ItemBase):
    """Attributes for Item objects"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rarity = ""
        self.primary = ""
        self.secondary = ""
        self.constituents = []


class Item(ItemAttributes):
    """The top-level Item object"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = ""
        self.description = ""
        self.stats = {}

    def __str__(self):
        if self.item_type == "armor":
            stats = templates.ARMOR_STATS
            details = templates.ARMOR_DETAILS
        else:
            stats = templates.WEAPON_STATS
            details = templates.WEAPON_DETAILS

        stats = stats.format(**self.stats)
        details = details.format(primary=self.primary,
                                 secondary=self.secondary)

        return templates.ITEM_INFO.format(name=self.name,
                                          description=self.description,
                                          item_type=self.item_type,
                                          item_class=self.item_class,
                                          item_subclass=self.item_subclass,
                                          details=details,
                                          stats=stats)
