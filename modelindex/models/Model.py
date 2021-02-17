from typing import Dict, Union

from modelindex import Metadata
from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.ResultList import ResultList


class Model(BaseModelIndex):

    def __init__(self,
                 name: str,
                 metadata: Union[dict, Metadata] = None,
                 results: Union[list, ResultList] = None,
                 paper: str = None,
                 code: str = None,
                 weights: str = None,
                 readme: str = None,
                 config: str = None,
                 _filepath: str = None,
                 ):
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
