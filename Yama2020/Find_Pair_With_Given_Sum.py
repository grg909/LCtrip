# -*- coding: UTF-8 -*-

# @Date    : 2020/3/1
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:

    def givenSum(self, nums, target):
        if not nums:
            return []
        hashT = dict()
        res = []
        target = target - 30
        for i in range(len(nums)):
            if target - nums[i] in hashT:
                if hashT[target - nums[i]] + i > sum(res):
                    res = [hashT[target - nums[i]], i]
            hashT[nums[i]] = i

        return res


if __name__ == '__main__':
    a = Solution()
    print(a.givenSum([0, 0], target=30))
