import data.string_templates as templates


class ItemBase:
    """Base class for Item"""
    def __init__(self):
        self.item_type = ""
        self.item_class = ""
        self.item_subclass = ""
        self.item_make = ""


class ItemAttributes(ItemBase):
    """Attributes for Item objects"""
    def __init__(self):
        super().__init__()
        self.rarity = ""
        self.primary = ""
        self.secondary = ""
        self.constituents = []


class Item(ItemAttributes):
    """The top-level Item object"""
    def __init__(self):
        super().__init__()
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
