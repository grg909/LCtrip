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
        dic = {'(': ')', '[': ']', '{': '}'}

        for char in s:
            if char in '{[(':
                stack.append(char)
            else:
                if not stack or char != dic[stack.pop()]:
                    return False
        return not stack
