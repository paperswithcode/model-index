from modelindex.consts import MODEL_INDEX_ROOT_FILE


class BaseModelIndex:

    def __init__(self,
                 data: dict = None,
                 filepath: str = MODEL_INDEX_ROOT_FILE,
                 ):

        if data is None:
            data = {}

        self.filepath = filepath
        self.data = data


