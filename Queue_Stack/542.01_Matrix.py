# -*- coding: UTF-8 -*-

# @Date    : 2019/12/3
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""
from collections import deque


class Solution:

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = map(len, (matrix, matrix[0]))
        around = ((0, 1), (1, 0), (0, -1), (-1, 0))
        r = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                # -------------------------BFS 开始--------------------------
                q = deque([(i, j, 0)])
                seen = {(i, j)}

                # 循环取节点
                while q:
                    a, b, t = q.popleft()
                    if not matrix[a][b]:
                        r[i][j] = t
                        break

                    # 放入邻节点
                    for x, y in around:
                        x, y = x + a, y + b
                        if 0 <= x < n and 0 <= y < m and (x, y) not in seen:
                            seen.add((x, y))
                            q.append((x, y, t + 1))
                # ----------------------------------------------------------
        return r
