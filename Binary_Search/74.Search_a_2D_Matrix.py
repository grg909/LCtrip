# -*- coding: UTF-8 -*-

# @Date    : 2019/12/11
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

# 思路1，把二维数组扁平化
class Solution:
    def searchMatrix(self, matrix, target):
        try:
            n, m = len(matrix), len(matrix[0])
        except:
            return False

        start, end = 0, n*m -1
        while start + 1 < end:
            mid = (start + end)//2
            x, y = mid/m, mid%m
            if matrix[x][y] > target:
                end = mid
            else:
                start = mid

        x, y = start/m, start%m
        if matrix[x][y] == target:
            return True

        x, y = end / m, end % m
        if matrix[x][y] == target:
            return True

        return False
