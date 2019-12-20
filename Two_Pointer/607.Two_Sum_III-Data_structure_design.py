# -*- coding: UTF-8 -*-

# @Date    : 2019/12/17
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：
    Two sum的变形，要注意的是还需要维护一个dict统计频次。
    在(1，2，3)中find(6)， 3和6-3都在set中，但不是有效答案，
    所以用dict统计频次是必要的。
    这道题只能用hash，不能用two pointer
"""


class TwoSum:

    data = []
    hash = {}
    """
    @param number: An integer
    @return: nothing
    """

    def add(self, number):
        # write your code here
        self.data.append(number)
        if number in self.hash:
            self.hash[number] += 1
        else:
            self.hash[number] = 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # write your code here
        for i in range(len(self.data)):
            target = value - self.data[i]
            if target in self.hash:
                if value != target or self.hash[target] > 1:
                    return True
        return False
