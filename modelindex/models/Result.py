from typing import Dict

from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.utils import lowercase_keys, load_any_file, full_filepath


class Result(BaseModelIndex):
    """Result represents a model result on a particular benchmark."""
    COMMON_FIELDS = [
        "Task",
        "Dataset",
        "Metrics",
    ]

    def __init__(self,
                 task: str,
                 dataset: str,
                 metrics: Dict,
                 _filepath: str = None,
                 ):
        """
        Args:
            task (str): The name of the ML task
            dataset (str): The name of the dataset
            metrics (dict): A dictionary of metrics
            _filepath (str): Path to the file where the data was loaded from
        """
        d = {
            "Task": task,
            "Dataset": dataset,
            "Metrics": metrics,
        }

        super().__init__(
            data=d,
            filepath=_filepath
        )

    def _check(self, silent=True):
        for field in ["Task", "Dataset", "Metrics"]:
            if field not in self.data or self.data[field] is None:
                self.check_errors.add(f"Field '{field}' is missing")

        for field in ["Task", "Dataset"]:
            if field in self.data and self.data[field] is not None and not isinstance(self.data[field], str):
                name = type(self.data[field]).__name__
                self.check_errors.add(f"The '{field}' field should be a string but got {name}")

        if "Metrics" in self.data and self.data["Metrics"]:
            m = self.data["Metrics"]
            if not isinstance(m, list) and not isinstance(m, dict):
                self.check_errors.add("The 'Metrics' fields needs to be either a dict or a list")

    @staticmethod
    def from_dict(d: Dict, _filepath: str = None):
        """Create a Result from a dict.

        Args:
            d (dict): dictionary containing result data
            _filepath (str): The file path to where the data was loaded from
        """
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
        """Load a Result from a file.

        Args:
            filepath (str): File from which to load the result
            parent_filepath (str): Parent filename (if file is imported from another file)
        """
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
        """Get the dataset name"""
        return self.data.get("Dataset", None)

    @property
    def task(self):
        """Get the ML task name"""
        return self.data.get("Task", None)

    @property
    def metrics(self):
        """Get the dictionary of metrics"""
        return self.data.get("Metrics", None)

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




