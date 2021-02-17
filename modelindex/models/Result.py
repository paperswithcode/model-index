from typing import Dict

from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.utils import lowercase_keys


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
            "Metrics": metrics,
        }

        super().__init__(
            data=d,
            filepath=_filepath
        )

    @staticmethod
    def from_dict(d: Dict, _filepath: str = None):
        lc_keys = lowercase_keys(d)

        task = None
        dataset = None
        metrics = None

        if "task" in lc_keys:
            task = d[lc_keys["task"]]
        if "dataset" in lc_keys:
            dataset = d[lc_keys["dataset"]]
        if "metrics" in lc_keys:
            metrics = d[lc_keys["metrics"]]

        return Result(
            task=task,
            dataset=dataset,
            metrics=metrics,
            _filepath=_filepath,
        )

    @property
    def dataset(self):
        return self.data["Dataset"]

    @property
    def task(self):
        return self.data["Task"]

    @property
    def metrics(self):
        return self.data["Metrics"]

    # Setters
    @dataset.setter
    def dataset(self, value):
        self.data["Dataset"] = value

    @task.setter
    def task(self, value):
        self.data["Task"] = value

    @metrics.setter
    def metrics(self, value):
        self.data["Metrics"] = value




