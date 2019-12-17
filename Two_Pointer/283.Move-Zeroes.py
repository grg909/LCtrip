# -*- coding: UTF-8 -*-

# @Date    : 2019/12/16
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        flag = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[flag] = nums[flag], nums[i]
                flag += 1
