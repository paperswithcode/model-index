import os

from modelindex.consts import MODEL_INDEX_ROOT_FILE
from modelindex.models.ModelIndex import ModelIndex
from modelindex.utils import load_any_file


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
    if "models" in keys_lowercase \
            or "collections" in keys_lowercase \
            or "import" in keys_lowercase:
        obj = ModelIndex.from_dict(raw, path)

    return obj
