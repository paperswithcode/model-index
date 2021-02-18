from typing import List, Union, Dict


class BaseModelIndex:

    def __init__(self,
                 data: Union[List,Dict] = None,
                 filepath: str = None,
                 check_errors: List = None,
                 ):
        if data is None:
            data = {}

        self.filepath = filepath
        self.data = data

        if check_errors is None:
            check_errors = []
        self.check_errors = check_errors

        # always call checking
        self.check(silent=True)

    def check(self, silent: bool = False):
        pass
