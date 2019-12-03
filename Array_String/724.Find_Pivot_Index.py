# -*- coding: UTF-8 -*-

# @Date    : 2019/12/3
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution1:

    def pivotIndex(self, nums: List[int]) -> int:
        sums = sum(nums)
        leftsum = 0
        for i in range(nums):
            if (2 * leftsum == sums - nums[i]):
                return 1
            else:
                leftsum += nums[i]
        return -1


class Solution2:

    def pivotIndex(self, nums: List[int]) -> int:
        l, r, diff = 0, 0, [0] * len(nums)
        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            diff[i] += l
            l += nums[i]
            diff[j] -= r
            r += nums[j]
        return diff.index(0) if 0 in diff else -1
