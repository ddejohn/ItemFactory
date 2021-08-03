PATHS = {"items": "ItemFactory/data/items.yml",
         "materials": "ItemFactory/data/materials.yml",
         "parts": "ItemFactory/data/parts.yml",
         "naming": "ItemFactory/data/naming.yml",
         "decorations": "ItemFactory/data/decorations.yml",
         "details": "ItemFactory/data/details.yml"}


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


HELP_BUILD = """```
Build an item with optional arguments
---------------

Grammar:
    build [class | subclass | type | subtype | (subclass, type)]

Examples:
    build
    build armor
    build one-handed
    build ranged
    build heavy chest
    build 'recurve bow'
    build dagger

Note:
    Enclose multi-word args with single quotes, e.g.: 'war hammer'
```"""


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


HELP_CLASS = """
class = 'armor'
      | 'weapon'
"""


HELP_SUBCLASS = """
subclass = 'heavy'
         | 'light'
         | 'one-handed'
         | 'two-handed'
"""


HELP_TYPE = """
type = 'head'
     | 'chest'
     | 'hands'
     | 'feet'
     | 'shield'
     | 'blade'
     | 'blunt'
     | 'axe'
     | 'ranged'
"""


HELP_SUBTYPE = """
subtype = 'helm'
        | 'helmet'
        | 'cuirass'
        | 'corslet'
        | 'gauntlets'
        | 'sabatons'
        | 'pavise shield'
        | 'kite shield'
        | 'hood'
        | 'coif'
        | 'brigandine'
        | 'gambeson'
        | 'gloves'
        | 'boots'
        | 'buckler'
        | 'targe shield'
        | 'dagger'
        | 'haladie dagger'
        | 'corvo'
        | 'stiletto'
        | 'shortsword'
        | 'falchion'
        | 'seax'
        | 'cutlass'
        | 'rapier'
        | 'kodachi'
        | 'hook sword'
        | 'willow leaf sabre'
        | 'chokuto'
        | 'jian'
        | 'xiphos'
        | 'baselard'
        | 'gladius'
        | 'morning star'
        | 'mace'
        | 'club'
        | 'flail'
        | 'labrys'
        | 'hatchet'
        | 'longsword'
        | 'claymore'
        | 'odachi'
        | 'dadao'
        | 'estoc'
        | 'katana'
        | 'flamberge'
        | 'zweihander'
        | 'broadsword'
        | 'bastard sword'
        | 'war hammer'
        | 'meteor hammer'
        | 'dire flail'
        | 'war scythe'
        | 'battle axe'
        | 'halberd'
        | 'glaive'
        | 'recurve bow'
        | 'scythian bow'
        | 'crossbow'
        | 'longbow'
"""
