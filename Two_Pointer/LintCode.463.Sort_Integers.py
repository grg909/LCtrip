# -*- coding: UTF-8 -*-

# @Date    : 2019/12/16
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# 标准的快排实现
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    def sortColors(self, nums):
        # write your code here
        if not nums:
            return

        self.quickSort(nums, 0, len(nums) - 1)

    def quickSort(self, nums, start, end):
        if start >= end:
            return

        left, right = start, end
        # 1. pivot, nums[start], nums[end]
        # get value not index
        pivot = nums[(start + end) // 2]

        # 2. left <= right not <
        while left <= right:
            while left <= right and nums[left] < pivot: # not <=
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.quickSort(nums, start, right)
        self.quickSort(nums, left, end)
