from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.utils import lowercase_keys


class ModelIndex(BaseModelIndex):
    def __init__(self,
                 data: dict = None,
                 filepath: str = None,
                 ):

        if data is None:
            data = {}

        super().__init__(
            data=data,
            filepath=filepath
        )

        self.lc_keys = lowercase_keys(data)

    @staticmethod
    def from_dict(d: dict, filepath: str = None):
        return ModelIndex(d, filepath)

