from typing import Dict, Union, List

from modelindex.models.Metadata import Metadata
from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.Result import Result
from modelindex.models.ResultList import ResultList
from modelindex.utils import lowercase_keys, full_filepath, load_any_file


class Model(BaseModelIndex):

    def __init__(self,
                 name: str,
                 metadata: Union[dict, Metadata, str] = None,
                 results: Union[list, ResultList, Result, str] = None,
                 paper: str = None,
                 code: str = None,
                 weights: str = None,
                 config: str = None,
                 readme: str = None,
                 in_collection: Union[str, List[str]] = None,
                 _filepath: str = None,
                 ):
        if metadata is not None and isinstance(metadata, str):
            metadata = Metadata.from_file(metadata, _filepath)
        elif metadata is not None and not isinstance(metadata, Metadata):
            metadata = Metadata.from_dict(metadata, _filepath)

        if results is not None and isinstance(results, str):
            results = ResultList.from_file(results, _filepath)
        elif results is not None and not isinstance(results, ResultList):
            results = ResultList(results, _filepath)

        d = {
            "Name": name,
            "Metadata": metadata,
            "Results": results,
            "Paper": paper,
            "Code": code,
            "Weights": weights,
            "Config": config,
            "README": readme,
            "In Collection": in_collection,
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
            "in_collection",
        ]

        dd = {}
        for field_name in copy_fields:
            key = field_name.lower()
            if key in lc_keys:
                dd[field_name] = d[lc_keys[key]]

            # try with " " instead of "_" in the field name
            if "_" in field_name:
                key = field_name.lower().replace("_", " ")
                if key in lc_keys:
                    dd[field_name] = d[lc_keys[key]]

        return Model(
            _filepath=_filepath,
            **dd,
        )

    @staticmethod
    def from_file(filepath: str = None, parent_filepath: str = None):
        fullpath = full_filepath(filepath, parent_filepath)
        raw, md_path = load_any_file(filepath, parent_filepath)
        d = raw
        if isinstance(raw, dict):
            lc_keys = lowercase_keys(raw)
            if "model" in lc_keys:
                d = raw[lc_keys["model"]]
            elif "models" in lc_keys:
                # called Model.from_file() on a model list, fallback to ModelList
                d = raw[lc_keys["models"]]
                if isinstance(d, list):
                    from modelindex.models.ModelList import ModelList
                    return ModelList(d, fullpath)

            return Model.from_dict(d, fullpath)
        else:
            raise ValueError(f"Expected a model dict, but got "
                             f"something else in file '{fullpath}'")


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

    @property
    def in_collection(self):
        return self.data["In Collection"]

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

    @in_collection.setter
    def in_collection(self, value):
        self.data["In Collection"] = value

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
