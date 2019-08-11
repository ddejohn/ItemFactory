from factory_util import build_item


class Item:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)


class ItemBase:
    def __init__(self):
        super().__init__()
        self.item_class = str
        self.base_type = str
        self.sub_type = str
        self.item_type = str
        self.rarity = str
        self.material_weights = list


class ItemConstruction:
    def __init__(self):
        super().__init__()
        self.base_name = str
        self.material = str
        self.secondary = str
        self.parts = list


class NewItem(ItemConstruction, ItemBase):
    def __init__(self):
        super().__init__()
        self.name = str
        self.description = str
        self.stats = dict
        build_item(self)


class ItemBuilder:
    @staticmethod
    def forge():
        new_item = NewItem()
        item_data = {
            "item_class": new_item.item_class,
            "base_type": new_item.base_type,
            "sub_type": new_item.sub_type,
            "name": new_item.name,
            "description": new_item.description,
            "stats": new_item.stats
        }

        return Item(**item_data)


def verbose_print(data, calls=0):
    out = ""
    spc = "    "
    for key, val in data.items():
        if isinstance(val, dict):
            out += spc*calls + f"{key}:\n{verbose_print(val, calls+1)}"
        else:
            out += spc*calls + f"{key}: {val}\n"
    return out


if __name__ == "__main__":
    for _ in range(100):
        item = ItemBuilder.forge()
        print(verbose_print(vars(item)))
    