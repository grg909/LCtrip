# LCtrip in :snake:
  Code OJ note in python3 - - We care about coding style here ! 白板编程面试模板代码，保证Coding Style前提下，最短最高效

# 前言
- 题目来源包括： LeetCode、LintCode、Cracking the coding interview、ACM challenge workbook(挑战程序设计竞赛)
- 本项目的target是白板编程时可以清晰简练的手写代码，好的coding style函数名，变量名自解释，而不用大量注释。同时在保证写法最佳情况下，最求代码量最短
- 项目持续更新中，优先使用 python3，如果您有coding style更有利于面试的写法希望分享的话欢迎联系更新~  
- 如果您对当前解析有任何疑问，咱们 issue 见~

# :trophy: 里程碑
- 🧬 数据结构
	- [🐤 Binary Tree](#-binary-tree)

# 题库解析
此专栏保证Coding Style前提下，最短最高效

### 🐤 Binary Tree
- 碰到二叉树的问题，就想想整棵树在该问题上的结果和左右儿子在该问题上的结果之间的联系是什么
- Dfs用递归实现分为 Divide Conquer 和 Traverse, Divide Conquer更为简单直接，90%问题可解决

#### 94.Binary Tree inorder traversal
```python
class Solution:

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
```