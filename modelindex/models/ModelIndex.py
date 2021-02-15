from modelindex.consts import MODEL_INDEX_ROOT_FILE
from modelindex.models.BaseModelIndex import BaseModelIndex


class ModelIndex(BaseModelIndex):
    def __init__(self,
                 filepath=MODEL_INDEX_ROOT_FILE
                 ):
        super().__init__(
            filepath=filepath
        )

