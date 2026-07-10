class Solution(object):
    def maximalPathQuality(self, values, edges, maxTime):
        """
        :type values: List[int]
        :type edges: List[List[int]]
        :type maxTime: int
        :rtype: int
        """
        n = len(values)
        adj = [[] for _ in range(n)]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))
            
        # Track number of times we visit a node to know if it's the first visit
        visited_count = [0] * n
        self.max_quality = 0
        
        def dfs(u, curr_time, curr_quality):
            # If this is the first time visiting this node, add its value
            if visited_count[u] == 0:
                curr_quality += values[u]
            
            visited_count[u] += 1
            
            # If back at node 0, update max_quality
            if u == 0:
                self.max_quality = max(self.max_quality, curr_quality)
            
            # Explore neighbors
            for v, t in adj[u]:
                if curr_time + t <= maxTime:
                    dfs(v, curr_time + t, curr_quality)
            
            # Backtrack
            visited_count[u] -= 1
            
        dfs(0, 0, 0)
        return self.max_quality