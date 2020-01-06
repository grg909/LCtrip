# -*- coding: UTF-8 -*-

# @Date    : 2020/1/6
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution1:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        if not root:
            return node

        cur = root
        while cur != node:
            if node.val < cur.val:
                if not cur.left:
                    cur.left = node
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = node
                cur = cur.right
        return root


# 分治
class Solution2:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        if not root:
            return node

        if node.val < root.val:
            root.left = self.insertNode(root.left, node)
        else:
            root.right = self.insertNode(root.right, node)

        return root
