*this approach is slow due to line 12 everytime pop happens array shifts towards its left. 

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        
        def helper(inleft, inright):
            
            if inleft > inright:
                return None
            
            val = preorder.pop(0)
            node = TreeNode(val)
            index = mapInorder[val]
            node.left = helper(inleft, index-1)
            node.right = helper(index+1, inright)
            
            return node
        
        mapInorder = {value:index for index, value in enumerate(inorder)}
        return helper(0, len(preorder) - 1)
        
   **********************************************************
   
   modification of above approach with adding a variable keeps track of index to iterate over the array
   
   class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        self.counter = 0
        def helper(inleft, inright):
            
            if inleft > inright:
                return None
            
            val = preorder[self.counter]
            self.counter += 1
            node = TreeNode(val)
            index = mapInorder[val]
            node.left = helper(inleft, index-1)
            node.right = helper(index+1, inright)
            
            return node
        
        mapInorder = {value:index for index, value in enumerate(inorder)}
        return helper(0, len(preorder) - 1)
