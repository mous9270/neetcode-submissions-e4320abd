class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges and n == 0:
            return True
        if len(edges) != n - 1:
            return False

        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()

        def dfs(node):
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        dfs(neighbor)
            return len(visited) == n

        return dfs(0)