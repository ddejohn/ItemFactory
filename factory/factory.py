"""Factory floor"""

# Standard Library
from random import choice, choices, sample, uniform

# Third party
import yaml

# Local
from .item import Item


with open("./data/materials.yml") as f:
    MATERIALS = yaml.safe_load(f.read())

with open("./data/constituents.yml") as f:
    CONSTITUENTS = yaml.safe_load(f.read())

with open("./data/naming.yml") as f:
    NAMING = yaml.safe_load(f.read())

with open("./data/decorations.yml") as f:
    DECORATIONS = yaml.safe_load(f.read())


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
    def start(item: Item):
        AssemblyLine._rarity(item)

    @staticmethod
    def _rarity(item: Item):
        if not item.rarity:
            item.rarity = _choose(ppl=AssemblyLine.weights.keys(),
                                  wts=(50, 25, 15, 6, 3, 1))
        AssemblyLine._materials(item)

    @staticmethod
    def _materials(item: Item):
        weights = AssemblyLine.weights[item.rarity]

        primary_materials = MATERIALS.get(item.category).get("primary")
        secondary_materials = MATERIALS.get(item.category).get("secondary")

        if item.category == "armor":
            primary_materials = primary_materials.get(item.base)
            secondary_materials = secondary_materials.get(item.base)
        else:
            secondary_materials = secondary_materials.get(item.rarity)

        item.primary = _choose(primary_materials, weights)
        item.secondary = choice(secondary_materials)

        AssemblyLine._constituents(item)

    @staticmethod
    def _constituents(item: Item):
        parts = CONSTITUENTS.get(item.category)

        if item.sub == "shield":
            parts = parts.get("shield")
        elif item.category == "armor":
            parts = parts.get(f"{item.base} {item.sub}")
        else:
            parts = parts.get(item.sub)

        for part in parts:
            if isinstance(part, list):
                part = choice(part)
            item.constituents.append(part)

        AssemblyLine._description(item)

    @staticmethod
    def _description(item: Item):
        _item_description(item)
        AssemblyLine._name(item)

    @staticmethod
    def _name(item: Item):
        _item_name(item)
        AssemblyLine._stats(item)

    @staticmethod
    def _stats(item: Item):
        _item_stats(item)

    @staticmethod
    def rename(item: Item):
        _item_name(item)

    @staticmethod
    def redescribe(item: Item):
        _item_description(item)


# ————————————————————————————————— helpers ————————————————————————————————— #


def _choose(ppl, wts):
    return choice(choices(population=ppl, weights=wts, k=len(ppl)))


def _shuffled(ppl) -> list:
    return sample(ppl, len(ppl))


def _fudge(x) -> float:
    return uniform(x - 0.2*x, x + 0.2*x)


def _is_are(word: str) -> str:
    if " " in word or (word[-1] == "s" and word[-2] not in "sy"):
        return f"{word} are"
    return f"{word} is"


def _set_or_pair(word: str) -> str:
    if word[-1] == "s" and word[-2] not in "uosy":
        return choice(["set", "pair"]) + f" of {word}"
    return word


def _a_an(*word: list) -> str:
    first, *rest = word
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


def _listify_words(words: list) -> str:
    *rest, last = words
    rest = ", ".join(rest)
    if rest:
        if " " not in rest:
            return f"{rest} and {last}"
        return f"{rest}, and {last}"
    return last


def paragraphize(s: str, w=50, i=""):
    new_string = i
    col = 0
    for char in s:
        new_string += char
        col += 1
        if col > w and char == " ":
            col = 0
            new_string += "\n" + i

    return new_string


# ————————————————————————————— item description ———————————————————————————— #


def _item_description(item: Item):
    condition = choice(_CONDITION[item.rarity])
    adj1, adj2, adj3, adj4 = sample(_DETAIL_ADJECTIVE[item.rarity], 4)
    verb = choice(_DETAIL_VERB[item.rarity])
    in_by = choice(("in", "with", "by"))

    part1, part2, part3 = sample(item.constituents, 3)
    construction = {
        "weapon": f"{item.primary} and {item.secondary}",
        "armor": f"{item.secondary} {item.primary}"
    }[item.category]

    softies = ["hide", "leather", "coif", "hood"]
    if item.primary in softies or item.make in softies:
        item.description = _soft_description(item, construction, in_by)

    if item.rarity in ["rare", "legendary", "mythical"]:
        details = {
            "rare": _choose([_patinas_etchings, _inlays], [5, 1]),
            "legendary": _choose([_patinas_etchings, _inlays], [3, 1]),
            "mythical": _choose([_patinas_etchings, _inlays], [2, 1])
        }.get(item.rarity)(item)
    else:
        details = _common_details(item, part2, part3, adj1, adj2)

    item.description = " ".join([
        f"{_a_an(condition).capitalize()}",
        f"{_set_or_pair(item.make)} with",
        f"{_a_an(adj3, adj4, part1)},",
        f"{verb}",
        f"{_get_make()} from {construction}.",
        details
    ])


def _soft_description(item: Item, construction, in_by):
    verbs = _shuffled(_DETAIL_VERB[item.rarity]).copy()
    nouns = _shuffled(_DETAIL_NOUN[item.rarity]).copy()
    soft_adjectives = _shuffled(_SOFT_ADJECTIVE[item.rarity]).copy()
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


def _get_details(item: Item):
    return {
        "rare": _choose([_patinas_etchings, _inlays], [5, 1]),
        "legendary": _choose([_patinas_etchings, _inlays], [3, 1]),
        "mythical": _choose([_patinas_etchings, _inlays], [2, 1])
    }.get(item.rarity, _common_details)(item)


def _inlays(item: Item):
    k = {"rare": 1, "legendary": 2, "mythical": 4}[item.rarity]
    adverb1, adverb2 = sample([f"{choice(_INLAID_ADVERB)} ", ""], 2)
    inlay_verb = choice(("decorated", "inlaid"))
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
        parts = item.constituents
        all_inlays = " ".join([
            f"The {_listify_words(parts)} are all {inlay_verb} with",
            f"{_listify_words(sample(_INLAYS, k))}."
        ])
    return all_inlays


def _patinas_etchings(item: Item):
    glisten_verb = choice(_GLISTENS_VERB)
    glisten_noun = choice(_GLISTENS_NOUN)
    glisten_adj = choice(_GLISTENS_ADJECTIVE)
    carving_noun = choice(_CARVINGS_NOUN)
    carving_adj = choice(_CARVINGS_ADJECTIVE)
    whole_entire = choice(['whole', 'entire'])
    covered = choice(["all covered in", "strewn with"])

    if item.make in ["morning star", "dire flail", "flail", "meteor hammer"]:
        general_name = "weapon"
    else:
        general_name = item.make.split()[-1]

    if item.make[-1] == "s" and item.make[-2] not in "sy":
        glisten_sentence = f"{item.make} {glisten_verb.rstrip('es')}"
    else:
        glisten_sentence = f"{whole_entire} {general_name} {glisten_verb}"

    return " ".join([
        f"The {_listify_words(item.constituents)}",
        f"are {covered} {carving_adj} {carving_noun},",
        f"and the {glisten_sentence} with {_a_an(glisten_adj)} {glisten_noun}."
    ])


def _common_details(item: Item, part2, part3, adj1, adj2):
    detail1, detail2 = sample(_DETAIL_NOUN[item.rarity], 2)
    in_with = choice(("in", "with"))

    return " ".join([
        f"The {_is_are(part2)}",
        f"{adj1} and {adj2}, and the {_is_are(part3)}",
        f"covered {in_with} {detail1} and {detail2}."
    ])


def _get_make():
    return choice([
        "shaped",
        "crafted",
        "formed",
        "fashioned",
        "forged",
        "cast",
        "hewn",
        "made",
        "constructed",
        "assembled"
    ])


# ———————————————————————————————— item name ———————————————————————————————— #


def _item_name(item: Item):
    new_name = []

    if item.category == "armor":
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


def _rare_name(item: Item):
    adjective = choice(_ADJECTIVES)
    abstract = choice(_ABSTRACT)
    noun = choice(_NOUNS)
    return choice([
        [adjective, item.primary, item.make],
        [adjective, item.primary, noun, abstract],
        [adjective, item.primary, item.make, abstract],
    ])


def _legendary_name(item: Item):
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
    ])


def _mythical_name(item: Item):
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
    ])


def _common_name(item: Item):
    if item.primary not in ["hide", "leather"]:
        return choice([
            [item.rarity, item.primary, item.make],
            [choice(_CONDITION[item.rarity]), item.primary, item.make]
        ])
    return choice([
        [item.rarity, item.primary, item.make],
        [choice(_SOFT_ADJECTIVE[item.rarity]), item.primary, item.make]
    ])


# ——————————————————————————————— item stats ———————————————————————————————— #


def _item_stats(item: Item):
    item.stats = {
        "weapon": _weapon_stats,
        "armor": _armor_stats
    }[item.category](item)


def _weapon_stats(item: Item):
    stats = _WEAPON_STAT_DATA["stats"][item.rarity]
    mults = _WEAPON_STAT_DATA["mults"][item.sub]
    wt = {"one-handed": 0.7}.get(item.sub, 1)
    d, r, s, k = [round(wt * _fudge(x * y), 2) for x, y in zip(stats, mults)]

    return {
        "damage": d,
        "range": r,
        "speed": s,
        "luck": k
    }


def _armor_stats(item: Item):
    stats = _ARMOR_STAT_DATA["stats"][item.rarity]
    mults = _ARMOR_STAT_DATA["mults"][item.sub]
    wt = {"heavy": 2}.get(item.base, 1)
    combs = [wt * _fudge(x * y) for x, y in zip(stats, mults)]
    p, m, n, k = [round(x, 2) for x in combs]

    return {
        "protection": p,
        "movement": m,
        "noise": n,
        "luck": k
    }


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