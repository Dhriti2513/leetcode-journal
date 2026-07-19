class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        # Allocate memory for the segment tree (2 * n elements)
        self.tree = [0] * (2 * self.n)
        
        # Populate the leaves of the tree with original array elements
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
            
        # Build the tree upwards by computing parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        # Move to the corresponding leaf node
        pos = index + self.n
        self.tree[pos] = val
        
        # Propagate the changes upwards up to the root node
        while pos > 1:
            # Parent node index is pos // 2 (or pos >> 1)
            # The two children are always pos and pos ^ 1
            self.tree[pos >> 1] = self.tree[pos] + self.tree[pos ^ 1]
            pos >>= 1

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        # Transform bounds to tree array bounds (exclusive right boundary)
        l = left + self.n
        r = right + self.n + 1
        
        while l < r:
            # If the left bound is odd, it is a right child of its parent.
            # Include it in the sum and move to the right element.
            if l & 1:
                res += self.tree[l]
                l += 1
            # If the right bound is odd, the element before it is a left child.
            # Include it in the sum.
            if r & 1:
                r -= 1
                res += self.tree[r]
            
            # Move both pointers up to their respective parents
            l >>= 1
            r >>= 1
            
        return res