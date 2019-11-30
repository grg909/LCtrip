# -*- coding: UTF-8 -*-

# @Date    : 2019/12/1
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        r = [0] * len(T)

        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                c = stack.pop()
                r[c] = i - c
            stack.append(i)

        return r
