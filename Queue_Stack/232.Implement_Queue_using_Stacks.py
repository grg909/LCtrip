# -*- coding: UTF-8 -*-

# @Date    : 2019/12/2
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Queue:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inStack, self.outStack = [], []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        :param x:
        :return:
        """
        self.inStack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        :return:
        """
        self.move()
        return self.outStack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        :return:
        """
        self.move()
        return self.outStack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        :return:
        """
        return (not self.inStack) and (not self.outStack)

    def move(self) -> None:
        """
        move element from inStack to outStack when outStack is empty
        :return:
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
