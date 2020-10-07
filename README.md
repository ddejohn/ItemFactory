# ItemFactory

_A random weapon and armor generator which provides richly detailed descriptions, unique names, and basic item stats for fantasy world building._

**ItemFactory** generates items loosely based on the names and constituent pieces of common medieval weapons and armor.

## Examples

```
name:             ornate electrum wail of shame
class:            light armor [chest]
type:             brigandine
rarity:           rare
material:         electrum
construction:     scale

stats:
    protection:   39.28
    movement:     -0.18
    noise:        0.54
    luck:         6.25

description:
    A faultless brigandine with spotless and immaculate
    spaulders, diligently crafted from scale electrum. The
    plackard, spaulders, gardbrace, and culet are all covered
    in labyrinthine inscriptions, and the entire brigandine
    gleams with a prismatic shimmer.
```

```
name:             blighted iron halberd
class:            two-handed weapon [axe]
type:             halberd
rarity:           crude
materials:        iron, cracked wood

stats:
    damage:       7.71
    range:        3.16
    speed:        2.28
    luck:         2.61

description:
    A lousy halberd with a gnarled and scratched haft,
    inexpertly fashioned from iron and cracked wood. The
    pommel is pitted and bent, and the beard is covered
    with bits of fur and gashes.
```

## Item rarity probabilities

Items are generated with the following probabilities, unless the user choses to generate their own item. In the future, I may add a feature to allow the user to input their own probabilities.

| rarity | probability |
|-|:-:|
| crude | 0.50 |
| common | 0.25 |
| uncommon | 0.15 |
| rare | 0.06 |
| legendary | 0.03 |
| mythical | 0.01 |

## Materials

Each item's material depends on its rarity. Weapons get a secondary material, while armor gets a construction method descriptor. Both secondary materials and construction methods are chosen with equal probability for weapons and armor, respectively.

### Weapons

| rarity | material (probability) | secondary material |
|-|:-:|:-:|
| crude | **iron** (0.91), **steel** (0.09) | splintered wood, cracked wood, warped wood |
| common | **iron** (0.083), **steel** (0.833), **bone** (0.084) | ash, maple, beech, hickory |
| uncommon | **steel** (0.083), **bone** (0.833), **obsidian** (0.084) | maple, beech, hickory, mahogany |
| rare | **bone** (0.083), **obsidian** (0.833), **electrum** (0.084) | hickory, mahogany, walnut, cherry |
| legendary | **obsidian** (0.083), **electrum** (0.833), **adamantite** (0.084) | walnut, cherry, birch, korina |
| mythical | **adamantite** (0.91), **meteorite** (0.09) | bloodwood, ebony, black walnut, purpleheart |

### Armor

Light armor is produced using either *lamellar* or *scale* construction methods. Heavy armor is produced using either *plate* or *laminar* construction methods.

| rarity | light armor material (probability) | heavy armor material (probability) |
|-|:-:|:-:|
| crude | **hide** (0.91), **leather** (0.09) | **iron** (0.91), **steel** (0.09) |
| common | **hide** (0.083), **leather** (0.833), **obsidian** (0.084) | **iron** (0.083), **steel** (0.833), **obsidian** (0.084) |
| uncommon | **leather** (0.083), **obsidian** (0.833), **electrum** (0.084) | **steel** (0.083), **obsidian** (0.833), **bone** (0.084) |
| rare | **obsidian** (0.083), **electrum** (0.833), **bone** (0.084) | **obsidian** (0.083), **bone** (0.833), **onyx** (0.084) |
| legendary | **electrum** (0.083), **bone** (0.833), **adamantite** (0.084) | **bone** (0.083), **onyx** (0.833), **adamantite** (0.084) |
| mythical | **adamantite** (0.91), **meteorite** (0.09) | **adamantite** (0.91), **meteorite** (0.09) |

## Weapon types

Weapons fall into two major categories, _one-handed_ and _two-handed,_ and four sub-types, _blade,_ _blunt,_ _axe,_ _ranged_ (note: _ranged_ weapons are only available in the _two-handed_ category). All weapons are generated with equal probability.

```yaml
weapon:
    one-handed:
        blade:
            - dagger
            - corvo
            - stiletto
            - shortsword
            - seax
            - xiphos
            - baselard
            - gladius
        blunt:
            - morning star
            - mace
            - club
            - flail
        axe:
            - labrys
            - hatchet
    two-handed:
        blade:
            - longsword
            - claymore
            - broadsword
            - bastard sword
        blunt:
            - war hammer
            - meteor hammer
            - dire flail
        axe:
            - war scythe
            - battle axe
            - halberd
            - glaive
        ranged:
            - recurve bow
            - scythian bow
            - crossbow
            - longbow
```

## Armor pieces

There are five basic types of armor, each of which has a heavy and a light variant. All armor items are generated with equal probability.

```yaml
armor:
    heavy:
        head:
            - helm
            - helmet
        chest:
            - cuirass
            - corslet
        hands:
            - gauntlets
            - gloves
        feet:
            - boots
            - sabatons
        shield:
            - pavise shield
            - kite shield
    light:
        head:
            - hood
            - coif
        chest:
            - brigandine
            - gambeson
        hands:
            - gloves
        feet:
            - boots
        shield:
            - buckler
            - targe shield
```

## Item parts

### Weapons

Each item gets a list of three to five parts chosen randomly according to the item type, and which are used in the generation of the item's description.

Some examples of item parts:

**blunt:** `throat`, `cheek`, `flange`, `face`, `crown`, `haft`, `handle`, `grip`

**bow:** `nock`, `face`, `hilt`, `grip`, `limbs`, `belly`

**heavy chest:** `breastplate`, `pauldrons`, `faulds`, `gardbrace`, `tasset`

**light hands:** `rerebraces`, `cuffs`, `lower cannons`, `vambraces`, `carpal plates`, `wrist plates`

## Names

Item names are determined by the item's type, rarity, and material.

My personal favorites I've seen so far: `copper tooth of dusk`, `god husher`

## Descriptions

Item descriptions are generated based on the item's type, rarity, material, and sub-type.

## Stats

Item stats are a function of the item's type, rarity, and sub-type. Note that these are very basic generic stats, and don't follow any particular gameworld's mechanics.

Each stat type has a base-value, and each item type has a multiplier for that stat value (e.g., claymores have a higher range multiplier than do daggers).

### Weapons

`damage`: the base damage level of the weapon

`range`: the effective range of the weapon

`speed`: how quickly the weapon can be handled

`luck`: determines the chance of a critical hit

### Armor

`protection`: the base level of protection this armor provides

`movement`: the player movement speed penalty attributed to this piece

`noise`: how much of a racket this armor produces during movement while wearing

`luck`: chance of critical hit from an enemy

## Possible Feature Additions

* Allow the user to design their own item stats
* I've looked into possibly designing a GUI, but I quite like using the terminal
* Allow the user to design their own word banks, or add to the existing ones
