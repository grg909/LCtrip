# -*- coding: UTF-8 -*-

# @Date    : 2019/12/20
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution1:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # deal with empty
        if not root:
            return []

        # deal with leaf
        if not root.left and not root.right:
            return [str(root.val)]

        # divide
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)

        # conquer
        res = []
        for path in left + right:
            res.append(str(root.val) + '->' + path)

        return res


# Traverse， dfs
class Solution2:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        result = []
        self.dfs(root, [str(root.val)], result)
        return result

    def dfs(self, node, path, result):
        if not node.left and not node.right:
            result.append('->'.join(path))

        if node.left:
            path.append(str(node.left.val))
            self.dfs(node.left, path, result)
            path.pop()

        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, path, result)
            path.pop()
