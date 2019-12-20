# -*- coding: UTF-8 -*-

# @Date    : 2019/12/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：先排序，然后Two pointer.
    关键在于，如果发现一对nums[i]+nums[j] <= target, 那么
    nums[i] + i 到 j之间的任何数都会小于target。
"""

# Description
# Given an array of integers, find how many pairs in the array such that their sum is
# less than or equal to a specific target number. Please return the number of pairs.
#
# Example
# Given nums = [2, 7, 11, 15], target = 24.
# Return 5.
# 2 + 7 < 24
# 2 + 11 < 24
# 2 + 15 < 24
# 7 + 11 < 24
# 7 + 15 < 25


class Solution:
    """
    @param: nums: an array of integer
    @param: target: An integer
    @return: An integer
    """

    def twoSum5(self, nums, target):
        if not nums or len(nums) < 2:
            return 0

        nums.sort()
        count = 0

        left, right = 0, len(nums) - 1
        while left < right:
            value = nums[left] + nums[right]
            if value <= target:
                count += right - left
                left += 1
            else:
                right -= 1

        return count
