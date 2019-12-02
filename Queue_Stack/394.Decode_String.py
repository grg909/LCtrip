# -*- coding: UTF-8 -*-

# @Date    : 2019/12/2
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:

    def decodeString(self, s: str) -> str:
        # back tracking technique
        # 用 stack 记录（[]之前的字母，翻倍次数，翻倍内容）
        stack = [['', 1, '']]
        a = n = ''
        for c in s:
            if c.isalpha():
                a += c
            elif c.isdigit():
                n += c
            elif c == '[':
                stack.append([a, int(n), ''])
            else:
                p, t, b = stack.pop()
                stack[-1][-1] += p + t * (b + a)
                a = ''

        return stack.pop()[-1] + a
