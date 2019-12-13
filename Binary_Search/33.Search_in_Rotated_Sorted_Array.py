# -*- coding: UTF-8 -*-

# @Date    : 2019/12/13
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""
from bisect import bisect


# 用一次二分
class Solution1:

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] >= nums[start]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[start] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1


# 用两次二分， 第一步 find minimum number in rotated sorted array
# 然后在确定区间里再搜索
class Solution2:

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        index = self.find_min_index(nums)
        if nums[index] <= target <= nums[-1]:
            return self.binary_search(nums, index, len(nums) - 1, target)
        return self.binary_search(nums, 0, index - 1, target)

    def binary_search(self, A, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1

    def find_min_index(self, nums):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > end:
                start = mid
            else:
                end = mid

        return start if nums[start] < nums[end] else end
