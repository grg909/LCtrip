# -*- coding: UTF-8 -*-

# @Date    : 2019/12/14
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return left
