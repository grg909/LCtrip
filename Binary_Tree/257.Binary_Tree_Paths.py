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


# Traverse， dfs， 作为binary tree问题更推荐的写法
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


# 另一种Traverse， dfs的标准写法
class Solution3:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        if not root:
            return []

        result = []
        self.dfs(root, [], result)
        return result

    def dfs(self, node, path, result):
        # 出口
        if not node:
            return

        # 本层处理
        path.append(str(node.val))
        if not node.left and not node.right:
            result.append('->'.join(path))
            path.pop()
            return

        # 以本层为base的下一层
        self.dfs(node.left, path, result)
        self.dfs(node.right, path, result)

        # 结束本层
        path.pop()
