from modelindex.consts import MODEL_INDEX_ROOT_FILE
from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.utils import lowercase_keys


class ModelIndex(BaseModelIndex):
    def __init__(self,
                 data: dict = None,
                 filepath: str = MODEL_INDEX_ROOT_FILE,
                 ):

        if data is None:
            data = {}

        lc_keys = lowercase_keys(data)
        self.lc_keys = lc_keys

        if "models" in lc_keys:
            self.models = data[lc_keys["models"]]

        if "collections" in lc_keys:
            self.collections = data[lc_keys["collections"]]

        super().__init__(
            data=data,
            filepath=filepath
        )

    @staticmethod
    def from_dict(d: dict, filepath: str = None):
        return ModelIndex(d, filepath)

