# -*- coding: UTF-8 -*-

# @Date    : 2019/12/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：类似LintCode 609, same strategy
"""

# Description
# Given an array of integers, find how many pairs in the array such that their sum
# is bigger than a specific target number. Please return the number of pairs.
#
#
# Example
# Given numbers = [2, 7, 11, 15], target = 24. Return 1. (11 + 15 is the only pair)
#
# Challenge
# Do it in O(1) extra space and O(nlogn) time.


class Solution:
    """
    @param: nums: an array of integer
    @param: target: An integer
    @return: An integer
    """

    def twoSum2(self, nums, target):
        if not nums or len(nums) < 2:
            return 0

        nums.sort()
        count = 0

        left, right = 0, len(nums) - 1
        while left < right:
            value = nums[left] + nums[right]
            if value > target:
                count += right - left
                right -= 1
            else:
                left += 1

        return count
