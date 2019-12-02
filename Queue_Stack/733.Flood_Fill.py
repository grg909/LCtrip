# -*- coding: UTF-8 -*-

# @Date    : 2019/12/3
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

from collections import deque


# BFS
class Solution1:

    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  newColor: int) -> List[List[int]]:

        m, n = map(len, (image, image[0]))
        around = ((1, 0), (0, -1), (-1, 0), (0, 1))

        if image[sr][sc] != newColor:
            q = deque([(sr, sc)])
            old = image[sr][sc]
            image[sr][sc] = newColor

            while q:

                x, y = q.popleft()
                image[x][y] = newColor

                for a, b in around:
                    a += x
                    b += y
                    if 0 <= a < n and 0 <= b < m and image[a][b] == old:
                        q.append((a, b))

        return image


# DFS
class Solution2:

    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  newColor: int) -> List[List[int]]:

        def dfs(i, j):
            image[i][j] = newColor
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and image[x][y] == old:
                    dfs(x, y)

        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != newColor:
            dfs(sr, sc)
        return image
