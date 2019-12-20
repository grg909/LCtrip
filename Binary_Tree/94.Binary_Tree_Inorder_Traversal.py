# -*- coding: UTF-8 -*-

# @Date    : 2019/12/19
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    必须bug free no recursion
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion 1: Traverse
# 类似preorder，见前

# Recursion 2: Divide & Conquer
# 类似preorder，见前


# Non-recursion. Stack
class Solution3:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        if not root:
            return res

        # 创建一个dummy node，右指针指向root并放到stack中
        # 此时stack的栈顶dummy是iterator的当前位置
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        # 每次将 iterator 挪到下一个点
        # 也就是调整 stack 使得栈顶到下一个点
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                res.append(stack[-1].val)

        return res


# 更好的模板，非迭代
class Solution4:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []

        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)  # add after all left children
                cur = cur.right

        return res


# Morris method
class Solution5:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        pass
