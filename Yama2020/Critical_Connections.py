# -*- coding: UTF-8 -*-

# @Date    : 2020/3/1
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""

"""


class Solution1:
    def FindCriticalConnection(self, numNodes, edges):
        # Get all the nodes
        nodes = [i + 1 for i in range(numNodes)]

        # Get all the neighbours
        neighbours = {node: [] for node in nodes}
        for i in range(len(edges)):
            neighbours[edges[i][0]].append(edges[i][1])
            neighbours[edges[i][1]].append(edges[i][0])

        # Closure: DFS
        def dfs(parent, seen):
            nonlocal neighbours

            # Child
            neigh = neighbours[parent]

            # Loop over all the possible child
            for node in neigh:
                # Return if we've seen the parent
                if seen[node] == 1:
                    continue

                # Mark this node is visited
                seen[node] = 1

                # DFS
                dfs(node, seen)

        # Loop over all the possible edges
        output = []
        for edge in edges:
            explored = {node: 0 for node in nodes}

            # Delete the nodes in the neighbour
            neighbours[edge[0]].remove(edge[1])
            neighbours[edge[1]].remove(edge[0])

            # DFS
            explored[nodes[0]] = 1
            dfs(nodes[0], explored)

            # Check if we could visit all the nodes
            if sum(explored.values()) < numNodes:
                output.append(edge)

            # Add back the edge
            neighbours[edge[0]].append(edge[1])
            neighbours[edge[1]].append(edge[0])

            # print(nodes)
        # print(neighbours)
        # print(output)
        return output


class Solution2:
    def FindCriticalConnection(self, numNodes, edges):
        nodes = [i + 1 for i in range(numNodes)]

        # Get all the neighbours
        neighbours = {node: [] for node in nodes}
        for i in range(len(edges)):
            neighbours[edges[i][0]].append(edges[i][1])
            neighbours[edges[i][1]].append(edges[i][0])

        times = [-1]*(numNodes+1)
        low = [-1]*(numNodes+1)

        res = []
        curTime = -1

        for i in nodes:
            if times[i] != -1:
                continue
            self.dfs(neighbours, times, curTime, low, -1, i, res)

        return res

    def dfs(self, adj, times, prevTime, low, parent, cur, res):
        prevTime += 1
        times[cur] = low[cur] = prevTime
        for nei in adj[cur]:
            if nei == parent:
                continue
            if times[nei] == -1:
                self.dfs(adj, times, prevTime, low, cur, nei, res)
            if low[nei] > times[cur]:
                res.append([cur, nei])
            low[cur] = min(low[nei], low[cur])


if __name__ == "__main__":
    # Case 1
    numNodes = 5
    edges = [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]
    a = Solution1()
    b = Solution2()
    print(a.FindCriticalConnection(numNodes, edges))
    print(b.FindCriticalConnection(numNodes, edges))

    # Case 2
    numNodes = 6
    edges = [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]]
    print(a.FindCriticalConnection(numNodes, edges))
    print(b.FindCriticalConnection(numNodes, edges))

    # Case 3
    numNodes = 9
    edges = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]
    print(a.FindCriticalConnection(numNodes, edges))
    print(b.FindCriticalConnection(numNodes, edges))