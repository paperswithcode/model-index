from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.CollectionList import CollectionList
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
            if models is not None and not isinstance(models, ModelList):
                models = ModelList(models)

            d["Models"] = models

        if "collections" in lc_keys:
            collections = data[lc_keys["collections"]]
            if collections is not None and not isinstance(collections, CollectionList):
                collections = CollectionList(collections)

            d["Collections"] = collections

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

    @property
    def collections(self):
        return self.data["Models"]

    @collections.setter
    def collections(self, value):
        self.data["Collections"] = value
