class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.total = 0
        
        def helper(node):
            if not node:
                return 0
            if node:
                left = helper(node.left)
                right = helper(node.right)
                self.total += abs(left - right)
                return left + right + node.val 
            
        helper(root)
        return self.total 
