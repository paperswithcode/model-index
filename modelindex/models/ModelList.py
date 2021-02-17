from typing import List, Union, Dict

from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.Model import Model


class ModelList(BaseModelIndex):
    def __init__(self,
                 models: List[Union[Model, Dict]] = None,
                 _filepath: str = None,
                 ):

        super().__init__(
            data=models,
            filepath=_filepath
        )