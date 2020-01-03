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


# divide and conquer
class Solution1:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        is_valid, _, _ = self.helper(root)
        return is_valid

    def helper(self, root):
        if not root:
            return True, None, None

        if not root.left and not root.right:
            return True, root.val, root.val

        is_left, left_max, left_min = self.helper(root.left)
        is_right, right_max, right_min = self.helper(root.right)

        is_valid = True
        if not is_left or not is_right:
            is_valid = False
        if left_max and left_max >= root.val:
            is_valid = False
        if right_min and right_min <= root.val:
            is_valid = False
        if not left_max:
            left_max, left_min = root.val, root.val
        if not right_max:
            right_max, right_min = root.val, root.val

        return is_valid, max(left_max, right_max,
                             root.val), min(left_min, right_min, root.val)


# Traverse, easier
class Solution2:
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
