# Standard Library
from random import choice
from itertools import product
from typing import Dict, Iterable, List

# Third Party
import yaml
import pandas as pd

# Local
from helpers.constants import PATHS


def load_data(path: str, columns: List[str]) -> pd.DataFrame:
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    return pd.DataFrame(traverse_dict(data), columns=columns)


def traverse_dict(data, items=tuple()) -> Iterable[tuple]:
    if isinstance(data, list):
        yield from product(*items, data)
    if isinstance(data, dict):
        for key, val in data.items():
            yield from traverse_dict(val, (*items, (key,)))


def select(df: pd.DataFrame, *args) -> pd.DataFrame:
    if df.empty or not args:
        return df
    mask = df.isin(args[:1]).any(axis=1)
    return select(df[mask].reset_index(drop=True), *args[1:])


def generate_selection_dict(df: pd.DataFrame) -> Dict[str, str]:
    return choice(df.to_dict("records"))


def load_yamls() -> dict:
    data = {}
    for name, path in PATHS.items():
        with open(path, "r") as f:
            data[name] = yaml.safe_load(f)
    return data


# d = {"a": {"b": {"c": [0, 1],
#                  "d": [2, 3, 4]}},
#      "w": {"x": {"y": [5, 6, 7],
#                  "z": [8, 9]}}}

# for prod in traverse_dict(d):
#     print(prod)

# a:
#     b:
#         c:
#             0
#             1
#         d:
#             2
#             3
#             4
# w:
#     x:
#         y:
#             5
#             6
#             7
#         z:
#             8
#             9
