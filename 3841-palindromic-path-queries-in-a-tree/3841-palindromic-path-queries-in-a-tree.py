class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Binary lifting for LCA and Euler tour for subtree range queries
        LOG = 17
        up = [[-1] * LOG for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0
        
        def dfs(u, p, d):
            nonlocal timer
            tin[u] = timer
            timer += 1
            depth[u] = d
            up[u][0] = p
            for i in range(1, LOG):
                if up[u][i - 1] != -1:
                    up[u][i] = up[up[u][i - 1]][i - 1]
            for v in adj[u]:
                if v != p:
                    dfs(v, u, d + 1)
            tout[u] = timer - 1

        dfs(0, 0, 0)
        
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for i in range(LOG - 1, -1, -1):
                if depth[u] - (1 << i) >= depth[v]:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        # Fenwick Tree / Segment Tree implementation for subtree XOR updates
        bit = [0] * (n + 2)
        def update_bit(idx, val):
            idx += 1
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def query_bit(idx):
            idx += 1
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        # Initialize values
        char_masks = [1 << (ord(c) - ord('a')) for c in s]
        for i in range(n):
            update_bit(tin[i], char_masks[i])
            if tout[i] + 1 < n:
                update_bit(tout[i] + 1, char_masks[i])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_c = parts[2]
                new_mask = 1 << (ord(new_c) - ord('a'))
                diff = char_masks[u] ^ new_mask
                if diff:
                    char_masks[u] = new_mask
                    update_bit(tin[u], diff)
                    update_bit(tout[u] + 1, diff)
            else:
                u, v = int(parts[1]), int(parts[2])
                lca = get_lca(u, v)
                # Path mask = prefix(u) ^ prefix(v) ^ LCA_val
                mask_u = query_bit(tin[u])
                mask_v = query_bit(tin[v])
                lca_val = char_masks[lca]
                
                path_mask = mask_u ^ mask_v ^ lca_val
                # Check if path_mask has at most one bit set
                is_palindrome = (path_mask & (path_mask - 1)) == 0
                ans.append(is_palindrome)
                
        return ans