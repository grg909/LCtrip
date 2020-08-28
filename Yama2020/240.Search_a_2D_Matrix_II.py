# -*- coding: UTF-8 -*-

# @Date    : 2020/3/1
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        cur_x, cur_y = len(matrix)-1, 0
        while 0 <= cur_x < len(matrix) and 0 <= cur_y < len(matrix[0]):
            if matrix[cur_x][cur_y] == target:
                return True
            elif matrix[cur_x][cur_y] > target:
                cur_x -= 1
            elif matrix[cur_x][cur_y] < target:
                cur_y += 1

        return False