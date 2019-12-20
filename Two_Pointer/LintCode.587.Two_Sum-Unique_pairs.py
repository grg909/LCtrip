# -*- coding: UTF-8 -*-

# @Date    : 2019/12/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：双指针注意跳过重复(注意while left < right 的一致性)。
    hash略麻烦，需要记录元素是否available(用0，1), 注意(1，3，3，3，5)，target=6中3的情况,
    别想去重，去重就干掉了3的情况
"""

# Description
# Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.
#
# Example
# Given nums = [1,1,2,45,46,46], target = 47
# return 2
#
# 1 + 46 = 47
# 2 + 45 = 47


# Two pointer
class Solution1:
    """
    @param: nums: an array of integer
    @param: target: An integer
    @return: An integer
    """

    def twoSum6(self, nums, target):

        if not nums or len(nums) < 2:
            return 0

        nums.sort()

        count = 0
        left, right = 0, len(nums) - 1
        while left < right:
            value = nums[left] + nums[right]
            if value == target:
                count, left, right = count + 1, left + 1, right - 1
                while left < right and nums[left - 1] == nums[left]:
                    left += 1
                while left < right and nums[right + 1] == nums[right]:
                    right -= 1
            elif value < target:
                left += 1
            else:
                right -= 1

        return count


# hash
class Solution2:
    """
    @param: nums: an array of integer
    @param: target: An integer
    @return: An integer
    """

    def twoSum6(self, nums, target):

        if not nums or len(nums) < 2:
            return 0

        hash = {}
        count = 0

        for i in range(len(nums)):
            value = target - nums[i]
            if value in hash:
                if hash[value] == 1:
                    count += 1
                    hash[value] = 0
            if nums[i] not in hash:
                hash[nums[i]] = 1

        return count


if __name__ == '__main__':
    a = Solution2()
    print(a.twoSum6([1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 7], 6))
