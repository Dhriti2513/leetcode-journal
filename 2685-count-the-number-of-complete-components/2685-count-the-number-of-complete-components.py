class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n
        complete_components = 0

        for i in range(n):
            if not visited[i]:
                component = []
                stack = [i]
                visited[i] = True
                while stack:
                    u = stack.pop()
                    component.append(u)
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            stack.append(v)
                v_count = len(component)
                is_complete = True
                for node in component:
                    if len(adj[node]) != v_count - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    complete_components += 1
                    
        return complete_components