from modelindex.models.MIDict import MIDict


class BaseModelIndex:

    def __init__(self,
                 data: dict = None,
                 filepath: str = None,
                 ):
        if data is None:
            data = {}

        self.filepath = filepath
        self.data = MIDict(data, self)

    def _update_data_callback(self):
        pass
