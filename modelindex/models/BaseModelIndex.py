import os

from typing import List, Union, Dict, Set
from ordered_set import OrderedSet


class BaseModelIndex:

    COMMON_FIELDS = []

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
            If silent: list of errors

        """
        errors = self.collect_check_errors()

        # only keep non-empty
        errors = [e for e in errors if e["errors"]]

        errors_formatted = []
        for e in errors:
            for msg in e["errors"]:
                fp = e["filepath"]
                if self.filepath:
                    # generate relative paths if possible
                    fp = os.path.relpath(fp, os.path.dirname(self.filepath))

                errors_formatted.append(
                    "%s: %s: %s" % (
                        fp,
                        e["type"],
                        msg
                    )
                )

        if not silent:
            for e in errors_formatted:
                print(e)
            # Return false if there are errors
            if not errors_formatted:
                print("All good!")
        else:
            return errors_formatted

    def _str_for_dict_with_padding(self, padding=2):
        """Produce a nice string for __str__ that describes this object.

        Args:
            padding (int): number of spaces to indent
        """
        # padding at this level of indentation
        pad = " "*padding
        last_pad = " "*(padding-2)

        # concatenate common fields
        out = []
        d = self.data.copy()
        for field in self.COMMON_FIELDS:
            if field in d:
                val = d.pop(field)
                if isinstance(val, BaseModelIndex):
                    val_str = val._str_with_padding(padding+2)
                else:
                    val_str = str(val)
                out.append(f"{field}={val_str}")

        # add any remaining
        if d:
            out.append(f"custom={d}")

        if self.filepath:
            out.append(f"_filepath={self.filepath}")

        name = type(self).__name__

        if out:
            return f"{name}(\n{pad}%s\n{last_pad})" % f",\n{pad}".join(out)
        else:
            return f"{name}()"

    def _str_with_padding(self, padding=2):
        # if dict use the default
        if isinstance(self.data, dict):
            return self._str_for_dict_with_padding(padding)
        elif isinstance(self.data, list):
            # if list assume it's a list of dicts
            out = []
            for d in self.data:
                if isinstance(d, BaseModelIndex):
                    out.append(d._str_for_dict_with_padding(padding+2))

            pad = " " * padding
            last_pad = " " * (padding - 2)
            if out:
                return f"[\n{pad}%s,\n{last_pad}]" % f",\n{pad}".join(out)
            else:
                return f"[]"

        else:
            return super().__str__()

    def __str__(self):
        return self._str_with_padding()

    def __repr__(self):
        return self.__str__()
