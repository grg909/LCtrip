# -*- coding: UTF-8 -*-

# @Date    : 2019/11/23
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# sliding window
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for i in range(len(nums)):
            prod *= nums[i]
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += i - left + 1
        return ans
