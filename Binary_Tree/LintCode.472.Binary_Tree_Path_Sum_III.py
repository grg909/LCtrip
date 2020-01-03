# -*- coding: UTF-8 -*-

# @Date    : 2020/1/3
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：现在的题意是可以从任何一点出发，而且有parent节点。
    那么我们其实是traverse一遍这棵树，在每一点，我们出发找有没有符合条件的路径。
    在每一点我们可以有三个方向：左边，右边，和上面。但是我们需要避免回头，所以需要一个previous节点的参数。
"""
"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    # @param {ParentTreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum3(self, root, target):
        results = []
        self.dfs(root, target, results)
        return results

    def dfs(self, root, target, results):
        if not root:
            return

        path = []
        self.findSum(root, None, target, path, results)

        self.dfs(root.left, target, results)
        self.dfs(root.right, target, results)

    def findSum(self, root, previous, target, path, results):
        path.append(root.val)
        target -= root.val

        if target == 0:
            results.append(list(path))

        if root.parent and root.parent != previous:
            self.findSum(root.parent, root, target, path, results)

        if root.left and root.left != previous:
            self.findSum(root.left, root, target, path, results)

        if root.right and root.right != previous:
            self.findSum(root.right, root, target, path, results)

        path.pop()
