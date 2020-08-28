# LCtrip in :snake:
  Code OJ note in python3 - - We care about coding style here ! 白板编程面试模板代码，保证Coding Style前提下，最短最高效

# 前言
- 题目来源包括： LeetCode、LintCode、Cracking the coding interview、ACM challenge workbook(挑战程序设计竞赛)
- 本项目的target是白板编程时可以清晰简练的手写代码，好的coding style函数名，变量名自解释，而不用大量注释。同时在保证写法最佳情况下，最求代码量最短
- 项目持续更新中，使用python3实现，如果您有更符合要求的写法，欢迎提交更新~  
- 如果您对当前解析有任何疑问，咱们 issue 见~

# :trophy: 里程碑
- 🧬 版图
    - [🐈 Sort Algorithm](#-sort-algorithm)
	- [🐤 Breadth First Search](#-breadth-first-search)
	- [🐈 Linked List](#-linked-list)
	- [🐑 Binary Tree](#-binary-tree)
	- [🦌 Binary Search](#-binary-search)
	- [🦎 Two Pointer](#-two-pointer)
	- [🐄 Deep First Search](#-dfs)
    - [🦉 Dynamic Programming](#-bfs)

# 题库解析
此专栏保证Coding Style前提下，最短最高效。

### 🐈 Sort Algorithm
```python
class Solution:
    # @param {int[]} A an integer array
    # @return None

    # 冒泡排序, Best O(n), Average O(n^2), Worst O(n^2)
    def bubbleSort(self, A):
        for last in range(len(A) - 1, 0, -1):
            for i in range(last):
                if A[i] > A[i + 1]:
                    A[i], A[i + 1] = A[i + 1], A[i]

    # 选择排序, Best O(n^2), Average O(n^2), Worst O(n^2)
    def selectionSort(self, A):
        for i in range(len(A)):
            minIdx = i
            for j in range(i + 1, len(A)):
                if A[j] < A[minIdx]:
                    minIdx = j
            A[i], A[minIdx] = A[minIdx], A[i]

    # 插入排序, Best O(n), Average O(n^2), Worst O(n^2) 用于近似有序的最佳
    def insertionSort(self, A):
        for i in range(1, len(A)):
            curIdx, tmp = i, A[i]
            while curIdx > 0 and A[curIdx - 1] > tmp:
                A[curIdx] = A[curIdx - 1]
                curIdx -= 1
            A[curIdx] = tmp

    # 快速排序, Best O(nlogn), Average O(nlogn), Worst O(n^2)
    def quickSort(self, A):
        self.qHelper(A, 0, len(A) - 1)

    def qHelper(self, A, start, end):
        if start >= end:
            return

        left, right = start, end
        pivot = A[(start + end) // 2]

        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        self.qHelper(A, start, right)
        self.qHelper(A, left, end)

    # 归并排序, Best O(nlogn), Average O(nlogn), Worst O(nlogn), 不太好因为需要额外空间O（n)
    def mergeSort(self, A):
        self.mHelper(A, 0, len(A) - 1, [0] * len(A))

    def mHelper(self, A, start, end, tmp):
        if start >= end:
            return

        mid = (start + end) // 2
        self.mHelper(A, start, mid, tmp)
        self.mHelper(A, mid + 1, end, tmp)
        self.mergeTwo(A, start, end, tmp)

    def mergeTwo(self, A, start, end, tmp):
        mid = (start + end) // 2
        leftIdx = start
        rightIdx = mid + 1
        idx = start

        while leftIdx <= mid and rightIdx <= end:
            if A[leftIdx] < A[rightIdx]:
                tmp[idx] = A[leftIdx]
                leftIdx += 1
            else:
                tmp[idx] = A[rightIdx]
                rightIdx += 1
            idx += 1

        while leftIdx <= mid:
            tmp[idx] = A[leftIdx]
            leftIdx, idx = leftIdx + 1, idx + 1
        while rightIdx <= end:
            tmp[idx] = A[rightIdx]
            rightIdx, idx = rightIdx + 1, idx + 1

        for i in range(start, end + 1):
            A[i] = tmp[i]
```

### 🐤 Breadth First Search
- BFS写法简单清晰，以下是使用场景
- 图的遍历 Traversal in Graph
    - 层级遍历 Level Order Traversal
    - 由点及面 Connected Component
    - 拓扑排序 Topological Sorting
- 最短路径 Shortest Path in Simple Graph
    - 仅限简单图求最短路径
    - 即，图中每条边长度都是1，且没有方向
- 能够用 BFS 解决的问题，一定不要用 DFS 去做！

#### LintCode 618.Search graph nodes
- Bfs分层和不分层
```python
from collections import deque

class Solution:
    def searchNode(self, graph: List[Node], values: dict, node:'Node', target:int)->'Node':
        q = deque([node])
        seen = set()
        seen.add(node)

        while q:
            head = q.popleft()
            if values[head] == target:
                return head

            for nei in head.neighbors:
                if nei not in seen:
                    q.append(nei)
                    seen.add(nei)

        return None

# Follow up: 如何找到所有最近的value=target的点: BFS分层
class Solution:
    def searchNode(self, graph: List[Node], values: dict, node:'Node', target:int)->List[Node]:
        q = deque([node])
        seen = set()
        seen.add(node)
        res = []

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if values[node] == target:
                    res.append(node)
                    for nei in node.neighbors:
                        if nei not in seen:
                            q.append(nei)
                            seen.add(nei)
            if res:
                return res

        return None
```

#### LintCode 137.Clone Graph
1. node -> nodes, bfs找出所有点
2. copy nodes, 建立新老节点的mapping关系
3. copy edges, 遍历老节点，根据老节点的关联关系来连接新节点
```python
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        root = node
        if node is None:
            return node

        # use bfs to traverse the graph and get all old nodes
        nodes = self.getNodes(node)

        # copy nodes, create a mapping dict from old->new
        mapping = {}
        for node in nodes:
            mapping[node] = Node(node.val, [])

        # copy edges
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]

    def getNodes(self, node: 'Node') -> 'set':
        results = set([node])
        q = deque([node])
        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in results:
                    results.add(neighbor)
                    q.append(neighbor)

        return results
```

#### LintCode 615.Course Schedule
1. no graph presentation: so build graph first
2. count and get the indegree of nodes
3. BFS topological sorting, start from the node with 0 indegree
4. if the graph can be topological sort, then return true
```python
from collections import deque

class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        graph = self.build_graph(numCourses, prerequisites)
        indegree = self.get_degree(numCourses, prerequisites)

        start_nodes = [n for n in graph.keys() if indegree[n] == 0]
        count = 0
        q = deque(start_nodes)

        while q:
            node = q.popleft()
            count += 1
            for edge in graph[node]:
                indegree[edge] -= 1
                if indegree[edge] == 0:
                    q.append(edge)

        return count == numCourses

    def build_graph(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}

        for edge in prerequisites:
            graph[int(edge[1])].append(edge[0])

        return graph

    def get_degree(self, numCourses, prerequisites):
        indegree = [0] * numCourses

        for edge in prerequisites:
            indegree[int(edge[0])] += 1

        return indegree
```

### 🐈 Linked List
- 熟悉基本操作，把复杂问题拆解为基本操作的组合
- 两个技巧：Dummy head 和 Two pointer (快慢指针)

#### LintCode 450.Reverse Nodes in k-Group
- 拆解为链表基本操作
- 可以在函数注释处写上链表的变化，避免出错
```python
class Solution:
    def reverseKGroup(self, head, k):
        """
        # dummy->[1->2->3]->[4->5->6]->7 (k = 3)
        # dummy->[3->2->1]->[6->5->4]->7
        """
        dummy = ListNode(-1)
        dummy.next = head

        pre = dummy
        while pre:
            pre = self.reverse_next_k_node(pre, k)

        return dummy.next

    def reverse_next_k_node(self, pre, k):
        """
        原：pre -> n1 -> n2 -> ... -> nk -> nk+1
        现：pre -> nk -> nk-1 -> ... -> n1 -> nk+1
        return n1
        """
        n1 = pre.next
        nk = self.find_kth_node(pre, k)
        if not nk:
            return None
        nk_plus = nk.next

        nk.next = None
        self.reverse(n1)
        pre.next = nk
        n1.next = nk_plus

        return n1

    def find_kth_node(self, pre, k):
        # pre -> n1 -> n2 -> ... -> nk
        cur = pre
        while k:
            cur = cur.next
            if not cur:
                return None
            k -= 1
        return cur

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
```

### 🐑 Binary Tree
- 碰到二叉树的问题，就想想整棵树在该问题上的结果和左右儿子在该问题上的结果之间的联系是什么
- DFS用递归实现分为 Divide Conquer 和 Traverse, Divide Conquer更为简单直接，90%二叉树问题可解决

#### 94.Binary Tree inorder traversal
```python
# Non-recursion
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

#### 145.Binary Tree Postorder traversal
```python
from collections import deque

# Use deque, non-recursion
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = deque([])

        cur = root
        stack = []
        while stack or cur:
            if cur:
                stack.append(cur)
                res.appendleft(cur.val)  # reverse process of preorder
                cur = cur.right          # reverse process of preorder
            else:
                node = stack.pop()
                cur = node.left          # reverse process of preorder
        return res
```

#### LintCode 578.Lowest Common Ancestor III
- 这题要注意A和B不一定都在子树里。return多个值来记录A和B是否在子树里存在，以及LCA node。分治法。最后递归结束以后，需要判断是否A和B都存在。
1. 如果A或B在root上，那么LCA就在root上。
2. 如果左子树和右子树都有LCA，那么也说明当前LCA在root上。
3. 如果只有左边有LCA，那么LCA就在左边。
4. 如果只有右边有LCA，那么LCA就在右边。
```python
class Solution:
    def lowestCommonAncestor3(self, root, A, B):
        a, b, lca = self.helper(root, A, B)
        if a and b:
            return lca
        else:
            return None

    def helper(self, root, A, B):
        if not root:
            return False, False, None

        left_a, left_b, left_node = self.helper(root.left, A, B)
        right_a, right_b, right_node = self.helper(root.right, A, B)

        a = left_a or right_a or root == A
        b = left_b or right_b or root == B

        if root == A or root == B:
            return a, b, root

        if left_node and right_node:
            return a, b, root
        if left_node:
            return a, b, left_node
        if right_node:
            return a, b, right_node

        return a, b, None
```

#### LintCode 614.Binary Tree Longest Consecutive Sequence II 
- 分治法。返回多个值来记录从某一个点往下走的时候递增的最大路径和递减的最大路径，以及一个全局的最长路径。在某一点，全局的最长路径就是这三者的最大值:
1. 左子树中遇到的最长路径
2. 右子树中遇到的最长路径
3. 通过当前点的最长路径

```python
class Solution:
    def longestConsecutive2(self, root):
        max_len, _, _ = self.helper(root)
        return max_len

    def helper(self, root):
        if not root:
            return 0, 0, 0

        left_len, left_down, left_up = self.helper(root.left)
        right_len, right_down, right_up = self.helper(root.right)

        down, up = 0, 0
        if root.left and root.left.val + 1 == root.val:
            down = left_down + 1
        if root.left and root.left.val - 1 == root.val:
            up = left_up + 1
        if root.right and root.right.val + 1 == root.val:
            down = max(down, right_down + 1)
        if root.right and root.right.val - 1 == root.val:
            up = max(up, right_up + 1)

        len = down + 1 + up
        len = max(len, left_len, right_len)

        return len, down, up
```

#### LintCode 246.Binary Tree Path Sum II
- 题目要求不一定从root出发，但是一定要从上往下。我们还是从root出发往下traverse。并且维护一边往下走一边把遍历到的点的值放进一个list里。
- 在当前点，我们做一件事：把当前的list从后往前加，看能不能加到target。如果加到target，说明有一个解。我们把这个解放进result里。全部check完毕以后，我们可以继续往下走了。最后全部traverse结束，我们返回答案的List。
- 此题是标准的dfs回溯实现模板
```python
class Solution:
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
```

#### LintCode 95.Validate Binary Search Tree
- 以下几道是BST典型题
```python
# Divide and Conquer
class Solution1:
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
class Solution2:
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
```

#### LintCode 448.Inorder Successor in BST
```python
# 结合BST的特点
class Solution1:
    def inorderSuccessor(self, root, p):
        if not root:
            return None

        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)

        left = self.inorderSuccessor(root.left, p)
        if left:
            return left
        else:
            return root

# stack迭代，套用中序模板
class Solution2:
    def inorderSuccessor(self, root, p):
        stack = []
        cur = root
        flag = False

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if flag:
                    return cur
                if cur == p:
                    flag = True
                cur = cur.right
        return None
```

#### LintCode 87.Remove Node in Binary Search Tree
```python
# 重点是build新BST的方法
class Solution:
    ans = []

    def removeNode(self, root, value):
        self.inorder(root, value)
        return self.build(0, len(self.ans) - 1)

    def inorder(self, root, value):
        if not root:
            return

        self.inorder(root.left, value)
        if root.val != value:
            self.ans.append(root.val)
        self.inorder(root.right, value)

    def build(self, left, right):
        if left == right:
            node = TreeNode(self.ans[left])
            return node

        if left > right:
            return None

        mid = (left + right) // 2
        node = TreeNode(self.ans[mid])
        node.left = self.build(left, mid - 1)
        node.right = self.build(mid + 1, right)
        return node
```

### 🦌 Binary Search
- 二分查找是很多其他算法的基础，比如快搜
- 二分法基本功
    - 时间复杂度小练习
    - 递归与非递归的权衡
    - 二分的三大痛点
    - 通用的二分法模板
- 第一境界：二分位置 之 圈圈叉叉 Binary Search on Index - OOXX
    - 找到满足某个条件的第一个位置或者最后一个位置
- 第二境界：二分位置 之 保留一半 Binary Search on Index - Half half
    - 保留有解的一半，或者去掉无解的一半
- 第三境界：二分答案 Binary Search on Result
    - 压根看不出是个二分法！
- 根据要求的时间复杂度倒推求解算法

#### 34. Find First and Last Position of Element in Sorted Array
- 二分法找第一次出现和最后一次出现
```python
# 二次无脑二分模板first and last， Todo：可有更好的coding style
class Solution1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        res = [-1, -1]
        if not nums:
            return res
        
        # find first appear
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            res[0] = start
        elif nums[end] == target:
            res[0] = end
        
        # find last appear
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                start = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            res[1] = start
        elif nums[start] == target:
            res[1] = end

        return res

# 更机智的方法，只用一种binery search，用python自带的bisect可
import bisect

class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first = bisect.bisect_left(nums, target)
        last = bisect.bisect_left(nums, target + 1)

        # the indices will be equal only if the target is not in the list
        if first == last:
            return [-1, -1]

        # last是最后一个目标值的下一个位置
        return [first, last - 1]
```

### 🦎 Two Pointer
- 灵活运用quick sort和quick select中的partition过程
- 对于求 2 个变量如何组合的问题，可以循环其中一个变量，然后研究另外一个变量如何变化
- 双指针问题也可以考虑hash解，看哪个更符合要求。双指针有同向（一般O(n^2))和异向(一般O(n))。
- Two sum若干变种，要熟练

#### 215.Kth largest element in an array
- Quick select的标准实现
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        # 举个例子就能发现，kth小和kth大互相转换是len(nums)-k
        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)

    def quickSelect(self, nums, start, end, k):
        """
        During the process, it's guaranteed start <= k <= end
        """
        if start == end:
            return nums[start]

        left, right = start, end
        pivot = nums[(start + end) // 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if k <= right:
            return self.quickSelect(nums, start, right, k)
        if k >= left:
            return self.quickSelect(nums, left, end, k)

        # right < k < left:
        return nums[k]
```

#### LintCode 463.Sort integers
- Quick sort的标准实现
```python
class Solution:
    def sortColors(self, nums):
        if not nums:
            return

        self.quickSort(nums, 0, len(nums) - 1)

    def quickSort(self, nums, start, end):
        if start >= end:
            return

        left, right = start, end
        # 1. pivot, nums[start], nums[end]
        # get value not index
        pivot = nums[(start + end) // 2]

        # 2. left <= right not <
        while left <= right:  
            while left <= right and nums[left] < pivot: # not <=
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.quickSort(nums, start, right)
        self.quickSort(nums, left, end)
```

#### 15.3Sum
- K sum问题的标准解法，很好的coding style
```python
class Solution:
    def threeSum(self, nums):
        if not nums or len(nums) < 3:
            return []

        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.find_two_sum(nums, i + 1, len(nums) - 1, -nums[i], result)

    def find_two_sum(self, nums, left, right, target, result):
        value = nums[left] + nums[right]
        while left < right:
            if value == target:
                result.append([-target, nums[left], nums[right]])
                right -= 1
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif value > target:
                right -= 1
            else:
                left += 1
```
