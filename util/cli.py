"""A CLI for ItemFactory"""

import yaml
from random import choice
from typing import List

with open("ItemFactory/data/menus.yml") as f:
    MAIN_MENU = yaml.safe_load(f.read())


TITLE = """Greetings adventurer, and welcome to...

        _ _|  |                     ____|             | 
          |   __|   _ \  __ `__ \   |     _` |   __|  __|   _ \    __|  |   |
          |   |     __/  |   |   |  __|  (   |  (     |    (   |  |     |   |
        ___| \__| \___| _|  _|  _| _|   \__,_| \___| \__| \___/  _|    \__, |
                                                                       ____/

...A random weapon and armor generator which provides richly detailed
    descriptions, unique names, and basic item stats!"""


RARITY = {
    "1": "crude",
    "2": "common",
    "3": "uncommon",
    "4": "rare",
    "5": "legendary",
    "6": "mythical"
}


MAIN_OPTIONS = {
    "1": "build your own",
    "2": "randomize!",
    "q": "quit"
}


MAIN_ACTIONS = {
    "build your own": False,
    "randomize!": True,
    "quit": "quit"
}


MAIN_PROMPTS = {
    "armor": "Choose an armor class",
    "heavy": "Choose an armor type",
    "light": "Choose an armor type",
    "weapon": "Choose a weapon class",
    "one-handed": "Choose a weapon type",
    "two-handed": "Choose a weapon type"
}


class Menu:
    def __init__(self, prompt: str, options: list):
        self.prompt = prompt
        self.options = {str(k): v for k, v in enumerate(options, 1)}
        self.submenu = {}

    def __str__(self, t=0):
        h = "|   "
        out = f"{t*h}{self.prompt}\n"
        for lbl, sub in self.submenu.items():
            out += sub.__str__(t+1)
            if not sub.submenu:
                for k, v in sub.options.items():
                    out += f"{(t+2)*h}{v}\n"
        return out


def save(items: list):
    print("\nSaving items to 'items.txt'")
    with open("ItemFactory/items.txt", "a+") as f:
        for item in items:
            item = str(item)
            f.write(f"\n{item}")


def load(label: str, data: dict) -> Menu:
    menu = Menu(prompt=label, options=data.keys())
    for k, v in data.items():
        if isinstance(v, dict):
            menu.submenu[k] = load(label=k, data=v)
        else:
            menu.submenu[k] = Menu(prompt=k, options=v)

    return menu


def get_input(prompt: str, options: dict) -> str:
    print(f"\n{prompt}")
    for k, v in options.items():
        print(f"  [{k}] - {v}")
    while True:
        sel = input(" > ").lower()
        if sel not in options:
            print("\nInvalid selection!\n")
        else:
            sel = options.get(sel)
            break

    return sel


def navigate(menu: Menu, rand: bool) -> List[str]:
    out = []
    if rand:
        sel = choice([*menu.options.values()])
    else:
        prompt = MAIN_PROMPTS.get(menu.prompt, "Choose an option")
        sel = get_input(prompt, menu.options)
    out.append(sel)

    if menu.submenu:
        return out + navigate(menu.submenu.get(sel), rand)
    return out


def main(rand: bool):
    return navigate(load(label="main menu", data=MAIN_MENU), rand)
