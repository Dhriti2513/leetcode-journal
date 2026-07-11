class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))
        visited = [False] * (n + 1)
        min_score = float('inf')
        stack = [1]
        visited[1] = True
        
        while stack:
            u = stack.pop()
            for v, dist in graph[u]:
                min_score = min(min_score, dist)
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
                    
        return min_score