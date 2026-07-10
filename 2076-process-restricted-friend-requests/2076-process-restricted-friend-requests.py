class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]
        
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_j] = root_i
            
class Solution(object):
    def friendRequests(self, n, restrictions, requests):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :type requests: List[List[int]]
        :rtype: List[bool]
        """
        uf = UnionFind(n)
        result = []
        
        for u, v in requests:
            root_u = uf.find(u)
            root_v = uf.find(v)
            
            # Already in the same friend group
            if root_u == root_v:
                result.append(True)
                continue
                
            # Check if this union violates any restrictions
            isValid = True
            for x, y in restrictions:
                root_x = uf.find(x)
                root_y = uf.find(y)
                
                # If merging u's group and v's group connects x's group and y's group
                if (root_x == root_u and root_y == root_v) or (root_x == root_v and root_y == root_u):
                    isValid = False
                    break
                    
            if isValid:
                uf.union(root_u, root_v)
                result.append(True)
            else:
                result.append(False)
                
        return result