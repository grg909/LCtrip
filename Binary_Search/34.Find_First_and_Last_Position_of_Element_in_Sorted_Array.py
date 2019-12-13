# -*- coding: UTF-8 -*-

# @Date    : 2019/12/7
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""
import bisect


# 二次无脑二分模板first and last
class Solution1:

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


# 用 python bisect
class Solution2:

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first = bisect.bisect_left(nums, target)
        last = bisect.bisect(nums, target)

        # the indices will be equal only if the target is not in the list
        if first == last:
            return [-1, -1]

        # last是最后一个目标值的下一个位置
        return [first, last-1]


# 机智的方法，只用一种binery search，自己实现binary/bisect都可
class Solution3:

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first = bisect.bisect_left(nums, target)
        # 因为有序性
        last = bisect.bisect_left(nums, target+1)

        # the indices will be equal only if the target is not in the list
        if first == last:
            return [-1, -1]

        # last是最后一个目标值的下一个位置
        return [first, last-1]