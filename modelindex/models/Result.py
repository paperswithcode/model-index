from typing import Dict

from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.utils import lowercase_keys, load_any_file, full_filepath


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

    def check(self, silent=True):
        self.check_errors = []

        for field in ["Task", "Dataset", "Metrics"]:
            if field not in self.data or self.data[field] is None:
                self.check_errors.append(f"Field '{field}' is missing")

        if "Metrics" in self.data and self.data["Metrics"]:
            m = self.data["Metrics"]
            if not isinstance(m, list) and not isinstance(m, dict):
                self.check_errors.append("The 'Metrics' fields needs to be either a dict or a list")

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

    @staticmethod
    def from_file(filepath: str = None, parent_filepath: str = None):
        fullpath = full_filepath(filepath, parent_filepath)
        raw, md_path = load_any_file(filepath, parent_filepath)
        d = raw
        if isinstance(raw, dict):
            lc_keys = lowercase_keys(raw)
            if "result" in lc_keys:
                d = raw[lc_keys["result"]]
            elif "results" in lc_keys:
                # called Result.from_file() on a result list, fallback to ResultList
                d = raw[lc_keys["results"]]
                if isinstance(d, list):
                    from modelindex.models.ResultList import ResultList
                    return ResultList(d, fullpath)

            return Result.from_dict(d, fullpath)
        else:
            raise ValueError(f"Expected a results dict, but got "
                             f"something else in file '{fullpath}'")

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




