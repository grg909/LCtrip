# -*- coding: UTF-8 -*-

# @Date    : 2019/12/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告: 降维，coding style
"""

# Description
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.
#
# Notice
# You may assume that each input would have exactly one solution.
#
# Example
# For example, given array S = [-1 2 1 -4], and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
# Challenge
# O(n^2) time, O(1) extra space

import sys


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """

    def threeSumClosest(self, numbers, target):
        if not numbers or len(numbers) < 3:
            return -1

        numbers.sort()
        result = None
        for i in range(len(numbers) - 2):
            self.find_two_closed(numbers, numbers[i], i + 1,
                                 len(numbers) - 1, target, result)

        return result

    def find_two_closed(self, numbers, first_num, left, right, target, result):
        while left < right:
            sum = first_num + numbers[left] + numbers[right]
            if result is None or abs(sum - target) < abs(result - target):
                result = sum
            if sum > target:
                right -= 1
            else:
                left += 1
