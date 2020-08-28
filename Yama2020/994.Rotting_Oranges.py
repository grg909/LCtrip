# -*- coding: UTF-8 -*-

# @Date    : 2020/3/1
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

from collections import deque


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        rotten = [
            [i, j] for i in range(row) for j in range(col) if grid[i][j] == 2
        ]
        offset = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque(rotten)
        time = 0

        while queue:
            new = []
            for i, j in queue:
                for dire in offset:
                    ni, nj = i + dire[0], j + dire[1]
                    if 0 <= ni < row and 0 <= nj < col and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        new.append([ni, nj])
            queue = new
            if not queue:
                break
            time += 1

        if any(1 in i for i in grid):
            return -1

        return time
