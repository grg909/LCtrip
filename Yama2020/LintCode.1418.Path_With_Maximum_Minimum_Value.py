# -*- coding: UTF-8 -*-

# @Date    : 2020/1/19
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告: 这题要求所有路径中最小值的最大值，因此每一步
    都保证走最大权值的那个方向就能满足要求，所以说到底是一个带权值的最短路径问题
"""

import heapq as hq


# Pure DFS， TLE
class Solution1:
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
            if 0 <= next_x < len(A) and 0 <= next_y <= len(
                    A[0]) and (next_x, next_y) not in path:
                self.dfs(A, next_x, next_y, max_score, path)
                path.pop()


# DFS + memo
class Solution2:
    """
    @param A: a List[List[int]]
    @return: Return the maximum score of a path
    """

    def maximumMinimumPath(self, A):
        pass


# Dijkstra (BFS + max heap, 一般用于解决带正数权值最短路径问题)
# Dijkstra算法的seen的处理要放到外面来，不可在for循环内
# 只有当点被pop出来了，才能算被seen了，这样如果有同一个点
# 第二次进入队列的权重比第一次大，该弹出第二次
class Solution3:
    """
    @param A: a List[List[int]]
    @return: Return the maximum score of a path
    """

    def maximumMinimumPath(self, A):
        min_num = A[0][0]
        seen = set()
        start, end = (0, 0), (len(A) - 1, len(A[0]) - 1)
        # priority queue
        pqueue = []
        hq.heappush(pqueue, (-A[0][0], start))
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pqueue:
            num, node = hq.heappop(pqueue)
            min_num = min(min_num, -num)
            seen.add(node)
            if node == end:
                return min_num

            for move in moves:
                next_row = node[0] + move[0]
                next_col = node[1] + move[1]
                if next_row < 0 or next_row >= len(
                        A) or next_col < 0 or next_col >= len(
                            A[0]) or (next_row, next_col) in seen:
                    continue
                hq.heappush(pqueue,
                            (-A[next_row][next_col], (next_row, next_col)))

        return -1
