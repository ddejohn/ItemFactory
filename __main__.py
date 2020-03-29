from .util import cli, factory


ITEMS = []
MENU = cli.main()


def save():
    print("\nSaving items to 'items.txt'")
    with open("ItemFactory/items.txt", "a+") as f:
        for item in ITEMS:
            item = str(item)
            f.write(f"\n{item}")
        # end
    # end
# end


def new_item(sel):
    traits = MENU.navigate(sel)
    item = factory.Item(traits)

    print(f"\n{item}")
    while True:
        sel = input("Keep item? [y/n]: ").lower()
        if sel and sel in "yn":
            if sel == "y":
                ITEMS.append(item)
            break
        else:
            print("\nInvalid selection!\n")
        # end
    # end
# end


# main menu loop
while True:
    sel = cli.get_input(
        prompt="What would you like to do?",
        options=cli.MAIN_OPTIONS
    )
    sel = cli.MAIN_ACTIONS.get(sel)

    if sel == "quit":
        if ITEMS:
            save()
            print("\nEnjoy your new items!\n")
        break
    else:
        new_item(sel)
    # end
# end
