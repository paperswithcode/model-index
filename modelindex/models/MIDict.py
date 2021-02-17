
class MIDict(dict):
    def __init__(self, d, parent_obj):
        super().__init__(d)
        self.parent_obj = parent_obj

    def __setitem__(self, item, value):
        super(MIDict, self).__setitem__(item, value)
        self.parent_obj._update_data_callback()