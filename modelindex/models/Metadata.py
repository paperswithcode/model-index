from typing import Union, Dict

from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.utils import lowercase_keys, full_filepath, load_any_file


class Metadata(BaseModelIndex):

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
                 training_data: str = None,
                 training_techniques: str = None,
                 training_resources: str = None,
                 architecture: str = None,
                 _filepath: str = None,
                 **kwargs,
                 ):
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

    @staticmethod
    def from_dict(d: Dict, _filepath: str = None):
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
        fullpath = full_filepath(filepath, parent_filepath)
        raw, md_path = load_any_file(filepath, parent_filepath)
        d = raw
        if isinstance(d, dict):
            return Metadata.from_dict(d, fullpath)

        raise ValueError(f"Expected a dictionary with metadata, "
                         f"but got something else in file at"
                         f"'{fullpath}'")
















