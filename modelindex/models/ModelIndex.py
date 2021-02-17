from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.CollectionList import CollectionList
from modelindex.models.ModelList import ModelList
from modelindex.utils import lowercase_keys, load_any_file


class ModelIndex(BaseModelIndex):
    def __init__(self,
                 data: dict = None,
                 filepath: str = None,
                 ):

        if data is None:
            data = {}

        d = {
            "Models": ModelList(),
            "Collections": CollectionList(),
        }
        lc_keys = lowercase_keys(data)
        if "models" in lc_keys:
            models = data[lc_keys["models"]]
            if models is not None and not isinstance(models, ModelList):
                models = ModelList(models)

            d["Models"] = models

        if "collections" in lc_keys:
            collections = data[lc_keys["collections"]]
            if collections is not None and not isinstance(collections, CollectionList):
                collections = CollectionList(collections)

            d["Collections"] = collections

        if "import" in lc_keys:
            imp = data[lc_keys["import"]]

            if not isinstance(imp, list):
                imp = list(imp)

            for import_file in imp:
                raw, md_name = load_any_file(import_file, filepath)

                raw_lc_keys = lowercase_keys(raw)
                if "models" in raw_lc_keys:
                    additional_models = raw[raw_lc_keys["models"]]
                    if not isinstance(additional_models, list):
                        additional_models = list(additional_models)
                    for model in additional_models:
                        d["Models"].add(model)

                if "collections" in raw_lc_keys:
                    additional_cols = raw[raw_lc_keys["collections"]]
                    if not isinstance(additional_cols, list):
                        additional_cols = list(additional_cols)
                    for col in additional_cols:
                        d["Collections"].add(col)

        super().__init__(
            data=d,
            filepath=filepath
        )

        self.lc_keys = lowercase_keys(data)

    @staticmethod
    def from_dict(d: dict, filepath: str = None):
        return ModelIndex(d, filepath)

    @property
    def models(self):
        return self.data["Models"]

    @models.setter
    def models(self, value):
        self.data["Models"] = value

    @property
    def collections(self):
        return self.data["Collections"]

    @collections.setter
    def collections(self, value):
        self.data["Collections"] = value
