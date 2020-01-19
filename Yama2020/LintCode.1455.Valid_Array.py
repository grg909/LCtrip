# -*- coding: UTF-8 -*-

# @Date    : 2020/1/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：异或运算的魔力，在算法题中最有用的位运算
"""


class Solution:
    """
    @param a: The array.
    @return: The number which has odd number of times or -1.
    """

    def isValid(self, a):
        result = 0
        for i in a:
            result ^= i
        if result in a:
            return result
        else:
            return -1
