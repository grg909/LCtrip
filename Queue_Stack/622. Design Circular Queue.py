# -*- coding: UTF-8 -*-

# @Date    : 2019/11/30
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :param k:
        :return:
        """
        self.size = 0
        self.max_size = k
        self.data = [0] * k
        self.front = self.rear = -1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :param value:
        :return:
        """
        if self.isFull():
            return False

        if self.rear == -1:
            self.rear = self.front = 0
        else:
            self.rear = (self.rear + 1) % self.max_size

        self.data[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :return:
        """
        if self.isEmpty():
            return False

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        :return:
        """
        return self.data[self.front] if self.size != 0 else -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        :return:
        """
        return self.data[self.rear] if self.size != 0 else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        :return:
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        :return:
        """
        return self.size == self.max_size
