import os
from typing import List, Dict

import yaml
import json
import markdown
import glob
from html.parser import HTMLParser


class CommentHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.extracted_comments = []

    def handle_comment(self, data):
        self.extracted_comments.append(data)


def lowercase_keys(d: dict):
    """Map keys to lowercase, e.g. it will map a dict with a MODELS key into
    {"models": "MODELS"}. This allows for a unified way of naming custom-case keys.
    """
    out = {}
    for k in d.keys():
        out[k.lower()] = k

    return out


def load_raw_from_markdown(path: str):
    """Load raw metadata from a markdown file

        Args:
            path (str): Path to the markdown file
    """

    with open(path, "r") as f:
        md = markdown.markdown(f.read())

    parser = CommentHTMLParser()
    parser.feed(str(md))
    comments = parser.extracted_comments

    # try to interpret as a yaml file
    metadata = []
    for comment in comments:
        try:
            parsed = yaml.load(comment, Loader=yaml.SafeLoader)
            if isinstance(parsed, dict):
                lc_keys = lowercase_keys(parsed)
                if "type" in lc_keys and (
                        parsed[lc_keys["type"]].lower() == "model-index"
                        or
                        parsed[lc_keys["type"]].lower() == "modelindex"
                ):
                    metadata.append(parsed)
        except Exception:
            pass

    # if there are many metadata entries, merge them
    meta_dict = {}
    for m in metadata:
        for key, value in m.items():
            if key not in meta_dict:
                meta_dict[key] = value
            else:
                cur = meta_dict[key]
                if not isinstance(cur, list):
                    cur = [cur]
                if isinstance(value, list):
                    cur.extend(value)
                else:
                    cur.append(value)

                meta_dict[key] = cur

    return meta_dict


def full_filepath(path: str, cur_filepath: str = None):
    """Return the full file path based on a possibly relative path (path)
    and the current file path (cur_filepath)
    """
    if cur_filepath is not None:
        dirname = os.path.dirname(cur_filepath)
        if dirname:
            path = os.path.join(dirname, path)

    return path


def expand_wildcard_path(path: str, cur_filepath: str = None):
    if "*" not in path and "?" not in path:
        return [path]
    else:
        # we need absolute paths for glob
        path = full_filepath(path, cur_filepath)
        fullpaths = glob.glob(path)

        # but we'll return relative paths so convert back
        if cur_filepath is not None:
            base_path = os.path.dirname(cur_filepath)
            return sorted([os.path.relpath(fp, base_path) for fp in fullpaths])
        else:
            return sorted(fullpaths)


def load_any_files_wildcard(path: str, cur_filepath: str = None):
    """Load any supported file format, supporting wildcard matches as well.

    Args:
        path (str): Path to files (including any wildcards)
        cur_filepath (str): The path to the current file from which we
                            are loading the new file
                            (important for relative paths)

    """

    out = []
    # to do globs we need the absolute path
    for filepath in expand_wildcard_path(path, cur_filepath):
        out.append(load_any_file(filepath, cur_filepath))

    return out


def load_any_file(path: str, cur_filepath: str = None):
    """Load any of the supported file formats

        Args:
            path (str): Path to the file to load
            cur_filepath (str): The path to the current file from which we
                                are loading the new file
                                (important for relative paths)

        Returns:
            (raw, md_path) - where raw is the loaded content of the file (normally a dict)
            and md_path is the file to the markdown path (if loaded from markdown)
    """

    relative_path = path
    path = full_filepath(path, cur_filepath)

    if not os.path.exists(path):
        raise IOError(f"File '{path}' does not exist.")

    md_path = None
    if path.endswith(".yml") or path.endswith(".yaml"):
        with open(path, "r") as f:
            raw = yaml.load(f, Loader=yaml.SafeLoader)
    elif path.endswith(".json"):
        with open(path, "r") as f:
            raw = json.load(f)
    elif path.endswith(".md"):
        md_path = relative_path
        raw = load_raw_from_markdown(path)
    else:
        raise ValueError(f"File type at path '{path}' not recognized. We support YAML (.yml or .yaml), "
                         f"JSON (.json) and markdown (.md) files.")

    return raw, md_path


def merge_lists_data(list_objs: List):
    """Take multiple e.g. ResultList objects and merge them together into one
       by concatenating the data lists.
    """
    if list_objs:
        objs1 = list_objs[0]
        # Merge data from all files
        if len(list_objs) > 1:
            for i in range(1, len(list_objs)):
                objs1.data.extend(list_objs[i].data)
        return objs1
    else:
        return list_objs


def merge_dicts(dict_list: List[Dict]):
    if dict_list:
        if len(dict_list) == 1:
            return dict_list[0]
        else:
            # merge dictionaries
            out = {}
            for d in dict_list:
                out.update(d)
            return out
    else:
        return None
