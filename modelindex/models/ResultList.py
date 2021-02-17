from typing import List, Union, Dict

from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.Result import Result


class ResultList(BaseModelIndex):
    def __init__(self,
                 results: Union[List[Union[Dict, Result]], Result, Dict] = None,
                 _filepath: str = None,
                 ):

        if results is None:
            results = []

        if isinstance(results, Result) or isinstance(results, dict):
            results = [results]

        results_parsed = []
        for r in results:
            if isinstance(r, Result):
                results_parsed.append(r)
            else:
                results_parsed.append(Result.from_dict(r))

        super().__init__(
            data=results_parsed,
            filepath=_filepath
        )

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __len__(self):
        return len(self.data)