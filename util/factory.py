"""Factory floor"""

import yaml
from random import choice, choices, sample, uniform


with open("ItemFactory/data/materials.yml") as f:
    MATERIALS = yaml.safe_load(f.read())
# end


with open("ItemFactory/data/constituents.yml") as f:
    CONSTITUENTS = yaml.safe_load(f.read())
# end


class ItemBase:
    def __init__(self, template: list):
        self.item_class, self.base_type, self.sub_type, self.make = template
        self.rarity = str
        self.primary = str
        self.secondary = str
        self.constituents = []
    # end
# end


class Item(ItemBase):
    def __init__(self, template=["", "", "", ""]):
        super().__init__(template)
        self.name = str
        self.description = str
        self.stats = dict
        AssemblyLine.start(self)
    # end

    def __str__(self):
        w = 18
        stats = "\n"
        clss = f"{self.base_type} {self.item_class} [{self.sub_type}]"
        if self.item_class == "armor":
            mat = "material:".ljust(w) + f"{self.primary}\n"
            mat += "construction:".ljust(w) + f"{self.secondary}"
        else:
            mat = "materials:".ljust(w) + f"{self.primary}, {self.secondary}"
        for k,v in self.stats.items():
            stats += f"  {k}:".ljust(w) + f"{v}\n"

        desc_words = self.description.split()
        desc_line = ""
        desc_lines = []
        for word in desc_words:
            desc_line += f" {word}"
            if len(desc_line) > 50:
                desc_lines.append(desc_line)
                desc_line = ""
            # end
        rem = len(desc_words) - len(" ".join(desc_lines).split())
        if rem != 0:
            desc_lines[-1] += "\n" + " ".ljust(w) + " ".join(desc_words[-rem:])
        # end
        desc = ("\n" + " "*(w-1)).join(desc_lines)
        out = [
            "name:".ljust(w) + f"{self.name}",
            "class:".ljust(w) + clss,
            "type:".ljust(w) + f"{self.make}",
            "rarity:".ljust(w) + f"{self.rarity}",
            mat,
            "description:".ljust(w-1) + desc,
            "stats:".ljust(w) + stats
        ]
        return "\n".join(out)
    # end
# end


class AssemblyLine:
    weights = {
        "crude":        [50, 5, 0, 0, 0, 0, 0],
        "common":       [5, 50, 5, 0, 0, 0, 0],
        "uncommon":     [0, 5, 50, 5, 0, 0, 0],
        "rare":         [0, 0, 5, 50, 5, 0, 0],
        "legendary":    [0, 0, 0, 0, 5, 50, 5],
        "mythical":     [0, 0, 0, 0, 0, 5, 50]
    }

    @staticmethod
    def start(item: 'Item'):
        AssemblyLine.__rarity(item)
    # end

    @staticmethod
    def __rarity(item: 'Item'):
        item.rarity = _choose(
            ppl=list(AssemblyLine.weights.keys()),
            wts=[50, 25, 15, 4, 2, 1]
        )
        AssemblyLine.__materials(item)
    # end

    @staticmethod
    def __materials(item: 'Item'):
        weights = AssemblyLine.weights[item.rarity]

        primary_materials = MATERIALS.get(item.item_class).get("primary")
        secondary_materials = MATERIALS.get(item.item_class).get("secondary")

        if item.item_class == "armor":
            primary_materials = primary_materials.get(item.base_type)
            secondary_materials = secondary_materials.get(item.base_type)
        elif item.item_class == "weapon":
            secondary_materials = secondary_materials.get(item.rarity)

        item.primary = _choose(primary_materials, weights)
        item.secondary = choice(secondary_materials)

        AssemblyLine.__constituents(item)
    # end

    @staticmethod
    def __constituents(item: 'Item'):
        parts = CONSTITUENTS.get(item.item_class)

        if item.sub_type == "shield":
            parts = parts.get("shield")
        elif item.item_class == "armor":
            parts = parts.get(f"{item.base_type} {item.sub_type}")
        else:
            parts = parts.get(item.sub_type)
        
        for part in parts:
            if isinstance(part, list):
                part = choice(part)
            item.constituents.append(part)

        AssemblyLine.__description(item)
    # end

    @staticmethod
    def __description(item: 'Item'):
        _item_description(item)
        AssemblyLine.__name(item)
    # end

    @staticmethod
    def __name(item: 'Item'):
        _item_name(item)
        AssemblyLine.__stats(item)
    # end

    @staticmethod
    def __stats(item: 'Item'):
        _item_stats(item)
    # end
# end


#—————————————————————————————————— helpers ——————————————————————————————————#


def _choose(ppl, wts):
    return choice(choices(population=ppl, weights=wts, k=len(ppl)))
# end


def _shuffled(ppl):
    return sample(ppl, len(ppl))
# end


def _variance(x) -> float:
    return uniform(x-0.3*x, x+0.3*x)
# end


def _is_are(this: str) -> str:
    if " " in this or (this[-1] == "s" and this[-2] != "y"):
        return f"{this} are"
    return f"{this} is"
# end


def _set_or_pair(this: str) -> str:
    if this[-1] == "s" and this[-2] not in "uosy":
        return choice(["set", "pair"]) + f" of {this}"
    return this
# end


def _a_an(*this: list) -> str:
    first, *rest = this
    if rest:
        rest = " ".join(rest)
        if " " in rest:
            rest = f" and {rest}"
        else:
            rest = f" {rest}"
    else:
        rest = ""
    if rest and rest[-1] == "s":
        return f"{first}{rest}"
    elif first[0] in "aeiou":
        return f"an {first}{rest}"
    return f"a {first}{rest}"
# end


def _listify_words(this: list) -> str:
    *rest, last = this
    rest = ", ".join(rest)
    if rest:
        if " " not in rest:
            return f"{rest} and {last}"
        return f"{rest}, and {last}"
    return last
# end


#—————————————————————————————— item description —————————————————————————————#


def _item_description(item: 'Item'):
    softies = ["hide", "leather", "coif", "hood"]
    condition = _shuffled(_CONDITION[item.rarity])
    adjective = _shuffled(_DETAIL_ADJECTIVE[item.rarity])

    in_by = choice(["in", "with", "by"])
    construction = {
        "weapon": f"{item.primary} and {item.secondary}",
        "armor": f"{item.secondary} {item.primary}"
    }[item.item_class]

    parts = item.constituents.copy()
    part1 = parts.pop(choice([*range(len(parts))]))
    part2 = parts.pop(choice([*range(len(parts))]))
    part3 = parts.pop(choice([*range(len(parts))]))

    if item.primary in softies or item.make in softies:
        item.description = _soft_description(item, construction, in_by)

    if item.rarity in ["rare", "legendary", "mythical"]:
        details = {
            "rare": _choose([_patinas_etchings, _inlays], [5, 1]),
            "legendary": _choose([_patinas_etchings, _inlays], [3, 1]),
            "mythical": _choose([_patinas_etchings, _inlays], [2, 1])
        }.get(item.rarity)(item)
    else:
        details = _common_details(item, part2, part3)

    item.description = " ".join([
        f"{_a_an(condition.pop()).capitalize()}",
        f"{_set_or_pair(item.make)} with",
        f"{_a_an(adjective.pop(), adjective.pop(), part1)},",
        f"{_shuffled(_DETAIL_VERB[item.rarity]).pop()}",
        f"{_get_make()} from {construction}.",
        details
    ])
# end


def _soft_description(item: 'Item', construction, in_by):
    verbs = _shuffled(_DETAIL_VERB[item.rarity])
    nouns = _shuffled(_DETAIL_NOUN[item.rarity])
    soft_adjectives = _shuffled(_SOFT_ADJECTIVE[item.rarity])
    if item.rarity in ["rare", "legendary", "mythical"]:
        qualities = ""
        second_sentence = _get_details(item)
    else:
        qualities = f"{soft_adjectives.pop()} and {soft_adjectives.pop()} "
        second_sentence = " ".join([
            f"The {_listify_words(item.constituents)} are all covered {in_by}",
            f"{nouns.pop()} and {nouns.pop()}."
        ])
    return " ".join([
        f"{(_a_an(soft_adjectives.pop()).capitalize())}",
        f"{_set_or_pair(item.make)} {verbs.pop()}",
        f"{_get_make()} from {qualities}{construction}.",
        second_sentence
    ])
# end


def _inlays(item: 'Item'):
    k = {"rare": 1, "legendary": 2, "mythical": 4}[item.rarity]
    if k == 4:
        parts = _shuffled(item.constituents)
        inlays = sample(_INLAYS, k)
        parts_one, parts_two = parts[:2], parts[2:]
        inlays_one, inlays_two = inlays[:2], inlays[2:]
        all_inlays = " ".join([
            f"The {_is_are(_listify_words(parts_one))}",
            f"inlaid with {_listify_words(inlays_one)},",
            f"and the {_is_are(_listify_words(parts_two))} decorated with",
            choice([
                f"{_listify_words(inlays_two)} insets.",
                f"insets of {_listify_words(inlays_two)}."
            ])
        ])
    else:
        all_inlays = " ".join([
            f"The {_listify_words(item.constituents)} are all inlaid with",
            f"{_listify_words(sample(_INLAYS, k))}."
        ])
    return all_inlays
# end


def _patinas_etchings(item: 'Item'):
    if item.make in ["morning star", "dire flail", "flail", "meteor hammer"]:
        general_name = "weapon"
    else:
        general_name = item.make.split()[-1]
    if item.make[-1] == "s" and item.make[-2] not in ["s", "y"]:
        second_sentence = item.make
        glisten_choice = choice(_GLISTENS_VERB).rstrip("es")
    else:
        second_sentence = f"{choice(['whole', 'entire'])} {general_name}"
        glisten_choice = choice(_GLISTENS_VERB)
    return " ".join([
        f"The {_listify_words(item.constituents)}",
        f"are all covered in {choice(_CARVINGS_ADJECTIVE)}",
        f"{choice(_CARVINGS_NOUN)}, and the",
        f"{second_sentence} {glisten_choice}",
        f"with {_a_an(choice(_GLISTENS_ADJECTIVE))} {choice(_GLISTENS_NOUN)}."
    ])
# end


def _common_details(item: 'Item', part2, part3):
    details = _shuffled(_DETAIL_NOUN[item.rarity])
    adjective = _shuffled(_DETAIL_ADJECTIVE[item.rarity])
    in_by = choice(["in", "with", "by"])
    return " ".join([
        f"The {_is_are(part2)}",
        f"{adjective.pop()} and {adjective.pop()}, and the",
        f"{_is_are(part3)}",
        f"covered {in_by} {details.pop()} and {details.pop()}."
    ])
# end


def _get_make():
    return choice([
        "shaped",
        "formed",
        "fashioned",
        "made",
        "constructed",
        "assembled"
    ])
# end


#————————————————————————————————— item name —————————————————————————————————#


def _item_name(item: 'Item'):
    new_name = []

    if item.item_class == "armor":
        if item.rarity in ["rare", "legendary", "mythical"]:
            new_name.extend(_rare_name(item))
        else:
            new_name.extend(_common_name(item))

    else:
        new_name.extend({
            "rare": _rare_name,
            "legendary": _legendary_name,
            "mythical": _mythical_name
        }.get(item.rarity, _common_name)(item))

    item.name = " ".join(new_name)
# end


def _rare_name(item: 'Item'):
    adjective = choice(_ADJECTIVES)
    abstract = choice(_ABSTRACT)
    noun = choice(_NOUNS)
    return choice([
        [adjective, item.primary, item.make],
        [adjective, item.primary, noun, abstract],
        [adjective, item.primary, item.make, abstract],
    ])
# end


def _legendary_name(item: 'Item'):
    adjective = choice(_ADJECTIVES)
    abstract = choice(_ABSTRACT)
    noun = choice(_NOUNS)
    prefix = choice(_PREFIXES)
    return choice([
        [adjective, item.make, abstract],
        [adjective, item.primary, item.make, abstract],
        [adjective, noun, abstract],
        [adjective, item.primary, noun],
        [adjective, noun, "of " + item.primary],
        [adjective, item.primary, noun, abstract],
        [item.primary, prefix, abstract],
        [item.primary, noun, abstract],
        _rare_name(item)
    ])
# end


def _mythical_name(item: 'Item'):
    adjective = choice(_ADJECTIVES)
    abstract = choice(_ABSTRACT)
    noun = choice(_NOUNS)
    verb = choice(_VERBS)
    prefix = choice(_PREFIXES)
    glisten = choice(_GLISTENS_ADJECTIVE)
    inlay = choice(_INLAYS)
    return choice([
        [glisten, noun, "of " + inlay],
        [glisten, noun, abstract],
        [adjective, noun, "of " + inlay],
        [adjective, noun, abstract],
        [inlay, noun, abstract],
        [noun, abstract],
        [adjective, noun + " of the", prefix],
        [prefix, verb],
        _legendary_name(item)
    ])
# end


def _common_name(item: 'Item'):
    if item.primary not in ["hide", "leather"]:
        return choice([
            [item.rarity, item.primary, item.make],
            [choice(_CONDITION[item.rarity]), item.primary, item.make]
        ])
    return choice([
        [item.rarity, item.primary, item.make],
        [choice(_SOFT_ADJECTIVE[item.rarity]), item.primary, item.make]
    ])
# end


#———————————————————————————————— item stats —————————————————————————————————#


def _item_stats(item: 'Item'):
    item.stats = {
        "weapon": _weapon_stats,
        "armor": _armor_stats
    }[item.item_class](item)
# end


def _weapon_stats(item: 'Item'):
    stats = _WEAPON_STAT_DATA["stats"][item.rarity]
    mults = _WEAPON_STAT_DATA["mults"][item.sub_type]
    wt = {"one-handed": 0.7}.get(item.sub_type, 1)
    combs = [round(wt*_variance(x*y), ndigits=2) for x, y in zip(stats, mults)]

    return {
        "damage": combs[0],
        "range": combs[1],
        "speed": combs[2],
        "luck": combs[3]
    }
# end


def _armor_stats(item: 'Item'):
    stats = _ARMOR_STAT_DATA["stats"][item.rarity]
    mults = _ARMOR_STAT_DATA["mults"][item.sub_type]
    wt = {"heavy": 2}.get(item.base_type, 1)
    combs = [round(wt*_variance(x*y), ndigits=2) for x, y in zip(stats, mults)]

    return {
        "protection": combs[0],
        "movement": combs[1],
        "noise": combs[2],
        "luck": combs[3]
    }
# end


#——————————————————————————————————— data ————————————————————————————————————#


_WEAPON_STAT_DATA = {
    "stats": {
        # attack range speed luck
        "crude":        [6.0, 3.0, 3.0, 2.0],
        "common":       [10.0, 3.0, 4.0, 3.0],
        "uncommon":     [20.0, 4.0, 5.0, 5.0],
        "rare":         [35.0, 5.0, 6.0, 7.0],
        "legendary":    [50.0, 6.0, 7.0, 7.0],
        "mythical":     [80.0, 7.0, 7.0, 8.0]
    },
    "mults": {
        # attack range speed luck
        "blade":        [1.1, 1.1, 0.8, 0.9],
        "axe":          [1.2, 0.9, 0.9, 1.3],
        "blunt":        [0.9, 0.8, 1.3, 1.2],
        "ranged":       [1.3, 3.0, 1.2, 0.7]
    }
}


_ARMOR_STAT_DATA = {
    "stats": {
        # protection movement noise luck
        "crude":        [4.0, 1.0, 5.0, 1.0],
        "common":       [8.0, 1.0, 3.0, 2.0],
        "uncommon":     [10.0, 0.5, 2.0, 4.0],
        "rare":         [14.0, 0.125, 0.5, 5.0],
        "legendary":    [20.0, 0.025, 0.05, 12.0],
        "mythical":     [40.0, 0.0125, 0.025, 16.0]
    },
    "mults": {
        # protection movement noise luck
        "head":         [1.0, -1.0, 0.5, 1.0],
        "chest":        [3.0, -1.5, 1.5, 1.0],
        "hands":        [0.5, -0.5, 0.5, 1.0],
        "feet":         [1.5, -0.5, 0.25, 1.0],
        "shield":       [2.0, -1.2, 1.25, 1.0]
    }
}


#———————————————————————————————— decorations ————————————————————————————————#


_INLAYS = [
    "gold",
    "silver",
    "onyx",
    "obsidian",
    "amethyst",
    "emerald",
    "ruby",
    "jade",
    "turquoise",
    "zircon",
    "howlite",
    "bloodstone",
    "topaz",
    "sardonyx",
    "gypsum",
    "opal",
    "coral",
    "moonstone",
    "sapphire",
    "spessartine",
    "charoite",
    "copper",
    "pearl"
]


_GLISTENS_VERB = [
    "glistens",
    "gleams",
    "glimmers",
    "twinkles",
    "flashes",
    "radiates",
    "beams",
    "glows",
    "glitters"
]


_GLISTENS_ADJECTIVE = [
    "rainbow",
    "verdigris",
    "prismatic",
    "opalescent",
    "nacreous",
    "variegated",
    "iridescent"
]


_GLISTENS_NOUN = [
    "patina",
    "shimmer",
    "shine",
    "sheen",
    "brilliance",
    "luster",
    "finish",
]


_CARVINGS_ADJECTIVE = [
    "intricate",
    "elaborate",
    "detailed",
    "elegant",
    "sophisticated",
    "complex",
    "labyrinthine",
    "minute",
]


_CARVINGS_NOUN = [
    "carvings",
    "etchings",
    "patterns",
    "inscriptions",
    "engravings"
]


_SOFT_ADJECTIVE = {
    "crude": [
        "scratched",
        "distressed",
        "chewed",
        "gnarled",
        "scored",
    ],
    "common": [
        "scratched",
        "burnished",
        "scored",
        "distressed"
    ],
    "uncommon": [
        "burnished",
        "fine",
        "satin"
    ],
    "rare": [
        "fine",
        "satin",
        "engraved"
    ],
    "legendary": [
        "fine",
        "satin",
        "engraved"
    ],
    "mythical": [
        "fine",
        "satin",
        "engraved"
    ]
}


_DETAIL_ADJECTIVE = {
    "crude": [
        "scratched",
        "pitted",
        "rusted",
        "distressed",
        "chewed",
        "gnarled",
        "bent",
        "scored",
        "burred"
    ],
    "common": [
        "scratched",
        "burred",
        "burnished",
        "scored",
        "pitted",
        "rusted",
        "distressed"
    ],
    "uncommon": [
        "burnished",
        "distressed",
        "scratched",
        "worn",
        "dull",
        "rough"
    ],
    "rare": [
        "polished",
        "smooth",
        "elegant",
        "immaculate",
        "spotless"
    ],
    "legendary": [
        "ornate",
        "engraved",
        "embossed",
        "gilded",
        "elaborate"
    ],
    "mythical": [
        "ornate",
        "engraved",
        "embossed",
        "gilded",
        "elaborate"
    ]
}


_DETAIL_NOUN = {
    "crude": [
        "dried blood",
        "dirt",
        "dust",
        "claw marks",
        "scratches",
        "gashes",
        "notches",
        "bits of fur",
        "teeth marks"
    ],
    "common": [
        "dried blood",
        "dirt",
        "claw marks",
        "scratches",
        "filth",
        "smudges",
    ],
    "uncommon": [
        "smudges",
        "grit",
        "scratches",
        "soot",
        "residue"
    ],
    "rare": [],
    "legendary": [],
    "mythical": []
}


_DETAIL_VERB = {
    "crude": [
        "haphazardly",
        "shoddily",
        "crudely",
        "defectively",
        "inexpertly",
        "poorly",
        "hastily"
    ],
    "common": [
        "haphazardly",
        "hastily",
        "inexpertly",
        "adequately",
        "competently"
    ],
    "uncommon": [
        "adequately",
        "competently",
        "sufficiently",
        "decently",
        "capably"
    ],
    "rare": [
        "meticulously",
        "skillfully",
        "precisely",
        "diligently",
        "fastidiously"
    ],
    "legendary": [
        "expertly",
        "elegantly",
        "masterfully",
        "flawlessly"
    ],
    "mythical": [
        "expertly",
        "elegantly",
        "masterfully",
        "flawlessly"
    ]
}


_CONDITION = {
    "crude": [
        "ruined",
        "rusty",
        "marred",
        "deformed",
        "lousy",
        "mediocre",
        "dreadful",
        "inferior",
        "substandard",
        "tarnished",
        "blighted",
        "filthy",
        "decrepit"
    ],
    "common": [
        "worn",
        "chipped",
        "blemished",
        "flawed",
        "mediocre",
        "common",
        "middling",
        "tarnished",
        "neglected",
        "mended"
    ],
    "uncommon": [
        "fair",
        "passable",
        "acceptable",
        "adequate",
        "blemished",
        "tarnished",
        "mended"
    ],
    "rare": [
        "fine",
        "exceptional",
        "refined",
        "superior",
        "unblemished",
        "faultless",
        "pristine"
    ],
    "legendary": [
        "flawless",
        "immaculate",
        "pristine",
        "exquisite",
        "superior",
        "refined",
        "impeccable",
        "superb"
    ],
    "mythical": [
        "flawless",
        "immaculate",
        "pristine",
        "exquisite",
        "superior",
        "refined",
        "impeccable"
    ]
}


#——————————————————————————————————— names ———————————————————————————————————#


_ABSTRACT = [
    "of blooding",
    "of humiliation",
    "of hubris",
    "of spite",
    "of death",
    "of life",
    "of bones",
    "of regret",
    "of dread",
    "of sorrow",
    "of screams",
    "of lust",
    "of carving",
    "of surprise",
    "of confusion",
    "of frenzy",
    "of breaking",
    "of loathing",
    "of sickness",
    "of poisons",
    "of tragedy",
    "of souls",
    "of rotting",
    "of governing",
    "of ecstasy",
    "of torpor",
    "of truth",
    "of lies",
    "of victory",
    "of ambition",
    "of vengeance",
    "of somnolence",
    "of joy",
    "of corruption",
    "of erosion",
    "of jubilance",
    "of merit",
    "of witching",
    "of burdens",
    "of honor",
    "of repulsion",
    "of reckoning",
    "of mourning",
    "of grieving",
    "of judgement",
    "of battering",
    "of hell",
    "of starlight",
    "of scorching",
    "of smite",
    "of waning",
    "of smiting",
    "of diffusion",
    "of mummification",
    "of crushing",
    "of extraction",
    "of valor",
    "of fear",
    "of firestorms",
    "of icestorms",
    "of ice",
    "of thunder",
    "of lightning",
    "of hatred",
    "of terror",
    "of ruin",
    "of storms",
    "of ruining",
    "of fury",
    "of disgust",
    "of friendship",
    "of calming",
    "of shame",
    "of pity",
    "of envy",
    "of suffering",
    "of tears",
    "of disdain",
    "of putrification",
    "of contempt",
    "of mediocrity",
    "of misery",
    "of thorns",
    "of light",
    "of dark",
    "of darkness",
    "of dawn",
    "of dusk",
    "of herecy",
    "of twilight",
    "of maleficence",
    "of brutality",
    "of savagery",
    "of malice",
    "of quickening",
    "of grace",
    "of disintegration",
    "of disintegrating",
    "of embalming",
    "of destruction",
    "of exsanguination",
    "of the hunt",
    "of the grotesque",
    "of the heretic",
    "of the prophet",
    "of the night",
    "of the stars",
    "of the storm",
    "of the shamed",
    "of the hated",
    "of the dawn",
    "of the dusk",
    "of the morning"
]


_ADJECTIVES = [
    "ghastly",
    "addictive",
    "gilded",
    "beautiful",
    "valorous",
    "ancient",
    "magnificent",
    "strange",
    "dreaded",
    "fearful",
    "splendid",
    "horrible",
    "luminous",
    "furious",
    "shameful",
    "friendly",
    "piteous",
    "weeping",
    "splendiferous",
    "loathsome",
    "blunderous",
    "magnetic",
    "electric",
    "burning",
    "brutal",
    "savage",
    "graceful",
    "volcanic",
    "uncanny",
    "spectral",
    "sinister",
    "ornate",
    "bloody",
    "ashen",
    "gleaming",
    "glittering",
    "eldritch",
    "eerie",
    "elegant",
    "exquisite",
    "munificent",
    "mirthful",
    "noxious",
    "nefarious",
    "repulsive",
    "freakish",
    "bewitched",
    "repugnant",
    "exotic",
    "burdensome",
    "vigilant",
    "bewildering",
    "chosen",
    "dazzling",
    "dusky",
    "putrid",
    "unpleasant",
    "bizarre",
    "frenzied",
    "stormy",
    "erosive",
    "vengeful",
    "somnolent",
    "opulent",
    "lustrous",
    "hideous",
    "insideous",
    "spiteful",
    "ugly",
    "thorny",
    "barbed",
    "ghoulish",
    "soulless",
    "corrupted",
    "envious",
    "grotesque",
    "weeping"
]


_PREFIXES = [
    "wolf",
    "troll",
    "goliath",
    "raven",
    "dragon",
    "crow",
    "widow",
    "thorn",
    "wraith",
    "skull",
    "spine",
    "doom",
    "death",
    "hate",
    "bone",
    "fear",
    "soul",
    "sky",
    "mind",
    "god",
    "star",
    "shadow",
    "sun",
    "moon",
    "storm"
]


_VERBS = [
    "ripper",
    "eater",
    "stealer",
    "absorber",
    "shredder",
    "bruiser",
    "seer",
    "destroyer",
    "killer",
    "purger",
    "bearer",
    "corruptor",
    "preacher",
    "defier",
    "husher",
    "defiler",
    "dredger",
    "mutilator",
    "adder",
    "breaker",
    "scorcher",
    "maker",
    "bringer",
    "slayer"
]


_NOUNS = [
    "eye",
    "fang",
    "claw",
    "bane",
    "marrow",
    "thorn",
    "crown",
    "heart",
    "blood",
    "wail",
    "tooth"
]
