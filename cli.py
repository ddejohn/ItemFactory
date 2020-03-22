"""A CLI for ItemFactory"""


ARMOR = {
    1: "heavy",
    2: "light"
}

WEAPON = {
    1: "melee",
    2: "ranged"
}

SUBARMOR = {
    1: "head",
    2: "chest",
    3: "hands",
    4: "feet",
    5: "shield"
}

SUBWEAPON = {
    1: "blade",
    2: "blunt",
    3: "axe",
    4: "bow"
}


ITEM = {
    1: ARMOR,
    2: WEAPON
}


MENU = {
    "Choose an item class": ITEM,
    "Choose an armor weight": ARMOR,
    "Choose a weapon style": WEAPON,
    "Choose an armor type": SUBARMOR,
    "Choose a weapon type": SUBWEAPON
}


def numput() -> int or None:
    sel = input(" > ")
    if sel.isdigit():
        return int(sel)
# end


def options(s: str, d: dict) -> None:
    print(s)
    for k,v in d.items():
        print(f"  [{k}] - {v}")
# end


def customize():
    while True:
        new_item = []
        for k,v in MENU.items():
            options(k, v)