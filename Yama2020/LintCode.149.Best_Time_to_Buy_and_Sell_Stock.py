# -*- coding: UTF-8 -*-

# @Date    : 2020/1/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""
import sys


class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        total = 0
        low, high = sys.maxsize, 0
        for i in prices:
            if i - low > total:
                total = i - low
            if i < low:
                low = i
        return total
