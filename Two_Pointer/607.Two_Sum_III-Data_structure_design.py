# -*- coding: UTF-8 -*-

# @Date    : 2019/12/17
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class TwoSum:

    data = []
    """
    @param number: An integer
    @return: nothing
    """

    def add(self, number):
        # write your code here
        self.data.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # write your code here
        hash = set()
        for i in range(len(self.data)):
            if value - self.data[i] in hash:
                return True
            hash.add(self.data[i])

        return False
