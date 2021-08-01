"""String constants used for the CLI"""


INTRO = r"""
Greetings adventurer, and welcome to...

        _ _|  |                     ____|             |
          |   __|   _ \  __ `__ \   |     _` |   __|  __|   _ \    __|  |   |
          |   |     __/  |   |   |  __|  (   |  (     |    (   |  |     |   |
        ___| \__| \___| _|  _|  _| _|   \__,_| \___| \__| \___/  _|    \__, |
                                                                       ____/

...A random weapon and armor generator which provides richly detailed
    descriptions, unique names, and basic item stats!

Type 'help' or '?' for a list of commands."""


# Commands ------------------------------------------------------------------ #


HELP_RANDOM = """
Forge a random item
-------------------

Grammar:
    random [type | class | subclass]

Examples:
    random
    random armor
    random heavy
    random two-handed
    random ranged
"""


HELP_BUILD = """
Start the forge
---------------

Grammar:
    build [(type | class) [ , (subclass | make)]]

Examples:
    build
    build armor
    build heavy chest
    build recurve bow
    build one-handed
    build dagger
"""


HELP_REROLL = """
Reroll an attribute
-------------------

Grammar:
    reroll ('name' | 'description' | 'stats')

Examples:
    reroll name
    reroll stats
"""


# Help topics --------------------------------------------------------------- #


HELP_GRAMMAR = """
Grammar tips:
    [] denotes an optional argument
    () denotes a group
    The '|' symbol means 'or'
    The ',' symbol indicates concatenation
    Single quotes denotes a terminal symbol
"""


HELP_TYPE = """
type = 'armor'
     | 'weapon'
"""


HELP_CLASS = """
class = 'heavy'
      | 'light'
      | 'one-handed'
      | 'two-handed'
"""


HELP_SUBCLASS = """
subclass = 'head'
         | 'chest'
         | 'hands'
         | 'feet'
         | 'shield'
         | 'blade'
         | 'blunt'
         | 'axe'
         | 'ranged'
"""


HELP_MAKE = """
make = 'dagger'
     | 'corvo'
     | 'stiletto'
     | 'shortsword'
     | 'seax'
     | 'xiphos'
     | 'baselard'
     | 'gladius'
     | 'longsword'
     | 'claymore'
     | 'broadsword'
     | 'bastard sword'
     | 'morning star'
     | 'mace'
     | 'club'
     | 'flail'
     | 'war hammer'
     | 'meteor hammer'
     | 'dire flail'
     | 'labrys'
     | 'hatchet'
     | 'war scythe'
     | 'battle axe'
     | 'halberd'
     | 'glaive'
     | 'recurve bow'
     | 'scythian bow'
     | 'crossbow'
     | 'longbow'
     | 'helm'
     | 'helmet'
     | 'hood'
     | 'coif'
     | 'cuirass'
     | 'corslet'
     | 'brigandine'
     | 'gambeson'
     | 'gauntlets'
     | 'gloves'
     | 'boots'
     | 'sabatons'
     | 'pavise shield'
     | 'kite shield'
     | 'buckler'
     | 'targe shield'
"""
