"""Factory floor"""

# Standard Library
from random import choice, choices, sample, uniform

# Third party
import yaml

# Local
from .item import Item


with open("ItemFactory/data/materials.yml") as materials_yaml, \
     open("ItemFactory/data/constituents.yml") as constituents_yaml, \
     open("ItemFactory/data/naming.yml") as naming_yaml, \
     open("ItemFactory/data/decorations.yml") as decorations_yaml:
    MATERIALS = yaml.safe_load(materials_yaml.read())
    CONSTITUENTS = yaml.safe_load(constituents_yaml.read())
    NAMING = yaml.safe_load(naming_yaml.read())
    DECORATIONS = yaml.safe_load(decorations_yaml.read())


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
