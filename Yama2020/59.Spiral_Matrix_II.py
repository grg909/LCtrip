# -*- coding: UTF-8 -*-

# @Date    : 2020/3/1
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:

    def generateMatrix(self, n: int):
        if not n:
            return []

        matrix = [[0 for i in range(n)] for j in range(n)]
        up, down = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        direct, count = 0, 0
        while True:
            if direct == 0:
                for i in range(left, right + 1):
                    count += 1
                    matrix[up][i] = count
                up += 1
            if direct == 1:
                for i in range(up, down + 1):
                    count += 1
                    matrix[i][right] = count
                right -= 1
            if direct == 2:
                for i in range(right, left - 1, -1):
                    count += 1
                    matrix[down][i] = count
                down -= 1
            if direct == 3:
                for i in range(down, up - 1, -1):
                    count += 1
                    matrix[i][left] = count
                left += 1
            if count == n**2:
                return matrix
            direct = (direct + 1) % 4
