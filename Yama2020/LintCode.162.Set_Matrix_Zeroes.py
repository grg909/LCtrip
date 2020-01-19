# -*- coding: UTF-8 -*-

# @Date    : 2020/1/18
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:
    """
    @param matrix: A lsit of lists of integers
    @return: nothing
    """

    def setZeroes(self, matrix):
        if not matrix:
            return

        row_num = len(matrix)
        col_num = len(matrix[0])
        row = [False] * row_num
        col = [False] * col_num
        for i in range(row_num):
            for j in range(col_num):
                if not matrix[i][j]:
                    row[i] = True
                    col[j] = True

        for i in range(row_num):
            for j in range(col_num):
                if row[i] or col[j]:
                    matrix[i][j] = 0
