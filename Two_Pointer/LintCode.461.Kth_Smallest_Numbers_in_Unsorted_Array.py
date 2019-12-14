# -*- coding: UTF-8 -*-

# @Date    : 2019/12/14
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

# Description
# Find the kth smallest numbers in an unsorted integer array.
#
# Example
# Given [3, 4, 1, 2, 5], k = 3, the 3rd smallest numbers are [1, 2, 3].
#
# Challenge
# An O(nlogn) algorithm is acceptable, if you can do it in O(n), that would be great.


class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """

    def kthSmallest(self, k, nums):
        return self.quickSelect(nums, 0, len(nums) - 1, k - 1)

    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]

        left, right = start, end
        pivot = nums[(left + right) // 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if right >= k and start <= right:
            return self.quickSelect(nums, start, right, k)
        elif left <= k and left <= end:
            return self.quickSelect(nums, left, end, k)


if __name__ == '__main__':
    a = Solution()
    a.kthSmallest(3, [9, 3, 2, 4, 8])
