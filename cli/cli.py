import cmd
import constants


class Help(cmd.Cmd):
    intro = constants.INTRO
    prompt = "\n(forge) "

    def help_grammar(self, *args):
        print(constants.HELP_GRAMMAR)

    def help_type(self, *args):
        print(constants.HELP_TYPE)

    def help_class(self, *args):
        print(constants.HELP_CLASS)

    def help_subclass(self, *args):
        print(constants.HELP_SUBCLASS)

    def help_make(self, *args):
        print(constants.HELP_MAKE)

    def help_random(self, *args):
        print(constants.HELP_RANDOM)

    def help_build(self, *args):
        print(constants.HELP_BUILD)

    def help_reroll(self, *args):
        print(constants.HELP_REROLL)


class Forge(Help):
    def __init__(self):
        super().__init__()

    def do_q(self, *args):
        """Shut down the forge"""
        return True

    def do_random(self, *args):
        pass

    def do_build(self, *args):
        pass

    def do_reroll(self, *args):
        pass


if __name__ == "__main__":
    Forge().cmdloop()
