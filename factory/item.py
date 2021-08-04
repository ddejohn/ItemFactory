class ItemBase:
    """Base class for Item"""
    def __init__(self, *, item_class, item_subclass, item_type, item_subtype):
        self.item_class = item_class
        self.item_subclass = item_subclass
        self.item_type = item_type
        self.item_subtype = item_subtype

    @property
    def embed(self) -> dict:
        head = f"**{self.item_subclass} {self.item_class}** [{self.item_type}]"
        return {"title": self.name,
                "description": f"{head}\n\n" + self.description,
                "color": 0x40444b,
                "fields": [{"name": "Type",
                            "value": self.item_subtype,
                            "inline": True},
                           {"name": "Rarity",
                            "value": self.rarity,
                            "inline": True},
                           {"name": "Construction",
                            "value": self.construction.capitalize(),
                            "inline": True}]}


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
    def construction(self) -> str:
        return f"{self.secondary} {self.primary}"


class Weapon(Item):
    """Top-level class for weapon items"""
    def __init__(self, **item_data: dict):
        super().__init__(**item_data)

    @property
    def construction(self) -> str:
        return f"{self.primary} and {self.secondary}"


if __name__ == "__main__":
    test = Weapon(**{"item_class": "weapon",
                     "item_subclass": "two-handed",
                     "item_type": "blade",
                     "item_subtype": "bastard sword"})
    test.rarity = "Legendary"
    test.primary = "Meteorite"
    test.secondary = "Ebony"
    print(test.embed)
