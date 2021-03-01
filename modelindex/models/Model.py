import os
from typing import Dict, Union, List

from ordered_set import OrderedSet

from modelindex.models.Metadata import Metadata
from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.Result import Result
from modelindex.models.ResultList import ResultList
from modelindex.utils import lowercase_keys, full_filepath, load_any_file, expand_wildcard_path, merge_lists_data


class Model(BaseModelIndex):
    """Model represents the ML model.
    """
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
                 name: str = None,
                 metadata: Union[Dict, Metadata, str] = None,
                 results: Union[List, ResultList, Result, Dict, str] = None,
                 paper: Union[str, Dict] = None,
                 code: str = None,
                 weights: str = None,
                 config: str = None,
                 readme: str = None,
                 in_collection: Union[str, List[str]] = None,
                 _filepath: str = None,
                 **kwargs,
                 ):
        """
        Args:
            name (str): Name of the model
            metadata (Metadata, dict, str): Metadata object, metadata dict or a filepath to the metadata file
            results (ResultList, Result, list, dict, str): ResultList, a single Results, a list of result dicts, a single
                                                     result dict, or a filepath to the result file
            paper (str, dict): URL to the paper, or a structured dict with paper metadata (title, url)
            code (str): URL to the code snippet
            weights (str): URL to the pretrained weights
            config (str): URL to the config file
            readme (str): path to the README file for the model
            in_collection (str, List): name of the collection to which the model belongs to
            _filepath: The file path to where the data was loaded from
            **kwargs: Any other custom fields
        """

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

    @classmethod
    def from_dict(cls, d: Dict, _filepath: str = None, _path_to_readme: str = None):
        """Create a Model from a dictionary.

        Args:
            d (dict): dictionary containing models data
            _filepath (str): The file path to where the data was loaded from
            _path_to_readme (str): Path to the README file if metadata was extracted from a README
        """
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
            dd["readme"] = _path_to_readme

        return cls(
            _filepath=_filepath,
            **dd,
        )

    @staticmethod
    def from_file(filepath: str = None, parent_filepath: str = None):
        """Load a Model from a file.

        Args:
            filepath (str): File from which to load the model
            parent_filepath (str): Parent filename (if file is imported from another file)
        """
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
                    return ModelList(d, fullpath, md_path)

            return Model.from_dict(d, fullpath, md_path)
        else:
            raise ValueError(f"Expected a model dict, but got "
                             f"something else in file '{fullpath}'")


    # Getters
    @property
    def name(self):
        """Get the model name"""
        return self.data.get("Name", None)

    @property
    def paper(self):
        """Get the model paper"""
        return self.data.get("Paper", None)

    @property
    def code(self):
        """Get the URL to code"""
        return self.data.get("Code", None)

    @property
    def weights(self):
        """Get the URL to weights"""
        return self.data.get("Weights", None)

    @property
    def config(self):
        """Get the URL to the config file"""
        return self.data.get("Config", None)

    @property
    def readme(self):
        """Get the path to the model README"""
        return self.data.get("README", None)

    @property
    def metadata(self):
        """Get the metadata as a Metadata object"""
        return self.data.get("Metadata", None)

    @property
    def results(self):
        """Get the results as a Result object"""
        return self.data.get("Results", None)

    @property
    def in_collection(self):
        """Get the name of the collection of which this model is part of."""
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
