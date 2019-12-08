# -*- coding: UTF-8 -*-

# @Date    : 2019/12/8
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# version 1
class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self._array = []
        self._sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self._sum += val
        self._array.append(val)
        if len(self._array) > self.size:
            self._sum -= self._sum.pop(0)
        return self._sum / len(self._array)


class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self._id = 0
        self._sum = [0 * (size + 1)]

    def _mod(self, indx):
        return indx % (self.size + 1)

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self._id += 1
        self._sum[self._mod(
            self._id)] = self._sum[self._mod(self._id - 1)] + val
        if self._id - self.size >= 0:
            return self._sum[self._mod(
                self._id)] - self._sum[self._mod(self._id) -
                                       self.size] / self.size
        else:
            return self._sum[self._id] / self._id
