# -*- coding: UTF-8 -*-

# @Date    : 2020/3/13
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


# Bottom-up method DP, most memory efficient. Time O(n^2), Space O(n).
# 多重循环DP，思考有难度
class Solution1:

    def getRow(self, rowIndex: int) -> List[int]:
        res = [0] * (1 + rowIndex)
        res[0] = 1
        for row in range(rowIndex + 1):
            for i in range(row, 0, -1):
                res[i] += res[i - 1]

        return res


# DFS, Time O(2^n), Space O(n)
class Solution2:

    def getRow(self, rowIndex: int) -> List[int]:
        res = [0] * (1 + rowIndex)
        for i in range(rowIndex + 1):
            res[i] = self.getNum(rowIndex, i)

        return res

    def getNum(self, rowIndex, i):
        if rowIndex == 0 or i == 0 or i == rowIndex:
            return 1

        return self.getNum(rowIndex - 1, i) + self.getNum(rowIndex - 1, i - 1)


# DP, Top-down with memory. Time O(n^2), Space O(n^2)
# 记忆化搜索DP，容易想到，属于DFS的优化
class Solution3:

    def getRow(self, rowIndex: int) -> List[int]:
        res = [0] * (1 + rowIndex)
        memory = dict()
        for colIndex in range(rowIndex + 1):
            res[colIndex] = self.getNum(rowIndex, colIndex, memory)

        return res

    def getNum(self, row, col, memory):
        if row == 0 or col == 0 or col == row:
            return 1

        if (row, col) in memory:
            return memory[row, col]

        memory[row, col] = self.getNum(row - 1, col, memory) + self.getNum(
            row - 1, col - 1, memory)
        return memory[row, col]
