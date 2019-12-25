# -*- coding: UTF-8 -*-

# @Date    : 2019/12/25
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# 由于obstacles的存在，在很多地方增加了corner case，要仔细考虑
class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        mp = {}
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    mp[(i, j)] = 0
                elif i == 0 and j == 0:
                    mp[(i, j)] = 1 - obstacleGrid[i][j]
                elif i == 0:
                    if obstacleGrid[i][j]:
                        mp[(i, j)] = 0
                    else:
                        mp[(i, j)] = mp[(i, j - 1)]
                elif j == 0:
                    if obstacleGrid[i][j]:
                        mp[(i, j)] = 0
                    else:
                        mp[(i, j)] = mp[(i - 1, j)]
                else:
                    mp[(i, j)] = mp[(i - 1, j)] + mp[(i, j - 1)]
        return mp[(m - 1, n - 1)]
