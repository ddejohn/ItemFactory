from .util import cli, factory


SECONDARY_ACTIONS = {
    "generate new name": factory.AssemblyLine.rename,
    "generate new description": factory.AssemblyLine.redescribe,
    "save item": cli.save
}


def new_item(rand) -> factory.Item:
    item = factory.Item()
    traits = cli.main(rand)
    item.category, item.base, item.sub, item.make = traits

    if not rand:
        item.rarity = cli.get_input("Choose item rarity", cli.RARITY)

    factory.AssemblyLine.start(item)
    return item


print(cli.TITLE)
while True:
    sel = cli.get_input(prompt="What would you like to do?",
                        options=cli.MAIN_OPTIONS)
    sel = cli.MAIN_ACTIONS.get(sel)

    if sel == "quit":
        print("\nEnjoy your new items!\n")
        break
    else:
        item = new_item(sel)
        print(f"\n{item}")

        while True:
            secondary = cli.get_input(prompt="What would you like to do?",
                                      options=cli.SECOND_OPTIONS)
            if secondary in SECONDARY_ACTIONS:
                SECONDARY_ACTIONS.get(secondary)(item)
                if "name" in secondary:
                    print(f"\nNew name: {item.name}")
                elif "description" in secondary:
                    desc = factory.paragraphize(s=item.description, i=" "*4)
                    print(f"\nNew item description:\n\n{desc}")
                else:
                    break
            else:
                break
