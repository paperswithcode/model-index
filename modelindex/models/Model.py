import os
from typing import Dict, Union, List

from ordered_set import OrderedSet

from modelindex.models.Metadata import Metadata
from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.Result import Result
from modelindex.models.ResultList import ResultList
from modelindex.utils import lowercase_keys, full_filepath, load_any_file, expand_wildcard_path, merge_lists_data


class Model(BaseModelIndex):
    COMMON_FIELDS = [
        "Name",
        "Metadata",
        "Results",
        "Paper",
        "Code",
        "Weights",
        "Config",
        "README",
        "In Collection"
    ]

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
                 **kwargs,
                 ):

        check_errors = OrderedSet()

        if metadata is not None and isinstance(metadata, str):
            # link to a metadata file
            try:
                metadata = Metadata.from_file(metadata, _filepath)
            except (IOError, ValueError) as e:
                check_errors.add(str(e))
        elif metadata is not None and not isinstance(metadata, Metadata):
            metadata = Metadata.from_dict(metadata, _filepath)

        if results is not None and isinstance(results, str):
            # link to 1+ result files
            results_list = []
            for results_file in expand_wildcard_path(results, _filepath):
                try:
                    results_list.append(ResultList.from_file(results_file, _filepath))
                except (IOError, ValueError) as e:
                    check_errors.add(str(e))
            results = merge_lists_data(results_list)
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
            **kwargs,
        }

        # Only non-empty items
        data = {k: v for k, v in d.items() if v is not None}

        super().__init__(
            data=data,
            filepath=_filepath,
            check_errors=check_errors,
        )

    def _check(self, silent=True):
        if self.name is None or self.name == "":
            self.check_errors.add("Field 'Name' cannot be empty")

        if self.readme and self.readme.endswith(".md") and len(self.readme) < 256:
            # check if the README exists
            fullpath = full_filepath(self.readme, self.filepath)
            if not os.path.isfile(fullpath):
                self.check_errors.add(f"Path to README file {self.readme} is not a valid file.")

    @staticmethod
    def from_dict(d: Dict, _filepath: str = None, _path_to_readme: str = None):
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

        dd = d.copy()
        for field_name in copy_fields:
            key = field_name.lower()
            if key in lc_keys:
                dd[field_name] = dd.pop(lc_keys[key])

            # try with _ instead of space in the field name
            if " " in field_name:
                key = field_name.lower().replace(" ", "_")
                if key in lc_keys:
                    dd[field_name] = dd.pop(lc_keys[key])

        if _path_to_readme:
            dd["README"] = _path_to_readme

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

            return Model.from_dict(d, fullpath, md_path)
        else:
            raise ValueError(f"Expected a model dict, but got "
                             f"something else in file '{fullpath}'")


    # Getters
    @property
    def name(self):
        return self.data.get("Name", None)

    @property
    def paper(self):
        return self.data.get("Paper", None)

    @property
    def code(self):
        return self.data.get("Code", None)

    @property
    def weights(self):
        return self.data.get("Weights", None)

    @property
    def config(self):
        return self.data.get("Config", None)

    @property
    def readme(self):
        return self.data.get("README", None)

    @property
    def metadata(self):
        return self.data.get("Metadata", None)

    @property
    def results(self):
        return self.data.get("Results", None)

    @property
    def in_collection(self):
        return self.data.get("In Collection", None)

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
