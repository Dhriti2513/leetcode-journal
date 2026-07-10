class Solution(object):
    def isPossible(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        degree = [0] * (n + 1)
        adj_set = set()
        
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            # Store pairs symmetrically to easily check existence
            adj_set.add((min(u, v), max(u, v)))
            
        # Find all nodes with an odd degree
        odds = [i for i in range(1, n + 1) if degree[i] % 2 != 0]
        k = len(odds)
        
        if k == 0:
            return True
            
        if k == 2:
            a, b = odds[0], odds[1]
            # Strategy 1: Connect them directly
            if (min(a, b), max(a, b)) not in adj_set:
                return True
            # Strategy 2: Use a helper node c that is not connected to a or b
            for c in range(1, n + 1):
                if c != a and c != b:
                    if (min(a, c), max(a, c)) not in adj_set and (min(b, c), max(b, c)) not in adj_set:
                        return True
            return False
            
        if k == 4:
            a, b, c, d = odds[0], odds[1], odds[2], odds[3]
            
            # Check pairing 1: (a, b) and (c, d)
            if (min(a, b), max(a, b)) not in adj_set and (min(c, d), max(c, d)) not in adj_set:
                return True
            # Check pairing 2: (a, c) and (b, d)
            if (min(a, c), max(a, c)) not in adj_set and (min(b, d), max(b, d)) not in adj_set:
                return True
            # Check pairing 3: (a, d) and (b, c)
            if (min(a, d), max(a, d)) not in adj_set and (min(b, c), max(b, c)) not in adj_set:
                return True
            return False
            
        return False