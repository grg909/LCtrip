# -*- coding: UTF-8 -*-

# @Date    : 2019/12/23
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:

    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        results = []
        if not candidates:
            return results
        candidates.sort()
        self.dfs(candidates, 0, [], target, results)
        return results

    # 递归的定义
    def dfs(self, candidates, startIndex, combination, target, results):
        # 3. 递归的出口
        if target == 0:
            results.append(list(combination))

        # 2. 递归的拆解
        for i in range(startIndex, len(candidates)):
            if i != startIndex and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                break
            combination.append(candidates[i])
            self.dfs(candidates, i, combination, target - candidates[i],
                     results)
            combination.pop()
