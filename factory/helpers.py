# Standard Library
from random import choice
from typing import Dict

# Third Party
import yaml
import pandas as pd


def load_data() -> pd.DataFrame:
    with open("./data/items.yml", "r") as items_yaml:
        items = yaml.safe_load(items_yaml)

    records = []
    for item_class, subclasses in items.items():
        for subclass, item_types in subclasses.items():
            for item_type, subtypes in item_types.items():
                for subtype in subtypes:
                    records.append({"item_class": item_class,
                                    "item_subclass": subclass,
                                    "item_type": item_type,
                                    "item_subtype": subtype})
    return pd.DataFrame(records)


def select(df: pd.DataFrame, *args) -> pd.DataFrame:
    if df.empty or not args:
        return df
    return select(df[df.isin(args[:1]).any(axis=1)], *args[1:])


def generate_item_dict(df: pd.DataFrame) -> Dict[str, str]:
    return choice(df.to_dict("records"))
