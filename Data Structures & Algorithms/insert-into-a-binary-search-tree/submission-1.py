# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val=val)
        def insert(node):
            if not node:
                return
            elif node.left is None and val < node.val:
                node.left = TreeNode(val=val)
                return
            elif node.right is None and val > node.val:
                node.right = TreeNode(val=val)
            elif val < node.val:
                insert(node.left)
            else:
                insert(node.right)


        insert(root)
        return root