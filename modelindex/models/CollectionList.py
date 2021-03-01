from typing import List, Union, Dict

from ordered_set import OrderedSet

from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.Collection import Collection
from modelindex.utils import full_filepath, load_any_file, lowercase_keys, expand_wildcard_path


class CollectionList(BaseModelIndex):
    """A list of Collection objects."""
    def __init__(self,
                 collections: Union[List[Union[Collection, Dict]], Collection, Dict] = None,
                 _filepath: str = None,
                 _path_to_readme: str = None,
                 ):
        """
        Args:
            collections (list,Collection,dict): Either a list of Collection objects, a single Collection object or a
                                                dict representing a Collection
            _filepath (str): The file path to where the data was loaded from
            _path_to_readme (str): Path to README if it was loaded from there

        """

        if collections is None:
            collections = []

        if isinstance(collections, Collection) or isinstance(collections, dict):
            collections = [collections]

        models_parsed = []
        check_errors = OrderedSet()
        for m in collections:
            if isinstance(m, str):
                # link to collection file, support wildcards
                for model_file in expand_wildcard_path(m, _filepath):
                    try:
                        model = Collection.from_file(model_file, _filepath)
                        if isinstance(model, Collection):
                            models_parsed.append(model)
                        elif isinstance(model, CollectionList):
                            models_parsed.extend(model)
                    except (IOError, ValueError) as e:
                        check_errors.add(str(e))
            elif isinstance(m, Collection):
                models_parsed.append(m)
            else:
                models_parsed.append(Collection.from_dict(m, _filepath, _path_to_readme))

        super().__init__(
            data=models_parsed,
            filepath=_filepath,
            check_errors=check_errors,
        )

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __iter__(self):
        self._iterator_inx = 0
        return self

    def __next__(self):
        if self._iterator_inx < len(self.data):
            self._iterator_inx += 1
            return self.data[self._iterator_inx - 1]
        else:
            raise StopIteration

    def __len__(self):
        return len(self.data)

    @property
    def collections(self):
        """Get the list of Collection objects"""
        return self.data

    def add(self, col: Union[Collection, Dict], _filepath: str = None):
        """Add a Collection to the list.

        Args:
            col (Collection, dict): Either a Collection or a dict representing a collection
            _filepath (str): The path from which it was loaded

        """
        col_filepath = _filepath if _filepath is not None else self.filepath
        if isinstance(col, dict):
            self.data.append(Collection.from_dict(col, col_filepath))
        elif isinstance(col, Collection):
            self.data.append(col)

    @staticmethod
    def from_file(filepath: str = None, parent_filepath: str = None):
        """Load a Collection from a file.

        Args:
            filepath (str): File from which to load the collection
            parent_filepath (str): Parent filename (if file is imported from another file)
        """

        fullpath = full_filepath(filepath, parent_filepath)
        raw, md_path = load_any_file(filepath, parent_filepath)
        d = raw

        if isinstance(d, list):
            return CollectionList(d, fullpath)
        elif isinstance(d, dict):
            lc_keys = lowercase_keys(raw)
            if "collections" in lc_keys:
                return CollectionList(d[lc_keys["collections"]], fullpath)

        raise ValueError(f"Expected a list of collections, but got something else"
                         f"in file {fullpath}")
