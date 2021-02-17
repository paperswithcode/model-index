from typing import Dict

from modelindex.models.BaseModelIndex import BaseModelIndex


class Result(BaseModelIndex):

    def __init__(self,
                 task: str,
                 dataset: str,
                 metrics: Dict,
                 _filepath: str = None,
                 ):
        d = {
            "Task": task,
            "Dataset": dataset,
            "metrics": metrics,
        }

        super().__init__(
            data=d,
            filepath=_filepath
        )
