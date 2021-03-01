from typing import List, Union, Dict

from ordered_set import OrderedSet

from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.Model import Model
from modelindex.utils import full_filepath, load_any_file, lowercase_keys, expand_wildcard_path


class ModelList(BaseModelIndex):
    """ModeList is a list of Models."""
    def __init__(self,
                 models: Union[List[Union[Model, Dict, str]], Model, Dict] = None,
                 _filepath: str = None,
                 _path_to_readme: str = None,
                 ):
        """
        Args:
            models (list, Model, dict): Either a list of models, and individual model or a dict representing a model
            _filepath (str): The path of the file from which the list is initialized
            _path_to_readme (str): Path to README if loaded from there
        """

        check_errors = OrderedSet()

        if models is None:
            models = []

        if isinstance(models, Model) or isinstance(models, dict):
            models = [models]

        models_parsed = []
        for m in models:
            if isinstance(m, str):
                # link to model file - support wildcards
                for model_file in expand_wildcard_path(m, _filepath):
                    try:
                        model = Model.from_file(model_file, _filepath)
                        if isinstance(model, Model):
                            models_parsed.append(model)
                        elif isinstance(model, ModelList):
                            models_parsed.extend(model)
                    except (IOError, ValueError) as e:
                        check_errors.add(str(e))
            elif isinstance(m, Model):
                # model object
                models_parsed.append(m)
            else:
                # dict
                models_parsed.append(Model.from_dict(m, _filepath, _path_to_readme))

        super().__init__(
            data=models_parsed,
            filepath=_filepath,
            check_errors=check_errors,
        )

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __iter__(self):
        self._iterator_inx = 0
        return self

    def __next__(self):
        if self._iterator_inx < len(self.data):
            self._iterator_inx += 1
            return self.data[self._iterator_inx - 1]
        else:
            raise StopIteration

    def __len__(self):
        return len(self.data)

    @property
    def models(self):
        """Get the list of models."""
        return self.data

    def add(self, model: Union[Model, Dict], _filepath: str = None):
        """Add a model to the list.

        Args:
            model (Model, dict): Either a Model or a dict representing a model
            _filepath (str): The path from which it was loaded

        """
        model_filepath = _filepath if _filepath is not None else self.filepath
        if isinstance(model, dict):
            self.data.append(Model.from_dict(model, model_filepath))
        elif isinstance(model, Model):
            self.data.append(model)

    @staticmethod
    def from_file(filepath: str = None, parent_filepath: str = None):
        """Load a ModelList from a file.

        Args:
            filepath (str): File from which to load the list of models.
            parent_filepath (str): Parent filename (if file is imported from another file)

        """
        fullpath = full_filepath(filepath, parent_filepath)
        raw, md_path = load_any_file(filepath, parent_filepath)
        d = raw

        if isinstance(d, list):
            return ModelList(d, fullpath)
        elif isinstance(d, dict):
            lc_keys = lowercase_keys(raw)
            if "models" in lc_keys:
                return ModelList(d[lc_keys["models"]], fullpath)

        raise ValueError(f"Expected a list of models, but got something else"
                         f"in file {fullpath}")

