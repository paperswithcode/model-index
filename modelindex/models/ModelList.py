from typing import List, Union, Dict

from ordered_set import OrderedSet

from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.Model import Model
from modelindex.utils import full_filepath, load_any_file, lowercase_keys


class ModelList(BaseModelIndex):
    def __init__(self,
                 models: Union[List[Union[Model, Dict, str]], Model, Dict] = None,
                 _filepath: str = None,
                 ):

        check_errors = OrderedSet()

        if models is None:
            models = []

        if isinstance(models, Model) or isinstance(models, dict):
            models = [models]

        models_parsed = []
        for m in models:
            if isinstance(m, str):
                try:
                    models_parsed.append(Model.from_file(m, _filepath))
                except (IOError, ValueError) as e:
                    check_errors.add(str(e))
            elif isinstance(m, Model):
                models_parsed.append(m)
            else:
                models_parsed.append(Model.from_dict(m, _filepath))

        super().__init__(
            data=models_parsed,
            filepath=_filepath,
            check_errors=check_errors,
        )

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    @property
    def models(self):
        return self.data

    def add(self, model: Union[Model, Dict], _filepath: str = None):
        model_filepath = _filepath if _filepath is not None else self.filepath
        if isinstance(model, dict):
            self.data.append(Model.from_dict(model, model_filepath))
        elif isinstance(model, Model):
            self.data.append(model)

    def __len__(self):
        return len(self.data)

    @staticmethod
    def from_file(filepath: str = None, parent_filepath: str = None):
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

