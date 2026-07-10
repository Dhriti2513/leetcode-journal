class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        has_incoming = [False] * n
        
        for _, to_node in edges:
            has_incoming[to_node] = True
            
        # Collect all nodes that have NO incoming edges
        return [i for i in range(n) if not has_incoming[i]]