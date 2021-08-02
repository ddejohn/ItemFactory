class ItemBase:
    """Base class for Item"""
    def __init__(self, *, item_class, item_subclass, item_type, item_subtype):
        self.item_class = item_class
        self.item_subclass = item_subclass
        self.item_type = item_type
        self.item_subtype = item_subtype

    def embed(self, primary_field: dict, secondary_field: dict) -> dict:
        class_subclass = f"{self.item_class} ({self.item_subclass})"
        return {"title": self.name,
                "description": f"*{self.description}*",
                "color": 0x40444b,
                "fields": [{"name": "Class (subclass)",
                            "value": class_subclass,
                            "inline": True},
                           {"name": "Type",
                            "value": self.item_type,
                            "inline": True},
                           {"name": "Subtype",
                            "value": self.item_subtype,
                            "inline": True},
                           {"name": "Rarity",
                            "value": self.rarity,
                            "inline": True},
                           primary_field,
                           secondary_field]}


class ItemAttributes(ItemBase):
    """Attributes for Item objects"""
    def __init__(self, **item_data: dict):
        super().__init__(**item_data)
        self.rarity = ""
        self.primary = ""
        self.secondary = ""
        self.constituents = []


class Item(ItemAttributes):
    """Common class for Armor and Weapon"""
    def __init__(self, **item_data: dict):
        super().__init__(**item_data)
        self.name = ""
        self.description = ""


class Armor(Item):
    """Top-level class for armor items"""
    def __init__(self, **item_data: dict):
        super().__init__(**item_data)

    @property
    def embed(self):
        primary_field = {"name": "Material",
                         "value": self.primary,
                         "inline": True}
        secondary_field = {"name": "Construction",
                           "value": self.secondary,
                           "inline": True}
        return super().embed(primary_field, secondary_field)


class Weapon(Item):
    """Top-level class for weapon items"""
    def __init__(self, **item_data: dict):
        super().__init__(**item_data)

    @property
    def embed(self):
        primary_field = {"name": "Primary Material",
                         "value": self.primary,
                         "inline": True}
        secondary_field = {"name": "Secondary Material",
                           "value": self.secondary,
                           "inline": True}
        return super().embed(primary_field, secondary_field)


if __name__ == "__main__":
    test = Weapon(**{"item_class": "weapon",
                     "item_subclass": "two-handed",
                     "item_type": "blade",
                     "item_subtype": "bastard sword"})
    test.rarity = "Legendary"
    test.primary = "Meteorite"
    test.secondary = "Ebony"
    print(test.embed)
