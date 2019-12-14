# -*- coding: UTF-8 -*-

# @Date    : 2019/12/14
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)

    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]

        left, right = start, end
        pivot = nums[(start + end) // 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if k <= right:
            return self.quickSelect(nums, start, right, k)
        if k >= left:
            return self.quickSelect(nums, left, end, k)

        return nums[k]
