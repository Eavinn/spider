"""
自定义pool
"""

from gevent.pool import Pool as BasePool
from gevent.monkey import patch_all

patch_all()


class Pool(BasePool):
    """协程池没有close功能，故使用自定义pool"""
    def apply_async(self, func, args=None, kwds=None, callback=None):
        return super().apply_async(func, args, kwds, callback)

    def close(self):
        pass

