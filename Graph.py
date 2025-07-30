

# que no 01

#Find the Town Judge

class Solution:
    def findJudge(self, n, trust):
        trust_scores = [0] * (n + 1)

        for a, b in trust:
            trust_scores[a] -= 1
            trust_scores[b] += 1

        for i in range(1, n + 1):
            if trust_scores[i] == n - 1:
                return i

        return -1


#Que no 02
# 
#Find Center of Star Graph
         
class Solution:
    def findCenter(self, edges):
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        return edges[0][1]


# Que no 03

#Find if Path Exists in Graph


class Solution:
    def validPath(self, n, edges, source, destination):
        from collections import defaultdict, deque

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        queue = deque([source])

        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return False



# Que no 04

#Minimum Height Trees


class Solution:
    def findMinHeightTrees(self, n, edges):
        from collections import defaultdict, deque

        if n == 1:
            return [0]

    
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        
        leaves = [node for node in graph if len(graph[node]) == 1]

        
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return leaves



# Que no 05

#Validate Binary Tree Nodes

class Solution:
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        parent = [0] * n
        
        for i in range(n):
            for child in (leftChild[i], rightChild[i]):
                if child != -1:
                    if parent[child] or child == i:
                        return False
                    parent[child] = 1

        root = -1
        for i in range(n):
            if parent[i] == 0:
                if root == -1:
                    root = i
                else:
                    return False

        visited = set()
        def dfs(node):
            if node == -1 or node in visited:
                return
            visited.add(node)
            dfs(leftChild[node])
            dfs(rightChild[node])

        dfs(root)
        return len(visited) == n
