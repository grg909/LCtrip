# -*- coding: UTF-8 -*-

# @Date    : 2019/12/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    这道题用two pointer更好(因为用two pointer前提就是已排序，且不用额外空间)，当然hash也行
"""


class Solution:
    """
    @param nums {int[]} n array of Integer
    @param target {int} = nums[index1] + nums[index2]
    @return {int[]} [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            value = nums[left] + right
            if value == target:
                return [left + 1, right + 1]
            elif value < target:
                left += 1
            else:
                right -= 1

        return []
