"""A CLI for ItemFactory"""

import yaml
from random import choice


with open("../data/menus.yml") as f:
    MAIN_MENU = yaml.safe_load(f.read())


TITLE = """Greetings adventurer, and welcome to...\n
\t _ _|  |                     ____|             |                       
\t   |   __|   _ \  __ `__ \   |     _` |   __|  __|   _ \    __|  |   | 
\t   |   |     __/  |   |   |  __|  (   |  (     |    (   |  |     |   | 
\t ___| \__| \___| _|  _|  _| _|   \__,_| \___| \__| \___/  _|    \__, | 
\t                                                                ____/ \n
...A random weapon and armor generator which provides richly detailed descriptions, unique names, and basic item stats!"""


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


def load(label: str, data: dict) -> 'Menu':
    menu = Menu(prompt=label, options=data.keys())
    for k,v in data.items():
        if isinstance(v, dict):
            menu.submenu[k] = load(label=k, data=v)
        else:
            menu.submenu[k] = Menu(prompt=k, options=v)

    return menu


def get_input(prompt: str, options: dict) -> str:
    print(f"\n{prompt}")
    for k,v in options.items():
        print(f"  [{k}] - {v}")
    while True:
        sel = input(" > ").lower()
        if sel not in options:
            print("\nInvalid selection!\n")
        else:
            sel = options.get(sel)
            break

    return sel


def navigate(menu, rand):
    out = []
    if not rand:
        prompt = MAIN_PROMPTS.get(menu.prompt, "Choose an option")
        sel = get_input(prompt, menu.options)
    else:
        sel = choice(list(menu.options.values()))
    out.append(sel)
    if not menu.submenu:
        return out
    out.extend(navigate(menu.submenu.get(sel), rand))

    return out


class Menu:
    def __init__(self, prompt: str, options: list):
        self.prompt = prompt
        self.options = {str(k):v for k,v in enumerate(options, 1)}
        self.submenu = {}


    def __str__(self, t=0):
        h = "|   "
        out = f"{t*h}{self.prompt}\n"
        for lbl, sub in self.submenu.items():
            out += sub.__str__(t+1)
            if not sub.submenu:
                for k,v in sub.options.items():
                    out += f"{(t+2)*h}{v}\n"

        return out


# def main():
    # print(TITLE)
    # return load(label="main menu", data=MAIN_MENU)


print(load(label="main menu", data=MAIN_MENU))