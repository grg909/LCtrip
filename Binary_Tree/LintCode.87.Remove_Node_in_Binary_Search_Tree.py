# -*- coding: UTF-8 -*-

# @Date    : 2020/1/6
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：重点是如何build一个新的BST，根据中序遍历的结果
"""


class Solution:
    """
    @param root: The root of the binary search tree.
    @param value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    ans = []

    def removeNode(self, root, value):
        self.inorder(root, value)
        return self.build(0, len(self.ans) - 1)

    def inorder(self, root, value):
        if not root:
            return

        self.inorder(root.left, value)
        if root.val != value:
            self.ans.append(root.val)
        self.inorder(root.right, value)

    def build(self, left, right):
        if left == right:
            node = TreeNode(self.ans[left])
            return node

        if left > right:
            return None

        mid = (left + right) // 2
        node = TreeNode(self.ans[mid])
        node.left = self.build(left, mid - 1)
        node.right = self.build(mid + 1, right)
        return node
