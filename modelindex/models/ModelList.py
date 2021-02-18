from typing import List, Union, Dict

from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.Model import Model


class ModelList(BaseModelIndex):
    def __init__(self,
                 models: Union[List[Union[Model, Dict]], Model, Dict] = None,
                 _filepath: str = None,
                 ):

        if models is None:
            models = []

        if isinstance(models, Model) or isinstance(models, dict):
            models = [models]

        models_parsed = []
        for m in models:
            if isinstance(m, Model):
                models_parsed.append(m)
            else:
                models_parsed.append(Model.from_dict(m, _filepath))

        super().__init__(
            data=models_parsed,
            filepath=_filepath
        )

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    @property
    def models(self):
        return self.data

    def add(self, model: Union[Model, Dict]):
        if isinstance(model, dict):
            self.data.append(Model.from_dict(model, self.filepath))
        elif isinstance(model, Model):
            self.data.append(model)

    def __len__(self):
        return len(self.data)

