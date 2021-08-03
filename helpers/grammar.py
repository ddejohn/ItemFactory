# Standard Library
from random import choice


def linking_verb(word: str) -> str:
    if " " in word or (word[-1] == "s" and word[-2] not in "sy"):
        return f"{word} are"
    return f"{word} is"


def pair_or_set(word: str) -> str:
    if word[-1] == "s" and word[-2] not in "uosy":
        return choice(("set", "pair")) + f" of {word}"
    return word


def determinative(word: str) -> str:
    """The determinative a(n) for nouns"""
    if word[0] in "aeiou":
        return f"an {word}"
    return f"a {word}"


def oxford_list(*words: str) -> str:
    """Returns an oxford-comma-separated list of words or phrases"""
    *rest, last = words
    rest = ", ".join(rest)
    if rest:
        if " " not in rest:
            return f"{rest} and {last}"
        return f"{rest}, and {last}"
    return last
