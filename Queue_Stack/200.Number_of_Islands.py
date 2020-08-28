# -*- coding: UTF-8 -*-

# @Date    : 2019/11/30
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

from collections import deque

# BFS


class Solution:

    def numIslands(self, grid) -> int:

        try:
            m = len(grid)
            n = len(grid[0])
        except BaseException:
            return 0

        r = 0
        around = ((0, 1), (1, 0), (0, -1), (-1, 0))

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


# DFS
class Solution2:

    def numIslands(self, grid) -> int:
        try:
            m = len(grid)
            n = len(grid[0])
        except BaseException:
            return 0

        # -------------------------DFS 开始------------------------
        # 定义dfs递归方程
        around = ((1, 0), (0, -1), (-1, 0), (0, 1))

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and int(grid[i][j]):
                grid[i][j] = '0'
                for a, b in around:
                    dfs(a + i, b + j)

        r = 0
        for i in m:
            for j in n:
                if int(grid[i][j]):
                    r += 1
                    dfs(i, j)
        return r


from collections import deque


class Solution3:

    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        island = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if int(grid[i][j]) and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    island += 1

        print(island)
        return island

    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_x = x + delta_x
                next_y = y + delta_y
                if self.is_valid(grid, next_x, next_y, visited):
                    queue.append((next_x, next_y))
                    visited.add((next_x, next_y))

    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in visited:
            return False
        return int(grid[x][y]) == 1

if __name__ == '__main__':
    a = Solution3()
    a.numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
                  ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]])
