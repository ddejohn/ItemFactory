"""A CLI for ItemFactory"""

import yaml

ITEM = {
    "1": "armor",
    "2": "weapon"
}


ARMOR = {
    "1": "heavy",
    "2": "light"
}


WEAPON = {
    "1": "melee",
    "2": "ranged"
}


SUBARMOR = {
    "1": "head",
    "2": "chest",
    "3": "hands",
    "4": "feet",
    "5": "shield"
}


SUBWEAPON = {
    "1": "blade",
    "2": "blunt",
    "3": "axe",
    "4": "bow"
}


MAKE = {
    "armor": [
        ("Choose an armor class", ARMOR),
        ("Choose an armor type", SUBARMOR)
    ],
    "weapon": [
        ("Choose a weapon class", WEAPON),
        ("Choose a weapon type", SUBWEAPON)
    ]
}


class Menu:
    def __init__(self, prompt: str, options: list):
        self.prompt = prompt
        self.options = {k: v for k,v in enumerate(options, 1)}
        self.submenus: dict
    # end

    def submenu(self, menu: 'Menu'):
        self.submenus[menu.prompt] = menu
    # end

    # def build_opt(self, options: list) -> dict:
    #     return {k: v for k,v in enumerate(options, 1)}

    def start(self):
        # initiate a single traversal of the menu tree
        pass



with open("./data/menus.yml") as f:
    menu_data = yaml.safe_load(f.read())


def dict_print(data: dict, t=0):
    out = ""
    header = "|   "
    for k,v in data.items():
        out += f"{t*header}{k}\n"
        if isinstance(v, dict):
            out += dict_print(v, t+1)
        elif isinstance(v, list):
            for elem in v:
                out += f"{(t+1)*header}{elem}\n"
    return out


print(dict_print(menu_data))


def get_input(prompt: str, options: dict) -> str:
    print(f"\n{prompt}")
    for k,v in options.items():
        print(f"  [{k}] - {v}")
    while True:
        sel = input(" > ")
        if sel not in options.keys():
            print("Invalid selection!")
        return options.get(sel)
# end


def customize():
    new_item = []
    sel = get_input("Choose an item type", ITEM)
    make = MAKE.get(sel)
    new_item.append(sel)
    for opt in make:
        # prompt, options = opt
        new_item.append(get_input(*opt))
    return new_item
# end
