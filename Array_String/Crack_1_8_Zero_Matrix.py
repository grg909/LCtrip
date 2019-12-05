# -*- coding: UTF-8 -*-

# @Date    : 2019/12/4
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

# Time 0(mn), Space O(n)
import unittest
from pprint import pprint


def nullify_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0


def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


def zero_matrix1(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = []
    cols = []

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.append(x)
                cols.append(y)

    for row in rows:
        nullify_row(matrix, row)

    for col in cols:
        nullify_col(matrix, col)

    return matrix


# save space usage, but much complex
def zero_matrix2(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row_has_0 = False
    col_has_0 = False

    for i in range(n):
        if matrix[0][i] == 0:
            row_has_0 = True
            break

    for j in range(m):
        if matrix[j][0] == 0:
            col_has_0 = True
            break

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                matrix[x][0] = 0
                matrix[0][y] = 0

    for i in range(1, m):
        if matrix[i][0] == 0:
            nullify_row(matrix, i)

    for j in range(1, n):
        if matrix[0][j] == 0:
            nullify_col(matrix, j)

    if row_has_0:
        nullify_row(matrix, 0)
    if col_has_0:
        nullify_col(matrix, 0)

    return matrix


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix2(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()