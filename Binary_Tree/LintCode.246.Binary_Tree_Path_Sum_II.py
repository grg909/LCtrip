# -*- coding: UTF-8 -*-

# @Date    : 2020/1/3
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    解题报告：不要求从root出发，但是一定从上往下
    可以在当前点的path中逆向去找是否有等于target的子路径
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
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        result = []
        if not root:
            return result
        self.helper(root, result, [], target)
        return result

    def helper(self, root, result, path, target):
        # 出口
        if not root:
            return

        # 本层开始，看看有没有满足要求的放入result
        path.append(root.val)
        sum = 0
        for i in range(len(path)-1, -1, -1):
            sum += path[i]
            if sum == target:
                result.append(path[i:])

        # 抛出以本层作为base的下一层
        self.helper(root.left, result, path, target)
        self.helper(root.right, result, path, target)

        # 结束本层，回溯
        path.pop()
