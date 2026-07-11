class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        red_adj = defaultdict(list)
        blue_adj = defaultdict(list)
        for u, v in redEdges: red_adj[u].append(v)
        for u, v in blueEdges: blue_adj[u].append(v)
        res = [-1] * n
        queue = deque([(0, -1, 0)])
        visited = set([(0, -1)])
        
        while queue:
            node, last_color, dist = queue.popleft()
            if res[node] == -1:
                res[node] = dist
            else:
                res[node] = min(res[node], dist)
            if last_color != 0:
                for neighbor in red_adj[node]:
                    if (neighbor, 0) not in visited:
                        visited.add((neighbor, 0))
                        queue.append((neighbor, 0, dist + 1))
            if last_color != 1:
                for neighbor in blue_adj[node]:
                    if (neighbor, 1) not in visited:
                        visited.add((neighbor, 1))
                        queue.append((neighbor, 1, dist + 1))
                        
        return res