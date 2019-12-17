# -*- coding: UTF-8 -*-

# @Date    : 2019/12/16
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

# Description
# Given an array of integers, remove the duplicate numbers in it.
#
# You should:
# 1. Do it in place in the array.
# 2. Move the unique numbers to the front of the array.
# 3. Return the total number of the unique numbers.
#
#
# Notice
# You don't need to keep the original order of the integers.
#
#
#
# Example
# Given nums = [1,3,1,4,4,2], you should:
#
# Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
# Return the number of unique integers in nums => 4.
# Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.
#
#
#
# Challenge
# Do it in O(n) time complexity.
# Do it in O(nlogn) time without extra space.


# Use hashset. Time O(n). Space O(n)
class Solution1:

    def removeDuplicates(self, nums):
        if not nums:
            return -1

        hash = set()

        flag = 0
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = 1
                nums[flag] = nums[i]
                flag += 1

        return flag


# Sort it, use two pinter. Time O(nlogn)
class Solution2:

    def removeDuplicates(self, nums):
        if not nums:
            return -1

        nums.sort()

        flag = 1
        for i in range(len(nums)):
            if nums[i] != nums[flag - 1]:
                nums[flag] = nums[i]
                flag += 1

        return flag
