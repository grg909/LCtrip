# -*- coding: UTF-8 -*-

# @Date    : 2019/12/2
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

from collections import deque


class Stack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque([])

    def push(self, x) -> None:
        """
        Push element x onto stack.
        :param x:
        :return:
        """
        self.q.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        :return:
        """
        if self.empty():
            # 由于deque的rotate方向是朝右，所以用负值！
            self.q.rotate(1 - len(self.q))
            return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        :return:
        """
        r = self.pop()
        self.q.append(r)
        return r

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        :return:
        """
        return not self.q
