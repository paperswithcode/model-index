import os
import copy
from typing import Dict, Union, List

from ordered_set import OrderedSet

from modelindex.models.Metadata import Metadata
from modelindex.models.BaseModelIndex import BaseModelIndex
from modelindex.models.Result import Result
from modelindex.models.ResultList import ResultList
from modelindex.utils import lowercase_keys, full_filepath, load_any_file, expand_wildcard_path, merge_lists_data


class Library(BaseModelIndex):
    """Library contains metadata about the software library providing the models.
    """
    COMMON_FIELDS = [
        "Name",
        "Repository",
        "Headline",
        "Website",
        "Docs",
        "README",
        "Image",
    ]

    def __init__(self,
                 name: str = None,
                 repository: str = None,
                 headline: str = None,
                 website: str = None,
                 docs: str = None,
                 readme: str = None,
                 image: str = None,
                 _filepath: str = None,
                 _path_to_readme: str = None,
                 **kwargs,
                 ):
        """
        Args:
            name (str): Name of the library
            repository (str): URL to the library code repository
            headline (str): A short description that will appear below the title
            website (str): URL to the website of the library (if different from code repository)
            docs (str): URL to documentation
            readme (str): path to the README file for the library
            image (str): path or URL to an image for the library
            _filepath: The file path to where the data was loaded from
            _path_to_readme: Path to the markdown readme file if data is coming from there
            **kwargs: Any other custom fields
        """

        check_errors = OrderedSet()

        d = {
            "Name": name,
            "Repository": repository,
            "Headline": headline,
            "Website": website,
            "Docs": docs,
            "README": readme,
            "Image": image,
            **kwargs,
        }

        # Only non-empty items
        data = {k: v for k, v in d.items() if v is not None}

        self._path_to_readme = _path_to_readme

        super().__init__(
            data=data,
            filepath=_filepath,
            check_errors=check_errors,
        )

    def _check(self, silent=True):
        if self.name is None or self.name == "":
            self.check_errors.add("Field 'Name' cannot be empty")

        if self._readme_is_filepath() and not self._path_to_readme:
            # check if the README exists
            fullpath = full_filepath(self.readme, self.filepath)
            if not os.path.isfile(fullpath):
                self.check_errors.add(f"Path to README file {self.readme} is not a valid file.")

        if self.image and not self.image.startswith("http"):
            fullpath = full_filepath(self.image, self.filepath)
            if not os.path.isfile(fullpath):
                self.check_errors.add(f"Path to Image file {self.image} is not a valid file.")

    @classmethod
    def from_dict(cls, d: Dict, _filepath: str = None, _path_to_readme: str = None):
        """Create a Library from a dictionary.

        Args:
            d (dict): dictionary containing library data
            _filepath (str): The file path to where the data was loaded from
            _path_to_readme (str): Path to the README file if metadata was extracted from a README
        """
        lc_keys = lowercase_keys(d)

        copy_fields = [
            "name",
            "repository",
            "headline",
            "website",
            "docs",
            "readme",
            "image",
        ]

        dd = d.copy()
        for field_name in copy_fields:
            key = field_name.lower()
            if key in lc_keys:
                dd[field_name] = dd.pop(lc_keys[key])

            # try with _ instead of space in the field name
            if " " in field_name:
                key = field_name.lower().replace(" ", "_")
                if key in lc_keys:
                    dd[field_name] = dd.pop(lc_keys[key])

        if _path_to_readme:
            dd["readme"] = _path_to_readme

        return cls(
            _filepath=_filepath,
            _path_to_readme=_path_to_readme,
            **dd,
        )

    @staticmethod
    def from_file(filepath: str = None, parent_filepath: str = None):
        """Load a Library from a file.

        Args:
            filepath (str): File from which to load the library
            parent_filepath (str): Parent filename (if file is imported from another file)
        """
        fullpath = full_filepath(filepath, parent_filepath)
        raw, md_path = load_any_file(filepath, parent_filepath)
        d = raw
        if isinstance(raw, dict):
            lc_keys = lowercase_keys(raw)
            if "library" in lc_keys:
                d = raw[lc_keys["library"]]

            return Library.from_dict(d, fullpath, md_path)
        else:
            raise ValueError(f"Expected a library dict, but got "
                             f"something else in file '{fullpath}'")

    def _readme_is_filepath(self):
        return self.readme and self.readme.endswith(".md") and len(self.readme) < 256

    def readme_content(self):
        """Get the content of the README file (instead of just the path as returned by .readme())"""

        if not self.readme:
            return None
        elif self._path_to_readme:
            with open(self.filepath, "r") as f:
                return f.read()
        elif self._readme_is_filepath():
            if self.filepath:
                fullpath = full_filepath(self.readme, self.filepath)
            else:
                fullpath = self.readme
            with open(fullpath, "r") as f:
                return f.read()
        else:
            return self.readme

    # Getters
    @property
    def name(self):
        """Get the library name"""
        return self.data.get("Name", None)

    @property
    def repository(self):
        """Get the library repository"""
        return self.data.get("Repository", None)

    @property
    def headline(self):
        """Get a short description of the library"""
        return self.data.get("Headline", None)

    @property
    def website(self):
        """Get the URL to the website"""
        return self.data.get("Website", None)

    @property
    def docs(self):
        """Get the URL to documentation"""
        return self.data.get("Docs", None)

    @property
    def readme(self):
        """Get the path to the library README"""
        return self.data.get("README", None)

    @property
    def image(self):
        """Get the path or URL to the image for the library"""
        return self.data.get("Image", None)

    # Setters
    @name.setter
    def name(self, value):
        self.data["Name"] = value

    @repository.setter
    def repository(self, value):
        self.data["Repository"] = value

    @headline.setter
    def headline(self, value):
        self.data["Headline"] = value

    @website.setter
    def website(self, value):
        self.data["Website"] = value

    @docs.setter
    def docs(self, value):
        self.data["Docs"] = value

    @readme.setter
    def readme(self, value):
        self.data["README"] = value

    @image.setter
    def image(self, value):
        self.data["Image"] = value

