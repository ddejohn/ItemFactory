from .util import cli, factory

ITEMS = []
print(cli.TITLE)


def new_item(rand) -> factory.Item:
    item = factory.Item()
    traits = cli.main(rand)
    item.item_class, item.base_type, item.sub_type, item.make = traits

    if not rand:
        item.rarity = cli.get_input("Choose item rarity", cli.RARITY)

    factory.AssemblyLine.start(item)
    return item


# main program loop
while True:
    sel = cli.get_input(
        prompt="What would you like to do?",
        options=cli.MAIN_OPTIONS
    )
    sel = cli.MAIN_ACTIONS.get(sel)

    if sel == "quit":
        if cli.ITEMS:
            cli.save(ITEMS)
            print("\nEnjoy your new items!\n")
        break
    else:
        item = new_item(sel)
        print(f"\n{item}")
        # while True:
        #     sel = input("Keep item? [y/n]: ").lower()
        #     if sel and sel in "yn":
        #         if sel == "y":
        #             ITEMS.append(item)
        #         break
        #     else:
        #         print("\nInvalid selection!\n")
