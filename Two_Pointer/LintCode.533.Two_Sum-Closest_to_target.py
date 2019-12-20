# -*- coding: UTF-8 -*-

# @Date    : 2019/12/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告： Two pointer,需要有一个全局dif每次比较更新
"""

# Description
# Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.
#
# Return the difference between the sum of the two integers and the target.
#
# Example
# Given array nums = [-1, 2, 1, -4], and target = 4.
#
# The minimum difference is 1. (4 - (2 + 1) = 1).
#
# Challenge
# Do it in O(nlogn) time complexity.

import sys


class Solution:
    """
    @param: nums: an array of integer
    @param: target: An integer
    @return: the difference between the sum and the target
    """

    def twoSumClosest(self, nums, target):
        if not nums or len(nums) < 2:
            return -1

        nums.sort()
        dif = sys.maxsize

        left, right = 0, len(nums) - 1
        while left < right:
            value = nums[left] + nums[right]
            if value == target:
                return 0
            if value < target:
                dif = min(dif, target - value)
                left += 1
            if value > target:
                dif = min(dif, target - value)
                right -= 1

        return dif
