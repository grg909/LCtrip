# -*- coding: UTF-8 -*-

# @Date    : 2019/12/25
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# DP
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        # python用dict来代替二维数组，避免浅拷贝的问题
        mp = {}
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    mp[(i, j)] = 1
                else:
                    mp[(i, j)] = mp[(i - 1, j)] + mp[(i, j - 1)]
        return mp[(m - 1, n - 1)]
