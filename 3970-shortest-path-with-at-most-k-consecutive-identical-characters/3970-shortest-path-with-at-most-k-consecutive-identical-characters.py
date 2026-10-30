class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        pq = [(0, 0, 1)]
        best = {}
        
        while pq:
            w, u, count = heappop(pq)
            
            if u == n - 1:
                return w
                
            state = (u, count)
            if state in best and best[state] < w:
                continue
            best[state] = w
            
            for v, weight in adj[u]:
                if labels[u] == labels[v]:
                    next_count = count + 1
                else:
                    next_count = 1
                    
                if next_count <= k:
                    next_state = (v, next_count)
                    new_w = w + weight
                    
                    if next_state not in best or new_w < best[next_state]:
                        best[next_state] = new_w
                        heappush(pq, (new_w, v, next_count))
                        
        return -1