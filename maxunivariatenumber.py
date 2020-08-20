class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.answer = 0 
        
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            left_path = right_path = 0
            if node.left and node.left.val == node.val:
                left_path = left + 1
            if node.right and node.right.val == node.val:
                right_path = right + 1
            
            self.answer = max(self.answer, left_path + right_path)
            
            return max(left_path, right_path)
        
        helper(root)
        return self.answer 
