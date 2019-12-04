# -*- coding: UTF-8 -*-

# @Date    : 2019/12/4
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""
import unittest
from copy import deepcopy
from pprint import pprint


def rotate_matrix1(matrix):

    n = len(matrix)

    for i in range(n // 2):
        for j in range(n):
            matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 -
                                                        i][j], matrix[i][j]

    for i in range(n):
        j = 0
        while j < i:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            j += 1

    pprint(matrix)
    return matrix


# better implementation
def rotate_matrix2(matrix):
    """rotates a matrix 90 degrees clockwise"""
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - 1 - layer
        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-1 - layer][-1 - i]

            # right -> bottom
            matrix[-1 - layer][-1 - i] = matrix[i][-1 - layer]

            # top -> right
            matrix[i][-1 - layer] = top

    return matrix


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix1(self):
        for [test_matrix, expected] in deepcopy(self.data):
            actual = rotate_matrix1(test_matrix)
            self.assertEqual(actual, expected)

    def test_rotate_matrix2(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix2(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
