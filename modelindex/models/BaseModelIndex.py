from typing import List, Union, Dict, Set
from ordered_set import OrderedSet


class BaseModelIndex:
    def __init__(self,
                 data: Union[List, Dict] = None,
                 filepath: str = None,
                 check_errors: Union[List, Set, OrderedSet] = None,
                 ):
        if data is None:
            data = {}

        self.filepath = filepath
        self.data = data
        self.check_errors = OrderedSet(check_errors)
        self._iterator_inx = 0

        # always call checking
        self._check(silent=True)

    def _check(self, silent: bool = False):
        pass

    def collect_check_errors(self, display_type: str = None):
        clname = type(self).__name__

        if display_type is None:
            display_type = clname

        collected = [
            {
                "filepath": self.filepath,
                "errors": self.check_errors,
                "type": display_type,
            }
        ]
        if self.data:
            objs = None
            if isinstance(self.data, list):
                # If it's a list, enumerate the position
                proper_name = clname
                if clname == "ResultList":
                    proper_name = "Results"
                elif clname == "ModelList":
                    proper_name = "Models"
                elif clname == "CollectionList":
                    proper_name = "Collections"

                objs = {}
                for i in range(0, len(self.data)):
                    objs[f"{proper_name}[{i}]"] = self.data[i]

            elif isinstance(self.data, dict):
                # if dictionary, just use it
                objs = self.data

            # recursively collect all errors
            if objs:
                for name, obj in objs.items():
                    if isinstance(obj, BaseModelIndex):
                        collected.extend(obj.collect_check_errors(name))

        return collected

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
