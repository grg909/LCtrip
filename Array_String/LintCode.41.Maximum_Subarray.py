# -*- coding: UTF-8 -*-

# @Date    : 2020/1/20
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：令PrefixSum[i] = A[0] + A[1] + … A[i - 1], PrefixSum[0] = 0
    计算子数组从下标i到下标j之间的所有数之和则有
    Sum(i~j) = PrefixSum[j + 1] - PrefixSum[i]  (重要解题技巧)
"""
import sys


class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        min_pre_sum = 0
        max_sub_sum = -sys.maxsize
        sum_cur = 0

        for i in nums:
            sum_cur += i
            sub_sum = sum_cur - min_pre_sum
            max_sub_sum = max(max_sub_sum, sub_sum)
            min_pre_sum = min(min_pre_sum, sum_cur)

        return max_sub_sum
