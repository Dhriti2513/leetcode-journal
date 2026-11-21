import sys
from typing import List

sys.setrecursionlimit(200000)

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        new_parent = list(parent)
        last_seen = {}
        
        def dfs_find(u: int):
            char = s[u]
            if char in last_seen:
                new_parent[u] = last_seen[char]
                
            prev_ancestor = last_seen.get(char, -1)
            last_seen[char] = u
            
            for v in adj[u]:
                dfs_find(v)
                
            if prev_ancestor == -1:
                del last_seen[char]
            else:
                last_seen[char] = prev_ancestor
                
        dfs_find(0)
        
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        ans = [1] * n
        
        def dfs_size(u: int) -> int:
            total = 1
            for v in new_adj[u]:
                total += dfs_size(v)
            ans[u] = total
            return total
            
        dfs_size(0)
        return ans