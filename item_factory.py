import cli
from inspect import getmembers
from factory import AssemblyLine


TITLE = """
\t _ _|  |                     ____|             |                       
\t   |   __|   _ \  __ `__ \   |     _` |   __|  __|   _ \    __|  |   | 
\t   |   |     __/  |   |   |  __|  (   |  (     |    (   |  |     |   | 
\t ___| \__| \___| _|  _|  _| _|   \__,_| \___| \__| \___/  _|    \__, | 
\t                                                                ____/ 

...A random weapon and armor generator which provides richly detailed descriptions, unique names, and basic item stats!"""


MAIN = {
    "1": "build your own",
    "2": "randomize!",
    "q": "quit"
}


MAIN_ACTIONS = {
    "build your own": False,
    "randomize!": True,
    "quit": "quit"
}


class ItemBase:
    def __init__(self, template: list):
        self.item_class, self.base_type, self.sub_type, self.make = template
        self.rarity = str
        self.primary = str
        self.secondary = str
        self.constituents = []
    # end
# end


class Item(ItemBase):
    def __init__(self, template=["", "", "", ""]):
        super().__init__(template)
        self.name = str
        self.description = str
        self.stats = dict
        AssemblyLine.start(self)
    # end

    def __str__(self):
        pass
# end


if __name__ == "__main__":
    print(f"\nHello, adventurer! Welcome to...\n{TITLE}")
    items = []
    menu = cli.main("data/menus.yml")
    while True:
        sel = cli.get_input(prompt="What would you like to do?", options=MAIN)
        sel = MAIN_ACTIONS.get(sel)
        if sel == "quit":
            print("\nEnjoy your new items!\n")
            break
        else:
            traits = menu.navigate(sel)
        item = Item(traits)
        for k,v in item.__dict__.items():
            print(f"{k}: {v}")
# end


# class Item:
#     def __init__(self, **kwargs):
#         for key, val in kwargs.items():
#             setattr(self, key, val)


# class ItemBase:
#     def __init__(self):
#         super().__init__()
#         self.item_class = str
#         self.base_type = str
#         self.sub_type = str
#         self.item_type = str
#         self.rarity = str
#         self.material_weights = list


# class ItemConstruction:
#     def __init__(self):
#         super().__init__()
#         self.base_name = str
#         self.material = str
#         self.secondary = str
#         self.parts = list


# class NewItem(ItemConstruction, ItemBase):
#     def __init__(self):
#         super().__init__()
#         self.name = str
#         self.description = str
#         self.stats = dict
#         build_item(self)


# class ItemBuilder:
#     @staticmethod
#     def forge():
#         new_item = NewItem()
#         item_data = {
#             "item_class": new_item.item_class,
#             "base_type": new_item.base_type,
#             "sub_type": new_item.sub_type,
#             "rarity": new_item.rarity,
#             "name": new_item.name,
#             "description": new_item.description,
#             "stats": new_item.stats
#         }

#         return Item(**item_data)


# def verbose_print(data, calls=0):
#     out = ""
#     spc = "    "
#     for key, val in data.items():
#         if isinstance(val, dict):
#             out += spc*calls + f"{key}:\n{verbose_print(val, calls+1)}"
#         else:
#             out += spc*calls + f"{key}: {val}\n"
#     return out
