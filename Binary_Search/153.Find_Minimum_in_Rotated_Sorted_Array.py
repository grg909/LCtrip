# -*- coding: UTF-8 -*-

# @Date    : 2019/12/10
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# 每次都和end比，注意必须是end不是start，因为有[1,2,3]这种特殊情况
class Solution:
    """
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin(self, nums):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid

        return min(nums[start], nums[end])
