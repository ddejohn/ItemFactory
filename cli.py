"""A CLI for ItemFactory"""

import yaml


def load_data(data: dict, label="new item") -> 'Menu':
    menu = Menu(prompt=label, options=data.keys())
    for k,v in data.items():
        if isinstance(v, dict):
            menu.submenu[k] = load_data(label=k, data=v)
        else:
            menu.submenu[k] = Menu(prompt=k, options=v)
    return menu
# end


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
# end


def get_input(prompt: str, options: dict) -> str:
    print(f"\n{prompt}")
    for k,v in options.items():
        print(f"  [{k}] - {v}")
    while True:
        sel = input(" > ")
        if sel not in options.keys():
            print("Invalid selection!")
        else:
            return options.get(sel)
# end


class Menu:
    def __init__(self, prompt: str, options: list):
        self.prompt = prompt
        self.options = {str(k):v for k,v in enumerate(options, 1)}
        self.submenu = {}
    # end

    def navigate(self):
        out = []
        sel = get_input(self.prompt, self.options)
        out.append(sel)
        if not self.submenu:
            return out
        out.extend(self.submenu.get(sel).navigate())
        return out
    # end

    def __str__(self, t=0):
        h = "    "
        out = f"{t*h}{self.prompt}\n"
        for lbl, sub in self.submenu.items():
            out += sub.__str__(t+1)
            if not sub.submenu:
                for k,v in sub.options.items():
                    out += f"{(t+2)*h}{v}\n"
        return out
    # end
# end


# TODO: create random Menu nav 
if __name__=="__main__":
    with open("./data/menus.yml") as f:
        menu_data = yaml.safe_load(f.read())

    main_menu = load_data(menu_data)
    print(main_menu.navigate())