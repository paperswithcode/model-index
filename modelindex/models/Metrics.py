from modelindex.consts import MODEL_INDEX_ROOT_FILE
from modelindex.models.BaseModelIndex import BaseModelIndex


class Metrics(BaseModelIndex):
    def __init__(self,
                 filepath=MODEL_INDEX_ROOT_FILE,
                 metrics={},
                 ):

        if not isinstance(metrics, dict):
            raise ValueError("'metrics' needs to be a dictionary")

        self.metrics = metrics

        super().__init__(
            filepath=filepath
        )
