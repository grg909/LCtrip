# -*- coding: UTF-8 -*-

# @Date    : 2020/3/1
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

class Solution:
    def uniqueTwoSum(self, nums, target):
        nums.sort()
        count = 0
        left, right = 0, len(nums)-1
        while left < right:
            sumPair = nums[left] + nums[right]
            if sumPair == target:
                count += 1
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif sumPair > target:
                right -= 1
            else:
                left += 1

        return count


if __name__ == '__main__':
    a = Solution()
    print(a.uniqueTwoSum([1, 1], target = 2))