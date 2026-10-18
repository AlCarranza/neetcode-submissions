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

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # Found the node to delete
            if not root.left:   # Case 1 or 2: no left child
                return root.right
            if not root.right:  # Case 2: no right child
                return root.left

            # Case 3: two children -> find in-order succesor
            succ = root.right
            while succ.left:
                succ = succ.left
            # Replace it
            root.val = succ.val # Copy succesor value
            root.right = self.deleteNode(root.right, succ.val) # remove the duplicate

        return root