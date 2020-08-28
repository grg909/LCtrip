# -*- coding: UTF-8 -*-

# @Date    : 2020/3/14
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# traverse, Time O(2^n), Space O(n)
class Solution1:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.mini = sys.maxsize
        self.dfs(triangle, 0, 0, 0)
        return self.mini

    def dfs(self, triangle, x, y, pathSum):
        if x == len(triangle) - 1:
            self.mini = min(self.mini, pathSum + triangle[x][y])
            return

        self.dfs(triangle, x + 1, y, pathSum + triangle[x][y])
        self.dfs(triangle, x + 1, y + 1, pathSum + triangle[x][y])


# Divide & Conquer
class Solution2:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.findMin(triangle, 0, 0)

    # the minimum sum of path that start from (x, y)
    def findMin(self, triangle, x, y):
        if x == len(triangle) - 1:
            return triangle[x][y]

        return triangle[x][y] + min(self.findMin(triangle, x + 1, y),
                                    self.findMin(triangle, x + 1, y + 1))


# DP(DFS + memory), 由于有了缓存，每一个点访问两次，因此 Time 0(n^2), Space O(n^2)
class Solution3:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memory = dict()
        return self.findMin(triangle, 0, 0, memory)

    # the minimum sum of path that start from (x, y)
    def findMin(self, triangle, x, y, memory):
        if x == len(triangle) - 1:
            memory[(x, y)] = triangle[x][y]
            return triangle[x][y]

        if (x, y) in memory:
            return memory[(x, y)]

        memory[(x, y)] = triangle[x][y] + min(
            self.findMin(triangle, x + 1, y, memory),
            self.findMin(triangle, x + 1, y + 1, memory))
        return memory[(x, y)]
