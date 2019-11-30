# -*- coding: UTF-8 -*-

# @Date    : 2019/12/1
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        stack = []
        d = {'(': ')', '[': ']', '{': '}'}

        for i in s:
            if i in '{[(':
                stack.append(i)
            else:
                if not stack or i != d[stack.pop()]:
                    return False
        return True
