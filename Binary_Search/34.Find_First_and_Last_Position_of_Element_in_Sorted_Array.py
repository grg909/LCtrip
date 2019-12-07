# -*- coding: UTF-8 -*-

# @Date    : 2019/12/7
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# 二次无脑二分模板first and last
class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        res = [-1, -1]
        if not nums:
            return res

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            res[0] = start
        elif nums[end] == target:
            res[0] = end

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                start = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            res[1] = start
        elif nums[start] == target:
            res[1] = end

        return res
