class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        
        def dfs(node):
            if node:
                dfs(node.left)
                self.answer = min(self.answer, node.val - self.previous)
                print(self.answer)
                self.previous = node.val
                dfs(node.right)
        
        
        self.previous = float('-inf')
        self.answer = float('inf')
        dfs(root)
        return self.answer
