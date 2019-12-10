# -*- coding: UTF-8 -*-

# @Date    : 2019/12/10
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # return -1 index is less than zero
"""

class Solution:

    def searchBigSortedArray(self, reader, target):

        if reader.get(0) == target:
            return 0

        # 乘2倍增法，动态数组实现方法
        index = 1
        while reader.get(index) < target:
            index *=2

        start, end = index/2, index
        while start + 1 < end:
            mid = (start + end) //2
            if reader.get(mid) < target:
                start = mid
            if reader.get(mid) > target:
                end = mid
            if reader.get(mid) == target:
                end = mid

        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end

        return -1