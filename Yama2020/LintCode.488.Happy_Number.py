# -*- coding: UTF-8 -*-

# @Date    : 2019/12/24
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution1:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """

    def isHappy(self, n):
        process_res = set()

        while True:
            nums = self.int_to_array(n)
            n = self.array_to_int(nums)
            if n == 1 or n in process_res:
                break
            process_res.add(n)

        return n == 1

    def int_to_array(self, n):
        nums = []
        while n:
            nums.append(n % 10)
            n = n // 10
        return nums

    def array_to_int(self, nums):
        res = 0
        for i in nums:
            res += i**2
        return res


# this is really fucking pythonic
class Solution2:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        d = {}
        while True:
            d[n] = 1
            n = sum([int(x) * int(x) for x in list(str(n))])
            if n == 1 or n in d:
                break
        return n == 1
