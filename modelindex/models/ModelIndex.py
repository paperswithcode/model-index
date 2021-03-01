from ordered_set import OrderedSet

from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.CollectionList import CollectionList
from modelindex.models.ModelList import ModelList
from modelindex.utils import lowercase_keys, load_any_file, full_filepath, load_any_files_wildcard, \
    expand_wildcard_path, merge_lists_data


class ModelIndex(BaseModelIndex):
    """ModelIndex is the root object for the whole model index.
    """
    COMMON_FIELDS = [
        "Models",
        "Collections",
    ]

    def __init__(self,
                 data: dict = None,
                 filepath: str = None,
                 _path_to_readme: str = None
                 ):
        """
        Args:
            data (dict): The root model index as a dictionary
            filepath (str): The path from which it was loaded
            _path_to_readme (str): The path to the readme file (if loaded from there)
        """

        check_errors = OrderedSet()

        if data is None:
            data = {}

        d = {
            "Models": ModelList(_filepath=filepath),
            "Collections": CollectionList(_filepath=filepath),
        }
        lc_keys = lowercase_keys(data)
        if "models" in lc_keys:
            models = data[lc_keys["models"]]
            # Syntax: Models: <path to file(s)>
            if models is not None and isinstance(models, str):
                models_list = []
                for model_file in expand_wildcard_path(models, filepath):
                    try:
                        models_list.append(ModelList.from_file(model_file, filepath))
                    except (IOError, ValueError) as e:
                        check_errors.add(str(e))
                models = merge_lists_data(models_list)
            # Syntax: Models: list[ model dict ]
            elif models is not None and not isinstance(models, ModelList):
                models = ModelList(models, filepath, _path_to_readme)

            d["Models"] = models

        if "collections" in lc_keys:
            collections = data[lc_keys["collections"]]
            # Syntax: Collections: <path to file(s)>
            if collections is not None and isinstance(collections, str):
                collections_list = []
                for model_file in expand_wildcard_path(collections, filepath):
                    try:
                        collections_list.append(CollectionList.from_file(model_file, filepath))
                    except (IOError, ValueError) as e:
                        check_errors.add(str(e))
                collections = merge_lists_data(collections_list)
            # Syntax: Collections: list[ model dict ]
            elif collections is not None and not isinstance(collections, CollectionList):
                collections = CollectionList(collections, filepath, _path_to_readme)

            d["Collections"] = collections

        if "import" in lc_keys:
            imp = data[lc_keys["import"]]

            if not isinstance(imp, list):
                imp = list(imp)

            for import_file in imp:
                try:
                    for relpath in expand_wildcard_path(import_file, filepath):
                        raw, md_name = load_any_file(relpath, filepath)
                        fullpath = full_filepath(relpath, filepath)
                        mi = ModelIndex.from_dict(raw, fullpath, md_name)
                        if mi.models:
                            for model in mi.models:
                                d["Models"].add(model)

                            for col in mi.collections:
                                d["Collections"].add(col)
                except (IOError, ValueError) as e:
                    check_errors.add(str(e))

        super().__init__(
            data=d,
            filepath=filepath,
            check_errors=check_errors,
        )

        self.lc_keys = lowercase_keys(data)

    @staticmethod
    def from_dict(d: dict, filepath: str = None, _path_to_readme: str = None):
        """Construct a ModelIndex from a dictionary

        Args:
            data (dict): The root model index as a dictionary
            filepath (str): The path from which it was loaded
            _path_to_readme (str): Path to the README.md file if loaded from there
        """
        return ModelIndex(d, filepath, _path_to_readme)

    @property
    def models(self) -> ModelList:
        """Get the list of models in the ModelIndex."""
        return self.data["Models"]

    @models.setter
    def models(self, value):
        """Set the list of models in the ModelIndex."""
        self.data["Models"] = value

    @property
    def collections(self) -> CollectionList:
        """Get the list of collections in the ModelIndex."""
        return self.data["Collections"]

    @collections.setter
    def collections(self, value):
        """Set the list of collections in the ModelIndex"""
        self.data["Collections"] = value

