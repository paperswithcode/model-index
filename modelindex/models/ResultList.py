from typing import List, Union, Dict

from ordered_set import OrderedSet

from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.Result import Result
from modelindex.utils import full_filepath, load_any_file, lowercase_keys


class ResultList(BaseModelIndex):
    def __init__(self,
                 results: Union[List[Union[Dict, Result, str]], Result, Dict] = None,
                 _filepath: str = None,
                 ):

        check_errors = OrderedSet()

        if results is None:
            results = []

        if isinstance(results, Result) or isinstance(results, dict):
            results = [results]

        results_parsed = []
        for r in results:
            if isinstance(r, str):
                try:
                    results_parsed.append(Result.from_file(r, _filepath))
                except (IOError, ValueError) as e:
                    check_errors.add(str(e))
            elif isinstance(r, Result):
                results_parsed.append(r)
            else:
                results_parsed.append(Result.from_dict(r, _filepath))

        super().__init__(
            data=results_parsed,
            filepath=_filepath,
            check_errors=check_errors,
        )

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __len__(self):
        return len(self.data)

    @staticmethod
    def from_file(filepath: str = None, parent_filepath: str = None):
        fullpath = full_filepath(filepath, parent_filepath)
        raw, md_path = load_any_file(filepath, parent_filepath)
        d = raw

        if isinstance(d, list):
            return ResultList(d, fullpath)
        elif isinstance(d, dict):
            lc_keys = lowercase_keys(raw)
            if "results" in lc_keys:
                return ResultList(d[lc_keys["results"]], fullpath)

        raise ValueError(f"Expected a list of results, but got something else"
                         f"in file {fullpath}")
