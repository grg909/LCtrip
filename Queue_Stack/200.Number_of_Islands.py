# -*- coding: UTF-8 -*-

# @Date    : 2019/11/30
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

from collections import deque


class Solution:

    def numIslands(self, grid):

        try:
            r = 0
            m = len(grid)
            n = len(grid[0])
            around = ((0, 1), (1, 0), (0, -1), (-1, 0))
        except BaseException:
            return 0

        for i in range(m):
            for j in range(n):
                if int(grid[i][j]):
                    r += 1

                    # ---------------------------BFS 开始------------------------
                    # 把根节点投入队列
                    q = deque([])
                    q.append((i, j))
                    grid[i][j] = '0'

                    while q:
                        x, y = q.popleft()

                        # 访问了根节点，放入其周围可继续探索的陆地节点
                        for a, b in around:
                            a += x
                            b += y
                            if 0 <= a < m and 0 <= b < n and int(grid[a][b]):
                                grid[a][b] = '0'
                                q.append((a, b))
                    # ----------------------------------------------------------------

        return r
