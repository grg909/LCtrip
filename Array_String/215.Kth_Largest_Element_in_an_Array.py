# -*- coding: UTF-8 -*-

# @Date    : 2019/12/8
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k < 1 or k > len(nums):
            return -1
        #                                            此处因为求从大到小第k
        return self.partition(nums, 0, len(nums) - 1, len(nums) - k)

    def partition(self, nums, start, end, k):
        """During the process, it's guaranteed start <= k <= end"""
        if start == end:
            return nums[k]

        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right -  1

        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)

        return nums[k]
