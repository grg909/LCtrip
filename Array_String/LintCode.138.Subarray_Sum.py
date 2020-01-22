# -*- coding: UTF-8 -*-

# @Date    : 2020/1/21
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：典型prefix sum解决问题
"""


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum(self, nums):
        prefix_sum = {}
        prefix_sum[0] = 0
        sum_cur = 0

        for i in range(len(nums)):
            sum_cur += nums[i]
            if sum_cur in prefix_sum:
                return [prefix_sum[sum_cur], i]
            prefix_sum[sum_cur] = i + 1

        return [-1, -1]
