# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        leftHeight = self.findHeight(root.left)
        rightHeight = self.findHeight(root.right)

        if rightHeight + 1 == leftHeight or rightHeight == leftHeight or rightHeight - 1 == leftHeight:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    def findHeight(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0
        
        return 1 + max(self.findHeight(root.left), self.findHeight(root.right))