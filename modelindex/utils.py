
def lowercase_keys(d: dict):
    """Map keys to lowercase, e.g. it will map a dict with a MODELS key into
    {"models": "MODELS"}. This allows for a unified way of naming custom-case keys.
    """
    out = {}
    for k in d.keys():
        out[k.lower()] = k

    return out
