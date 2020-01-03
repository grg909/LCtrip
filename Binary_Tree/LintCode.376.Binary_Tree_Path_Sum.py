# -*- coding: UTF-8 -*-

# @Date    : 2020/1/3
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：path类的题都要回溯（pop），才能找到所有的组合
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


# traverse, jiuzhang推荐的做法
class Solution1:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):
        if not root:
            return []

        result = []
        self.helper(root, target, [root.val], result)
        return result

    def helper(self, root, target, path, result):

        if root.left:
            path.append(root.left.val)
            self.helper(root.left, target, path, result)
            path.pop()
        if root.right:
            path.append(root.right.val)
            self.helper(root.right, target, path, result)
            path.pop()

        if not root.left and not root.right and sum(path) == target:
            result.append(list(path))


# Traverse. 我个人更喜欢这个，标准的dfs实现思路
class Solution2:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):
        if not root:
            return []

        result = []
        self.helper(root, target, [], result)
        return result

    def helper(self, root, target, path, result):
        # 4.出口
        if not root:
            return

        # 1.本层开始，看看有没有满足要求的放入result
        path.append(root.val)
        if not root.left and not root.right and sum(path) == target:
            result.append(list(path))
            path.pop()
            return

        # 2.抛出基于本层的下一层
        self.helper(root.left, target, path, result)
        self.helper(root.right, target, path, result)

        # 3.结束本层
        path.pop()
