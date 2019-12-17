# -*- coding: UTF-8 -*-

# @Date    : 2019/12/14
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # 当跳出循环时 left > right， 而此时left其实指在原来right区域的第一个值，所以可以保证left的前的所有元素都是<k
        return left
