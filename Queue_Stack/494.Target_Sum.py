# -*- coding: UTF-8 -*-

# @Date    : 2019/12/1
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

# 不易理解，多消化


class Solution:

    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        # 定义方法有点像排列组合back tracking？
        def dfs(cur, i, d={}):
            # dfs中 d 参数传的是引用，所以只有第一次会采用默认值 {}
            if i < len(nums) and (i, cur) not in d:  # 搜索周围节点
                d[(i, cur)] = dfs(cur + nums[i], i + 1) + \
                    dfs(cur - nums[i], i + 1)
            return d.get((i, cur), int(cur == S))

        return dfs(0, 0)
