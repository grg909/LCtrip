# -*- coding: UTF-8 -*-

# @Date    : 2020/1/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        if not nums:
            return []

        start, end = 0, k
        sum_k = sum(nums[:k])
        result = [sum_k]
        while end < len(nums):
            sum_k = sum_k + nums[end] - nums[start]
            result.append(sum_k)
            start, end = start+1, end+1

        return result
