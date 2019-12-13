# -*- coding: UTF-8 -*-

# @Date    : 2019/12/13
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# Time O(m + n)
class Solution:

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        row, col = len(matrix) - 1, 0
        while row >= 0 and col < len(matrix[0] - 1):
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True

        return False
