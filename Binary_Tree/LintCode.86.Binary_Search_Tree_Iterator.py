# -*- coding: UTF-8 -*-

# @Date    : 2020/1/3
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：非常标准的in-order stack遍历模板
    Split the iterative in order traversal into sub functions.
    Time complexity for hasNext() and next() are O(1).
    Space complexity is O(h) where h is the height of the tree.
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """

    def __init__(self, root):
        self.stack = []
        self.cur = root

    """
    @return: True if there has next node, or false
    """

    def hasNext(self):
        return self.cur or len(self.stack)

    """
    @return: return next node
    """

    def next(self):
        while self.cur or self.stack:
            if self.cur:
                self.stack.append(self.cur)
                self.cur = self.cur.left
            else:
                self.cur = self.stack.pop()
                nxt = self.cur
                self.cur = self.cur.right
                return nxt
