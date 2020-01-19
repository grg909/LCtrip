# -*- coding: UTF-8 -*-

# @Date    : 2020/1/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：每个位置上的盛水数目 = min(左侧最高，右侧最高) - 当前高度
"""
import sys


class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """

    def trapRainWater(self, heights):
        if not heights:
            return 0

        left_max = []
        curt_max = -sys.maxsize
        for height in heights:
            curt_max = max(curt_max, height)
            left_max.append(curt_max)

        right_max = []
        curt_max = -sys.maxsize
        for height in reversed(heights):
            curt_max = max(curt_max, height)
            right_max.append(curt_max)

        right_max = right_max[::-1]

        water = 0
        for i in range(len(heights)):
            water += min(left_max[i], right_max[i]) - heights[i]

        return water
