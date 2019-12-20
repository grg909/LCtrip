# -*- coding: UTF-8 -*-

# @Date    : 2019/12/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：1.可以降维到3 sum，时间复杂度 O(N^3)
    2. hash, 时间复杂度 O(N^2), 难点在去重
    3. 递归，可以用记忆化搜索来优化
"""


class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """

    def fourSum(self, numbers, target):
        # write your code here
        if not numbers or len(numbers) < 4:
            return []
        hash = {}
