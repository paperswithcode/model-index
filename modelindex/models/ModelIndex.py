from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.ModelList import ModelList
from modelindex.utils import lowercase_keys


class ModelIndex(BaseModelIndex):
    def __init__(self,
                 data: dict = None,
                 filepath: str = None,
                 ):

        if data is None:
            data = {}

        d = {}
        lc_keys = lowercase_keys(data)
        if "models" in lc_keys:
            models = data[lc_keys["models"]]
            if not isinstance(models, ModelList):
                models = ModelList(models)

            d["Models"] = models

        super().__init__(
            data=d,
            filepath=filepath
        )

        self.lc_keys = lowercase_keys(data)

    @staticmethod
    def from_dict(d: dict, filepath: str = None):
        return ModelIndex(d, filepath)

    @property
    def models(self):
        return self.data["Models"]

    @models.setter
    def models(self, value):
        self.data["Models"] = value
