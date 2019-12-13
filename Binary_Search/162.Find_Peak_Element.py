# -*- coding: UTF-8 -*-

# @Date    : 2019/12/13
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end)//2
            if nums[mid-1] < nums[mid] < nums[mid+1]:
                start = mid
            elif nums[mid-1] > nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid

        return start if nums[start] > nums[end] else end