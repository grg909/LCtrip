# -*- coding: UTF-8 -*-

# @Date    : 2020/1/19
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:
    """
    @param A: a List[List[int]]
    @return: Return the maximum score of a path
    """

    def maximumMinimumPath(self, A):
        if not A:
            return -1

        max_score = 0
        self.dfs(A, 0, 0, max_score, [])

        return max_score

    def dfs(self, A, cur_x, cur_y, max_score, path):
        # out
        path.append((cur_x, cur_y))
        if cur_x == len(A) - 1 and cur_y == len(A[0]) - 1:
            score = min([A[i][j] for i, j in path])
            if score > max_score:
                max_score = score
            return

        # start a layer
        for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_x, next_y = cur_x + x, cur_y + y
            if 0 <= next_x < len(A) and 0 <= next_y <= len(A[0]) and (next_x, next_y) not in path:
                self.dfs(A, next_x, next_y, max_score, path)
                path.pop()
