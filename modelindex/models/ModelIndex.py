from ordered_set import OrderedSet

from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.CollectionList import CollectionList
from modelindex.models.ModelList import ModelList
from modelindex.utils import lowercase_keys, load_any_file, full_filepath


class ModelIndex(BaseModelIndex):
    def __init__(self,
                 data: dict = None,
                 filepath: str = None,
                 ):

        check_errors = OrderedSet()

        if data is None:
            data = {}

        d = {
            "Models": ModelList(_filepath=filepath),
            "Collections": CollectionList(_filepath=filepath),
        }
        lc_keys = lowercase_keys(data)
        if "models" in lc_keys:
            models = data[lc_keys["models"]]
            if models is not None and isinstance(models, str):
                try:
                    models = ModelList.from_file(models, filepath)
                except (IOError, ValueError) as e:
                    check_errors.add(str(e))
            elif models is not None and not isinstance(models, ModelList):
                models = ModelList(models, filepath)

            d["Models"] = models

        if "collections" in lc_keys:
            collections = data[lc_keys["collections"]]
            if collections is not None and isinstance(collections, str):
                try:
                    collections = CollectionList.from_file(collections, filepath)
                except (IOError, ValueError) as e:
                    check_errors.add(str(e))
            elif collections is not None and not isinstance(collections, CollectionList):
                collections = CollectionList(collections, filepath)

            d["Collections"] = collections

        if "import" in lc_keys:
            imp = data[lc_keys["import"]]

            if not isinstance(imp, list):
                imp = list(imp)

            for import_file in imp:
                try:
                    fullpath = full_filepath(import_file, filepath)
                    raw, md_name = load_any_file(import_file, filepath)

                    raw_lc_keys = lowercase_keys(raw)
                    if "models" in raw_lc_keys:
                        additional_models = raw[raw_lc_keys["models"]]
                        if not isinstance(additional_models, list):
                            additional_models = list(additional_models)
                        for model in additional_models:
                            d["Models"].add(model, fullpath)

                    if "collections" in raw_lc_keys:
                        additional_cols = raw[raw_lc_keys["collections"]]
                        if not isinstance(additional_cols, list):
                            additional_cols = list(additional_cols)
                        for col in additional_cols:
                            d["Collections"].add(col, fullpath)
                except (IOError, ValueError) as e:
                    check_errors.add(str(e))

        super().__init__(
            data=d,
            filepath=filepath,
            check_errors=check_errors,
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

    def check(self, silent=False):
        """Check if the mandatory fields are present and if file references are valid.

        Args:
            silent (bool): If to return a list of errors without printing them out

        Returns:
            A list of errors

        """
        errors = self.collect_check_errors()

        # only keep non-empty
        errors = [e for e in errors if e["errors"]]

        errors_formatted = []
        for e in errors:
            for msg in e["errors"]:
                errors_formatted.append(
                    "%s: %s: %s" % (
                        e["filepath"],
                        e["type"],
                        msg
                    )
                )

        if not silent:
            for e in errors_formatted:
                print(e)
        else:
            return errors_formatted
