import yaml
import json
import markdown
import os

from modelindex.consts import MODEL_INDEX_ROOT_FILE
from modelindex.models.ModelIndex import ModelIndex


def load_raw_from_markdown(path: str):
    """Load raw metadata from a markdown file

        Args:
            path (str): Path to the markdown file
    """

    with open(path, "r") as f:
        md = markdown.markdown(f.read())

    # TODO

    return ""


def load_any_file(path: str):
    """Load any of the supported file formats

        Args:
            path (str) Path to the file to load

        Returns:
            (raw, md_path) - where raw is the loaded content of the file (normally a dict)
            and md_path is the file to the markdown path (if loaded from markdown)
    """

    if not os.path.exists(path):
        raise IOError(f"File {path} does not exist.")

    md_path = None
    if path.endswith(".yml") or path.endswith(".yaml"):
        with open(path, "r") as f:
            raw = yaml.load(f, Loader=yaml.SafeLoader)
    elif path.endswith(".json"):
        with open(path, "r") as f:
            raw = json.load(f)
    elif path.endswith(".md"):
        md_path = path
        raw = load_raw_from_markdown(path)
    else:
        raise ValueError(f"File type at path '{path}' not recognized. We support YAML (.yml or .yaml), "
                         f"JSON (.json) and markdown (.md) files.")

    return raw, md_path


def load(path: str = "model-index.yml"):
    """Load the model index.

       Args:
            path (str): Path to the file to load, or a directory containing model-index.yml.

       Returns:
            ModelIndex instance that has been loaded from the disk.
    """

    if os.path.isdir(path):
        path = os.path.join(path, MODEL_INDEX_ROOT_FILE)

    raw, md_path = load_any_file(path)

    # make sure the input is a dict
    if not isinstance(raw, dict):
        raise ValueError(f"Expected the file '{path}' to contain a dictionary of values, but it doesn't.")

    # Guess the type based on dict entries
    obj = None
    keys_lowercase = [k.lower() for k in raw.keys()]
    if "models" in keys_lowercase:
        obj = ModelIndex.from_dict(raw, path)

    return obj
