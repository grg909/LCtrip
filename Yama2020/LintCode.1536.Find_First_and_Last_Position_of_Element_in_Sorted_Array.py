# -*- coding: UTF-8 -*-

# @Date    : 2019/12/25
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

import bisect


class Solution:
    """
    @param nums: the array of integers
    @param target:
    @return: the starting and ending position
    """

    def searchRange(self, nums, target):
        first = bisect.bisect_left(nums, target)
        # 因为有序性
        last = bisect.bisect_left(nums, target + 1)

        # the indices will be equal only if the target is not in the list
        if first == last:
            return [-1, -1]

        # last是最后一个目标值的下一个位置
        return [first, last - 1]
