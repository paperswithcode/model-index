from modelindex.consts import MODEL_INDEX_ROOT_FILE


class BaseModelIndex:

    def __init__(self, filepath=MODEL_INDEX_ROOT_FILE):
        self.filepath = filepath


