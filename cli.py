"""A CLI for ItemFactory"""


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