# -*- coding: UTF-8 -*-

# @Date    : 2020/1/17
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, number):
        self.stack.append(number)
        if not self.minStack:
            self.minStack.append(number)
        else:
            self.minStack.append(min(number, self.minStack[-1]))

    def pop(self):
        if not self.stack:
            return None

        ret = self.stack[-1]
        del (self.stack[-1], self.minStack[-1])
        return ret

    def min(self):
        return self.minStack[-1]
