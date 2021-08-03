"""String templates for item info"""


ARMOR_DETAILS = """
    construction:       {secondary} {primary}
"""


ARMOR_STATS = """
    protection:         {protection: >5.2f}
    movement:           {movement: >5.2f}
    noise:              {noise: >5.2f}
    luck:               {luck: >5.2f}
"""


WEAPON_DETAILS = """
    material:           {primary} and {secondary}
"""


WEAPON_STATS = """
    damage:             {damage: >5.2f}
    range:              {range: >5.2f}
    speed:              {speed: >5.2f}
    luck:               {luck: >5.2f}
"""


ITEM_INFO = """
{name}

{description}

---

details:
    type:               {item_class} {item_type} [{item_subclass}]
    make:               {item_make}
    rarity:             {rarity}
{details}

stats:
{stats}
"""


demo = """
ornate electrum wail of shame

A faultless brigandine with spotless and immaculate
spaulders, diligently crafted from scale electrum. The
plackard, spaulders, gardbrace, and culet are all covered
in labyrinthine inscriptions, and the entire brigandine
gleams with a prismatic shimmer.

---

Type                                    Rarity          Construction
Dagger (one-handed weapon [blade])      Mythical        Meteorite and Ebony


Helm (heavy armor [head])
Cuirass (heavy armor [chest])



details:
    type:               light armor [chest]
    make:               brigandine
    rarity:             rare
    construction:       scale electrum

stats:
    protection:         39.28
    movement:           -0.18
    noise:               0.54
    luck:                6.25
"""


DESCRIPTION_INTRO = """
{condition} {make} with {parts} {made_adverb}
{made_verb} from {construction}. {details}
""".strip("\n").replace("\n", " ")


DESCRIPTION_DETAILS_ETCHINGS = """
The {constituents} are {covered} {carving_adj} {carving_noun},
and the {glisten_sentence} with {glisten_adj} {glisten_noun}.
""".strip("\n").replace("\n", " ")


DESCRIPTION_DETAILS_INLAYS_NORMAL = """
The {constituents} are {inlay_adverb} {inlay_verb} with {inlays}.
""".strip("\n").replace("\n", " ")


DESCRIPTION_DETAILS_INLAYS_MYTHICAL = """
The {parts1} {inlay_adverb1}inlaid with {inlay_noun1}, and the
{parts2} {inlay_adverb2}decorated with {inlay_noun2}.
""".strip("\n").replace("\n", " ")


DESCRIPTION_DETAILS_COMMON = """
The {part2} {adj1} and {adj2}, and the {part3}
covered {in_with} {details1} {details2}.
""".strip("\n").replace("\n", " ")


DESCRIPTION_DETAILS_SOFT = """

""".strip("\n").replace("\n", " ")
