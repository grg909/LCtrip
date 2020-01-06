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


# dfs
class Solution1:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        return self.helper(root, None, None)

    # 这个方法的定义min_n, max_n是当前root为根的树中
    # 所有节点中的最大值和最小值
    def helper(self, root, min_n, max_n):
        if not root:
            return True

        if (min_n and root.val <= min_n) or (max_n and root.val >= max_n):
            return False

        return self.helper(root.left, min_n, root.val) and self.helper(
            root.right, root.val, max_n)


# divide and conquer, 此法简单直接
class Solution2:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        is_bst, _, _ = self.helper(root)
        return is_bst

    def helper(self, root):
        if not root:
            return True, None, None

        is_left, left_min, left_max = self.helper(root.left)
        is_right, right_min, right_max = self.helper(root.right)

        # 只要判定False情况就不用管最大最小值了，因为只有出现
        # 一个subtree非BST，整个tree都不是BST了
        if not is_left or not is_right:
            return False, None, None
        if left_max and left_max >= root.val:
            return False, None, None
        if right_min and root.val >= right_min:
            return False, None, None

        # is BST
        min_tree = left_min if left_min else root.val
        max_tree = right_max if right_max else root.val

        return True, min_tree, max_tree


# Traverse
# 每次用当前节点和左子树遍历过的最后一个节点做比较。
# 如果最后一个节点的值小，就说明这不是一个BST。因为BST的任何一个节点比左边大。
class Solution3:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    last_val = None
    is_valid = True

    def isValidBST(self, root):
        self.helper(root)
        return self.is_valid

    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        if self.last_val and self.last_val >= root.val:
            self.is_valid = False
            return
        self.last_val = root.val
        self.helper(root.right)
