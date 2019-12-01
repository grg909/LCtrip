# -*- coding: UTF-8 -*-

# @Date    : 2019/12/1
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 初始化栈，用栈储存未处理的数字
        stack = []

        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            else:
                a = stack.pop()
                stack[-1] = int(eval(str(stack[-1]) + i + a))

        return stack[-1]


# Better implementation
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        dic = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }
        stack = []

        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            else:
                a = stack.pop()
                stack[-1] = dic[i](stack[-1], a)

        return stack[-1]
