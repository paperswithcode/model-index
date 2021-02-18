from typing import List, Union, Dict, Set
from ordered_set import OrderedSet


class BaseModelIndex:
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

        # always call checking
        self.check(silent=True)

    def check(self, silent: bool = False):
        pass
