from modelindex.models.Model import Model
from modelindex.utils import full_filepath, load_any_file, lowercase_keys


class Collection(Model):

    @staticmethod
    def from_file(filepath: str = None, parent_filepath: str = None):
        fullpath = full_filepath(filepath, parent_filepath)
        raw, md_path = load_any_file(filepath, parent_filepath)
        d = raw
        if isinstance(raw, dict):
            lc_keys = lowercase_keys(raw)
            if "collection" in lc_keys:
                d = raw[lc_keys["collection"]]
            elif "collections" in lc_keys:
                # called Collection.from_file() on a collection list, fallback to CollectionList
                d = raw[lc_keys["collections"]]
                if isinstance(d, list):
                    from modelindex.models.CollectionList import CollectionList
                    return CollectionList(d, fullpath)

            return Collection.from_dict(d, fullpath, md_path)
        else:
            raise ValueError(f"Expected a collection dict, but got "
                             f"something else in file '{fullpath}'")

