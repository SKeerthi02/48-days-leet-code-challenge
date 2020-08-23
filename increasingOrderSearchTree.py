class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        answer = []
        self.temp = inord = TreeNode
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.temp.right = node
                self.temp = self.temp.right
                inorder(node.right)
        inorder(root)
        
        return inord.right
