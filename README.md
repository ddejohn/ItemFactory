# ItemFactory

> *A random weapon and armor generator which provides richly detailed descriptions, unique names, and basic item stats*

**ItemFactory** generates items loosely based on the names and constituent pieces of common medieval weapons and armor. There are more than 10^24^ possible combinations of items alone, not counting the possible names and descriptions!

## Examples

```
name: worn steel battle axe
description: A blemished battle axe with a pitted and rusted haft, adequately constructed from steel and ash. The pommel is distressed and scratched, and the hook is covered in scratches and claw marks.
stats:
    damage: 13.16
    range: 3.08
    speed: 4.63
    luck: 3.8


name: chewed hide boots
description: A mediocre set of boots with a rusted and gnarled cuisse, haphazardly formed from hide. The greaves are scored and pitted, and the cuisse is covered by notches and gashes.
stats:
    protection: 7.28
    movement: -0.4
    noise: 1.2
    luck: 0.89


name: rare onyx helmet
description: A superior helmet with an elegant and smooth visor, meticulously made from plate onyx. The visor, comb, and gorget are all covered in complex etchings, and the entire helmet glistens with a rainbow shimmer.
stats:
    protection: 22.26
    movement: -0.25
    noise: 0.6
    luck: 12.32


name: furious obsidian war scythe
description: A faultless war scythe with a smooth and polished grip, fastidiously assembled from obsidian and cherry. The fuller, pommel, grip, and cross-guard are all inlaid with silver.
stats:
    damage: 34.32
    range: 6.17
    speed: 5.93
    luck: 5.1


name: fear shredder
description: An immaculate claymore with an engraved and ornate pommel, masterfully formed from meteorite and ebony. The pommel and hilt are inlaid with sardonyx and copper, and the fuller and cross-guard are decorated with bloodstone and sapphire insets.
stats:
    damage: 92.42
    range: 5.76
    speed: 6.67
    luck: 8.69
    

name: soul's marrow
description: An immaculate longbow with a gilded and elaborate face, flawlessly fashioned from adamantite and black walnut. The belly and limbs are inlaid with pearl and coral, and the face, nock, and grip are decorated with obsidian and copper insets.
stats:
    damage: 106.28
    range: 17.48
    speed: 10.67
    luck: 5.39
```

## Item Rarity and Item Material

There are six item rarity tiers for both weapons and armor.

### Probabilities

| Rarity    | Probability |
| :-------- | :---------: |
| crude     |   51.55%    | 
| common    |   25.77%    |
| uncommon  |   15.46%    |
| rare      |    4.12%    |
| legendary |    2.07%    |
| mythical  |    1.03%    |

### Materials

Each item's material depends on its rarity. Weapons get a secondary material, while armor gets a construction method descriptor.

#### Weapons

| Rarity   |                      Material (probability)                    |
| -------- | :-------------------------------------------------------------:|
| crude    |  **iron** (76.9%), **steel** (23.1%)                           |
| common   |  **iron** (18.75%), **steel** (62.5%), **bone** (18.75%)       |
| uncommon |  **steel** (18.75%), **bone** (62.5%), **obsidian** (18.75%)   |
| rare     |  **bone** (18.75%), **obsidian** (62.5%), **electrum** (18.75%)|
| legendary|  **electrum** (76.9%), **adamantite** (23.1%)                  |
| mythical |  **adamantite** (76.9%), **meteorite** (23.1%)                 |

#### Secondary

Secondary weapon materials are chosen based on item rarity, with each material in its respective rarity tier having equal probability.

| Rarity   |       Secondary Material (probability)       |
| -------- | :------------------------------------------: |
| crude    |  splintered wood, cracked wood, warped wood  |
| common   |  ash, maple, beech, hickory                  |
| uncommon |  maple, beech, hickory, mahogany             |
| rare     |  hickory, mahogany, walnut, cherry           |
| legendary|  walnut, cherry, birch, korina               | 
| mythical |  bloodwood, ebony, black walnut, purpleheart |

#### Heavy Armor

Heavy armor is produced using either *plate* or *laminar* construction methods.

| Rarity   |                   Material (probability)                    |
| -------- | :---------------------------------------------------------: |
| crude    |  **iron** (76.9%), **steel** (23.1%)                        |
| common   |  **iron** (18.75%), **steel** (62.5%), **obsidian** (18.75%)|
| uncommon |  **steel** (18.75%), **obsidian** (62.5%), **bone** (18.75%)|
| rare     |  **obsidian** (18.75%), **bone** (62.5%), **onyx** (18.75%) |
| legendary|  **onyx** (76.9%), **adamantite** (23.1%)                   |
| mythical |  **adamantite** (76.9%), **meteorite** (23.1%)              |

#### Light Armor

Light armor is produced using either *lamellar* or *scale* construction methods.

| Rarity   |                      Material (probability)                       |
| -------- | :---------------------------------------------------------------: |
| crude    |  **hide** (76.9%), **leather** (23.1%)                            |
| common   |  **hide** (18.75%), **leather** (62.5%), **obsidian** (18.75%)    |
| uncommon |  **leather** (18.75%), **obsidian** (62.5%), **electrum** (18.75%)|
| rare     |  **obsidian** (18.75%), **electrum** (62.5%), **bone** (18.75%)   |
| legendary|  **bone** (76.9%), **adamantite** (23.1%)                         |
| mythical |  **adamantite** (76.9%), **meteorite** (23.1%)                    |


## Weapons

Weapons fall into two major categories, *melee* and *ranged*, and two sub-types, *one-handed* and *two-handed*. All weapons are generated with equal probability.

### Melee

Melee item types include both one-handed and two-handed swords, axes, and blunt weapons.

One-handed:
~ `Labrys`, `hatchet`, `morning star`, `mace`, `club`, `flail`, `dagger`, `corvo`, `stiletto`, `shortsword`, `xiphos`, `seax`, `baselard`, `gladius`

Two-handed:
~ `War hammer`, `meteor hammer`, `dire flail`, `longsword`, `broadsword`, `claymore`, `bastard sword`, `war scythe`, `battle axe`, `halberd`, `glaive`

### Ranged

There are currently no one-handed ranged items. I am considering adding throwing knives, throwing stars, and caltrops, however.

Two-handed:
~ `Recurve bow`, `scythian bow`, `crossbow`, `longbow`

## Armor

There are five basic types of armor, each of which has a heavy and a light variant. All armor items are generated with equal probability.

Heavy:

~ `Helm`, `helmet`, `cuirass`, `corslet`, `gauntlets`, `boots`, `sabatons`, `pavise shield`, `kite shield`

Light:

~ `Hood`, `coif`, `brigandine`, `gambeson`, `gloves`, `boots`, `buckler`, `targe shield`


## Item parts

### Weapons

Each weapon item gets a list of three to five parts corresponding the the weapon type, which are used in the generation of the item's description. Item types are separated into four main categories.

Blade:
~ `Fuller`, `pommel`, `hilt`, `grip`, `cross-guard`, `quillon`

Axe:
~ `Pommel`, `haft`, `hook`, `beard`

Blunt:
~ `Throat`, `cheek`, `flange`, `face`, `crown`, `haft`, `handle`, `grip`

Bow:
~ `Nock`, `face`, `hilt`, `grip`, `limbs`, `belly`

### Armor


## Names

Item names are determined by the item's type, rarity, and material.

## Descriptions

Item descriptions are generated based on the item's type, rarity, material, and sub-type.

## Stats

Item stats are a function of the item's type, rarity, and sub-type.

#### Weapons
`damage`: the base damage level of the weapon
`range`: the effective range of the weapon
`speed`: how quickly the weapon can be handled
`luck`: determines the chance of a critical hit


#### Armor
`protection`: the base level of protection this armor provides
`movement`: the player movement speed penalty attributed to this piece
`noise`: how much of a racket this armor produces during movement while wearing
`luck`: chance of critical hit from an enemy

## Planned Features