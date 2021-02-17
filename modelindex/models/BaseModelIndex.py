from typing import List, Union, Dict


class BaseModelIndex:

    def __init__(self,
                 data: Union[List,Dict] = None,
                 filepath: str = None,
                 ):
        if data is None:
            data = {}

        self.filepath = filepath
        self.data = data
