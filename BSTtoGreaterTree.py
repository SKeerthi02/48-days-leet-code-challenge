class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.total = 0
        def inorder(node):
            if node:
                inorder(node.right)
                self.total += node.val 
                node.val = self.total 
                inorder(node.left)
        inorder(root)
        return root
