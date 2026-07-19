# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        
        def dfs(node):
            if not node:
                return 0
            
            # Recursively calculate the univalue path lengths for children
            left_len = dfs(node.left)
            right_len = dfs(node.right)
            
            left_arrow = 0
            right_arrow = 0
            
            # Check if left child matches current node's value
            if node.left and node.left.val == node.val:
                left_arrow = left_len + 1
                
            # Check if right child matches current node's value
            if node.right and node.right.val == node.val:
                right_arrow = right_len + 1
            
            # Update the global maximum path length with the combined path through this node
            self.longest = max(self.longest, left_arrow + right_arrow)
            
            # Return the longest single-direction path to the parent node
            return max(left_arrow, right_arrow)
            
        dfs(root)
        return self.longest