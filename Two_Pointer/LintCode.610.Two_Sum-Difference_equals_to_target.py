# -*- coding: UTF-8 -*-

# @Date    : 2019/12/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：必须小心返回值要求什么，由于返回值的限定使得此题最好用hash
    时刻注意重复的情况是否考虑到了
"""

# Description
# Given an array of integers, find two numbers that their difference equals to a target value.
# where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.
#
# Notice
# It's guaranteed there is only one available solution
#
# Example
# Given nums = [2, 7, 15, 24], target = 5
# return [1, 2] (7 - 2 = 5)

from bisect import bisect


# 同向双指针，复杂度略高, O(n^2)
# 注意，其实返回有问题，返回的是排序之后的index了
class Solution1:
    """
    @param numbers: Give an array numbers of n integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum7(self, nums, target):

        nums.sort()
        for left1 in range(len(nums) - 1):
            left2 = left1 + 1
            while left2 < len(nums):
                dif = nums[left2] - nums[left1]
                if dif == target:
                    return [left1 + 1, left2 + 1]
                elif dif < target:
                    left2 += 1
                else:
                    break


# One pass, 用binary search. Time O(nlogn)
# 注意，其实返回有点问题，返回的是排序之后的index了
class Solution2:
    """
    @param numbers: Give an array numbers of n integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum7(self, nums, target):

        nums.sort()
        for left in range(len(nums) - 1):
            res = bisect(nums, nums[left] + target)
            if nums[res - 1] - nums[left] == target:
                return [left + 1, res]


# 本题正解，还是hash
class Solution3:
    """
    @param numbers: Give an array numbers of n integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum7(self, nums, target):

        hash = {}

        for i in range(len(nums)):
            value1 = nums[i] + target
            if value1 in hash:
                return [hash[value1] + 1, i + 1]

            value2 = nums[i] - target
            if value2 in hash:
                return [hash[value2] + 1, i + 1]

            hash[nums[i]] = i


if __name__ == '__main__':
    a = Solution3()
    print(a.twoSum7([1, 22, 8, 3, 5, 2, 34, 6, 9], 6))
