# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Step 1: Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found! Step 2: Delete the node based on its structure
            
            # Case 1 & 2: Node has 0 or 1 child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # Case 3: Node has 2 children
            # Find the inorder successor (smallest node in the right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left
                
            # Copy the successor's value to the current node
            root.val = successor.val
            
            # Recursively delete the successor node from the right subtree
            root.right = self.deleteNode(root.right, successor.val)
            
        return root