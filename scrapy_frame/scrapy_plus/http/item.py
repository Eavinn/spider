"""
三大内置对象：数据对象
"""


class Item(object):
    """数据类"""
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data
