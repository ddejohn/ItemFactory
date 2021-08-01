# Standard Library
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
            item_data = yaml.safe_load(item_data.read())
            item_types = item_data[""]
            item_classes = item_data[""]
            item_subclasses = item_data[""]
            item_makes = item_data[""]

        self.item_type = item_data.get(item_type, choice(("armor", "weapon")))
        self.item_class = item_data.get(self.item_type).get(item_class)
        self.item_subclass = item_subclass
        self.item_make = item_make


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
