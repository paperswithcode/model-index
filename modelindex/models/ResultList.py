from typing import List, Union, Dict

from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.Result import Result


class ResultList(BaseModelIndex):
    def __init__(self,
                 results: List[Union[Dict, Result]] = None,
                 _filepath: str = None,
                 ):

        super().__init__(
            data=results,
            filepath=_filepath
        )