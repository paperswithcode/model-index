import os
from typing import Dict

from modelindex.consts import MODEL_INDEX_ROOT_FILE
from modelindex.models.Model import Model
from modelindex.models.ModelIndex import ModelIndex
from modelindex.models.ModelList import ModelList
from modelindex.models.Result import Result
from modelindex.models.Metadata import Metadata
from modelindex.models.ResultList import ResultList
from modelindex.utils import load_any_file


def has_at_least_one_models_key(lc_keys):
    """Check if there is at least one optional Models dict key in lowercase keys
    """

    model_keys = {"paper",
                  "code",
                  "weights",
                  "config",
                  "readme",
                  "metadata",
                  "results",
                  "incollection"}

    return len(model_keys.intersection(set(lc_keys))) >= 1


def load_based_on_dict_field_guess(raw: Dict, path: str, md_path: str):
    """Load from a dict by guessing it's type based on keys in the dict.

    Args:
        raw (dict): The dictionary we want to load in
        path (str): The path it was read from
        md_path (str): Path to the Markdown file (if dict coming from there)

    """
    keys_lowercase = [k.lower() for k in raw.keys()]
    if "models" in keys_lowercase \
            or "collections" in keys_lowercase \
            or "import" in keys_lowercase:
        obj = ModelIndex.from_dict(raw, path)
    elif "task" in keys_lowercase and "dataset" in keys_lowercase and "metrics" in keys_lowercase:
        obj = Result.from_dict(raw, path)
    elif "name" in keys_lowercase and has_at_least_one_models_key(keys_lowercase):
        obj = Model.from_dict(raw, path, md_path)
    else:
        obj = Metadata.from_dict(raw, path)

    return obj


def load(path: str = "model-index.yml"):
    """Load the model index.

       Args:
            path (str): Path to the file to load, or a directory containing model-index.yml.

       Returns:
            ModelIndex instance that has been loaded from the disk.
    """

    if os.path.isdir(path):
        new_path = os.path.join(path, MODEL_INDEX_ROOT_FILE)
        # if model-index.yml doesn't exist try model-index.yaml
        if not os.path.exists(new_path):
            yaml_ext = os.path.join(path, "model-index.yaml")
            if os.path.exists(yaml_ext):
                new_path = yaml_ext
        path = new_path

    raw, md_path = load_any_file(path)

    # make sure the input is a dict
    if not isinstance(raw, dict) and not isinstance(raw, list):
        raise ValueError(f"Expected the file '{path}' to contain a dict or a list, but it doesn't.")

    # Guess the type based on dict entries
    obj = None
    if isinstance(raw, dict) and raw:
        obj = load_based_on_dict_field_guess(raw, path, md_path)
    elif isinstance(raw, list) and raw:
        obj_guess = load_based_on_dict_field_guess(raw[0], path, md_path)
        if isinstance(obj_guess, Result):
            return ResultList(raw, path)
        elif isinstance(obj_guess, Model):
            return ModelList(raw, path)

    if obj is None:
        raise ValueError(f"Unrecognized format in file '{path}'")

    return obj
