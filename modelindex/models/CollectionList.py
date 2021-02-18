from typing import List, Union, Dict

from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.Collection import Collection
from modelindex.utils import full_filepath, load_any_file, lowercase_keys


class CollectionList(BaseModelIndex):
    def __init__(self,
                 models: Union[List[Union[Collection, Dict]], Collection, Dict] = None,
                 _filepath: str = None,
                 ):

        if models is None:
            models = []

        if isinstance(models, Collection) or isinstance(models, dict):
            models = [models]

        models_parsed = []
        for m in models:
            if isinstance(m, str):
                models_parsed.append(Collection.from_file(m, _filepath))
            elif isinstance(m, Collection):
                models_parsed.append(m)
            else:
                models_parsed.append(Collection.from_dict(m, _filepath))

        super().__init__(
            data=models_parsed,
            filepath=_filepath
        )

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    @property
    def collections(self):
        return self.data

    def add(self, col: Union[Collection, Dict]):
        if isinstance(col, dict):
            self.data.append(Collection.from_dict(col, self.filepath))
        elif isinstance(col, Collection):
            self.data.append(Collection)

    @staticmethod
    def from_file(filepath: str = None, parent_filepath: str = None):
        fullpath = full_filepath(filepath, parent_filepath)
        raw, md_path = load_any_file(filepath, parent_filepath)
        d = raw

        if isinstance(d, list):
            return CollectionList(d, fullpath)
        elif isinstance(d, dict):
            lc_keys = lowercase_keys(raw)
            if "models" in lc_keys:
                return CollectionList(d[lc_keys["collections"]], fullpath)

        raise ValueError(f"Expected a list of collections, but got something else"
                         f"in file {fullpath}")
