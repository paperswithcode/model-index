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
                models_parsed.append(Model.from_dict(m))

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
