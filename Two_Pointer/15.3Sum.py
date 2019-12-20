# -*- coding: UTF-8 -*-

# @Date    : 2019/12/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：降维，注意coding style，可以将熟悉的部分打包为
    模块，提高代码可读性
"""


# 分解为1+2sum，two pointer, 注意跳过重复
class Solution1:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []

        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                value = nums[left] + nums[right]
                if value == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left, right = left + 1, right - 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                elif value < target:
                    left += 1
                else:
                    right -= 1

        return result


# 更好的coding style，可读性大大增强
class Solution2:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, nums):
        if not nums or len(nums) < 3:
            return []

        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.find_two_sum(nums, i + 1, len(nums) - 1, -nums[i], result)

    def find_two_sum(self, nums, left, right, target, result):
        value = nums[left] + nums[right]
        while left < right:
            if value == target:
                result.append([-target, nums[left], nums[right]])
                right -= 1
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif value > target:
                right -= 1
            else:
                left += 1
