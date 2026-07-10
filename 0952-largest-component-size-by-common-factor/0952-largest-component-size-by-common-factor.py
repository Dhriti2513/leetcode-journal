class UnionFind(object):
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]

class Solution(object):
    def largestComponentSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = max(nums)
        uf = UnionFind(max_val + 1)
        
        # Map each number to its prime factors
        for num in nums:
            d = 2
            val = num
            while d * d <= val:
                if val % d == 0:
                    uf.union(num, d)
                    while val % d == 0:
                        val //= d
                d += 1
            if val > 1:
                uf.union(num, val)
                
        # Count the size of each component based on the elements present in nums
        count = {}
        max_component = 0
        for num in nums:
            root = uf.find(num)
            count[root] = count.get(root, 0) + 1
            if count[root] > max_component:
                max_component = count[root]
                
        return max_component