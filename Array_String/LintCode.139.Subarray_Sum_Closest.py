# -*- coding: UTF-8 -*-

# @Date    : 2020/1/21
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySumClosest(self, nums):
        prefix_sum = [(0, -1)]
        for i, num in enumerate(nums):
            prefix_sum.append((prefix_sum[-1][0] + num, i))
