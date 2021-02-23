from typing import Union, Dict, List

from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.utils import lowercase_keys, full_filepath, load_any_file, merge_dicts


class Metadata(BaseModelIndex):
    """Metadata for a model."""

    COMMON_FIELDS = [
        "FLOPs",
        "Parameters",
        "Epochs",
        "Batch Size",
        "Training Data",
        "Training Techniques",
        "Training Resources",
        "Architecture",
    ]

    def __init__(self,
                 flops: Union[str, int] = None,
                 parameters: Union[str, int] = None,
                 epochs: Union[str, int] = None,
                 batch_size: Union[str, int] = None,
                 training_data: [str, List] = None,
                 training_techniques: [str, List] = None,
                 training_resources: str = None,
                 architecture: [str, List] = None,
                 _filepath: str = None,
                 **kwargs,
                 ):
        """
        Args:
            flops (str,int): number of FLOPs
            parameters (str,int): total number of parameters for the model
            epochs (str,int): how many epochs the model was trained
            batch_size (str,int): batch size for the model
            training_data (str,list): one or a list of datasets used in training
            training_techniques (str,list): one or a list of training techniques
            training_resources (str): hardware used to train
            architecture (str, List): one or a list of architectures used in the model
            _filepath (str): path to the file where the data is coming from
            **kwargs: any other custom metadata
        """
        d = {
            "FLOPs": flops,
            "Parameters": parameters,
            "Epochs": epochs,
            "Batch Size": batch_size,
            "Training Data": training_data,
            "Training Techniques": training_techniques,
            "Training Resources": training_resources,
            "Architecture": architecture,
            **kwargs,
        }

        # only save non-None values
        data = {k: v for k, v in d.items() if v is not None}

        super().__init__(
            data=data,
            filepath=_filepath
        )

    def _check(self, silent=True):
        if not isinstance(self.data, dict) and not isinstance(self.data, list):
            self.check_errors.add("Metadata should be either a list or a dict")

    @staticmethod
    def from_dict(d: Dict, _filepath: str = None):
        """Construct Metadata from a dict.

        Args:
            d (dict): A dictionary of values
            _filepath (str): path to the file where the data is coming from

        """
        # be flexible to a common error where
        if isinstance(d, list) and len(d) > 0:
            d = merge_dicts(d)

        lc_keys = lowercase_keys(d)

        dd = d.copy()
        for field_name in Metadata.COMMON_FIELDS:
            key = field_name.lower()
            if key in lc_keys:
                dd[field_name] = dd.pop(lc_keys[key])

            # try with _ instead of space in the field name
            if " " in field_name:
                key = field_name.lower().replace(" ", "_")
                if key in lc_keys:
                    dd[field_name] = dd.pop(lc_keys[key])

        return Metadata(
            _filepath=_filepath,
            **dd,
        )

    @staticmethod
    def from_file(filepath: str = None, parent_filepath: str = None):
        """Load a Metadata from a file.

        Args:
            filepath (str): File from which to load the metadata
            parent_filepath (str): Parent filename (if file is imported from another file)
        """
        fullpath = full_filepath(filepath, parent_filepath)
        raw, md_path = load_any_file(filepath, parent_filepath)

        d = raw
        if isinstance(d, dict):
            return Metadata.from_dict(d, fullpath)

        raise ValueError(f"Expected a dictionary with metadata, "
                         f"but got something else in file at"
                         f"'{fullpath}'")

    # Getters
    @property
    def flops(self):
        """Get the FLOPs"""
        return self.data.get("FLOPs", None)

    @property
    def parameters(self):
        """Get number of parameters"""
        return self.data.get("Parameters", None)

    @property
    def epochs(self):
        """Get epochs"""
        return self.data.get("Epochs", None)

    @property
    def batch_size(self):
        """Get batch size"""
        return self.data.get("Batch Size", None)

    @property
    def training_data(self):
        """Get training data used"""
        return self.data.get("Training Data", None)

    @property
    def training_techniques(self):
        """Get techniques used"""
        return self.data.get("Training Techniques", None)

    @property
    def training_resources(self):
        """Get training resources used"""
        return self.data.get("Training Resources", None)

    @property
    def architecture(self):
        """Get the architecture(s) used."""
        return self.data.get("Architecture", None)

    # Setters
    @flops.setter
    def flops(self, value):
        self.data["FLOPs"] = value

    @parameters.setter
    def parameters(self, value):
        self.data["Parameters"] = value

    @epochs.setter
    def epochs(self, value):
        self.data["Epochs"] = value

    @batch_size.setter
    def batch_size(self, value):
        self.data["Batch Size"] = value

    @training_data.setter
    def training_data(self, value):
        self.data["Training Data"] = value

    @training_techniques.setter
    def training_techniques(self, value):
        self.data["Training Techniques"] = value

    @training_resources.setter
    def training_resources(self, value):
        self.data["Training Resources"] = value

    @architecture.setter
    def architecture(self, value):
        self.data["Architecture"] = value









