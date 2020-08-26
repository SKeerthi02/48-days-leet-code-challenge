class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        
        def dfs(inleft, inright):
            
            if inleft > inright:
                return None
            
            val = postorder.pop()
            node = TreeNode(val)
            index = inorderIndexMap[val]
            
            node.right = dfs(index+1, inright)
            node.left = dfs(inleft, index-1)
 
            
            return node
        inorderIndexMap = {value:index for index, value in enumerate(inorder)}
        return dfs(0, len(inorder)-1)
