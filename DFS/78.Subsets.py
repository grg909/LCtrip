# -*- coding: UTF-8 -*-

# @Date    : 2019/12/21
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：使用组合类搜索的专用深度优先搜索算法。
    一层一层的决策每个数要不要放到最后的集合里。
"""
from collections import deque

# BFS, not recommend for this kind of combination search problem
class Solution1:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        nums.sort()
        queue = deque([])
        queue.append([])

        while queue:
            subset = queue.popleft()
            res.append(subset)

            for i in nums:
                if not subset or subset[-1] < i:
                    nextSubset = list(subset)
                    nextSubset.append(i)
                    queue.append(nextSubset)

        return res


# DFS, 推荐使用的组合类深度搜索模板
class Solution2:

    results = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.dfs(nums, 0, [])
        return self.results

    # 1. 递归的定义
    # 以subset开头的，配上nums以index开始的数所有组合放到results里
    def dfs(self, nums, index, subset):
        # 3. 递归的出口
        # 此处，python需要格外注意深拷贝和浅拷贝问题
        if index == len(nums):
            self.results.append(list(subset))
            return

        # 2. 递归的拆解: 如何进入下一层
        # 选了 nums[index]
        subset.append(nums[index])
        self.dfs(nums, index + 1, subset)

        # 不选 nums[index]
        subset.pop()
        self.dfs(nums, index + 1, subset)
