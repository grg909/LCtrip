# -*- coding: UTF-8 -*-

# @Date    : 2019/12/22
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：背subsets的模板3
    既然要求Unique的，就想办法排除掉重复的，选择一个“代表”
    选代表：一般排序选第一个？
    去重一般在求解过程中排除选择就好，不要到最终结果里去重
"""


# DFS 模板
class Solution1:

    results = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.dfs(nums, 0, [])
        return self.results

    def dfs(self, nums, startIndex, subset):
        self.results.append(list(subset))

        for i in range(startIndex, len(nums)):
            # 举例，避免前后都是1，上一层没选的情况下，下一层选了就重复
            # 如{1, 2(1), 2(2)}，规定{1, 2(1)}和{1, 2(2)}重复
            if i > startIndex and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset)
            subset.pop()


# Non-recursive
class Solution2:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        pass
