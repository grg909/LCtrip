# -*- coding: UTF-8 -*-

# @Date    : 2019/12/4
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

# O(n)
import unittest


def string_compression(string):
    compressed = []
    counter = 0

    for i in range(len(string)):
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1

    # add the last repeated character
    compressed.append(string[-1] + str(counter))

    return min(string, ''.join(compressed), key=len)


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [('aabcccccaaa', 'a2b1c5a3'), ('abcdef', 'abcdef')]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
