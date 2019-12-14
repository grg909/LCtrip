# -*- coding: UTF-8 -*-

# @Date    : 2019/11/19
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start = 0
        count = len(nums) + 1
        sum_n = 0
        for i in range(len(nums)):
            sum_n += nums[i]
            while sum_n >= s:
                count = min(count, i - start + 1)
                sum_n -= nums[start]
                start += 1
        if count != len(nums) + 1:
            return count
        else:
            return 0
