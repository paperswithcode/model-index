
class BaseModelIndex:

    def __init__(self,
                 data: dict = None,
                 filepath: str = None,
                 ):
        if data is None:
            data = {}

        self.filepath = filepath
        self.data = data
