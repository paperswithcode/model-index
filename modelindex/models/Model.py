from typing import Dict, Union

from modelindex.models.Metadata import Metadata
from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.Result import Result
from modelindex.models.ResultList import ResultList
from modelindex.utils import lowercase_keys


class Model(BaseModelIndex):

    def __init__(self,
                 name: str,
                 metadata: Union[dict, Metadata] = None,
                 results: Union[list, ResultList, Result] = None,
                 paper: str = None,
                 code: str = None,
                 weights: str = None,
                 config: str = None,
                 readme: str = None,
                 _filepath: str = None,
                 ):

        if metadata is not None and not isinstance(metadata, Metadata):
            metadata = Metadata.from_dict(metadata)

        if results is not None and not isinstance(results, ResultList):
            results = ResultList(results)

        d = {
            "Name": name,
            "Metadata": metadata,
            "Results": results,
            "Paper": paper,
            "Code": code,
            "Weights": weights,
            "Config": config,
            "README": readme,
        }

        # Only non-empty items
        data = {k: v for k, v in d.items() if v is not None}

        super().__init__(
            data=data,
            filepath=_filepath
        )

    @staticmethod
    def from_dict(d: Dict, _filepath: str = None):
        lc_keys = lowercase_keys(d)

        copy_fields = [
            "name",
            "paper",
            "code",
            "weights",
            "config",
            "readme",
            "metadata",
            "results",
        ]

        dd = {}
        for field_name in copy_fields:
            key = field_name.lower()
            if key in lc_keys:
                dd[field_name] = d[lc_keys[key]]

        return Model(
            _filepath=_filepath,
            **dd,
        )

    # Getters
    @property
    def name(self):
        return self.data["Name"]

    @property
    def paper(self):
        return self.data["Paper"]

    @property
    def code(self):
        return self.data["Code"]

    @property
    def weights(self):
        return self.data["Weights"]

    @property
    def config(self):
        return self.data["Config"]

    @property
    def readme(self):
        return self.data["README"]

    @property
    def metadata(self):
        return self.data["Metadata"]

    @property
    def results(self):
        return self.data["Results"]

    # Setters
    @name.setter
    def name(self, value):
        self.data["Name"] = value

    @paper.setter
    def paper(self, value):
        self.data["Paper"] = value

    @code.setter
    def code(self, value):
        self.data["Code"] = value

    @weights.setter
    def weights(self, value):
        self.data["Weights"] = value

    @config.setter
    def config(self, value):
        self.data["Config"] = value

    @readme.setter
    def readme(self, value):
        self.data["README"] = value

    @metadata.setter
    def metadata(self, value):
        if value is not None and not isinstance(value, Metadata):
            self.data["Metadata"] = Metadata.from_dict(value)
        else:
            self.data["Metadata"] = value

    @results.setter
    def results(self, value):
        if value is not None and not isinstance(value, ResultList):
            self.data["Results"] = ResultList(value)
        else:
            self.data["Results"] = value
