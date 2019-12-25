# -*- coding: UTF-8 -*-

# @Date    : 2019/12/25
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：二分搜索要熟练
"""


class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):

        m, n = len(matrix), len(matrix[0])

        start, end = 0, m * n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[mid // n][mid % n] == target:
                end = mid
            elif matrix[mid // n][mid % n] > target:
                end = mid
            else:
                start = mid

        if matrix[start // n][start % n] == target:
            return True
        if matrix[end // n][end % n] == target:
            return True

        return False
