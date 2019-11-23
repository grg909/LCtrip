# -*- coding: UTF-8 -*-

# @Date    : 2019/11/17
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    Minimum Moves to Equal Array Elements
"""


class Solution():

    def minMove(self, nums):
        """

        :param nums: List[int]
        :return: int
        """
        count = 0
        while (True):
            max1, min1 = max(nums), min(nums)
            if (max1 == min1):
                break
            idx, count = nums.index(max1), count + 1
            for i in range(len(nums)):
                nums[i] = nums[i] + 1 if i != idx else nums[i]
            return count
