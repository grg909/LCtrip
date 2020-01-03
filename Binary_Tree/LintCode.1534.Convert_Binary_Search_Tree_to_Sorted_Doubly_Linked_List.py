# -*- coding: UTF-8 -*-

# @Date    : 2020/1/3
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """

    def treeToDoublyList(self, root):
        if not root:
            return root
        first = None
        last = None
        prev = None

        # iterate the tree like a list
        for v in self.inorder(root):
            if first is None:
                first = v
            last = v
            if prev:
                prev.right = v
                v.left = prev
            prev = v
        first.left = last
        last.right = first
        return first

    # 此处用yield方便，但是继承基本的inorder模板
    def inorder(self, root):
        stack = []

        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                yield cur
                cur = cur.right
