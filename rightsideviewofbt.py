BFS + deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        answer = []
        
        if not root:
            return answer
        
        nextLevel = deque([root,])
        while nextLevel:
            
            currentLevel = nextLevel
            nextLevel = deque()
            
            while currentLevel:
                node = currentLevel.popleft()
                
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            answer.append(node.val)
        return answer
  ****************************  ****************************
  
  DFS, Recursion
  
  class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        answer = []
        
        if not root:
            return answer
        def dfs(root, level):
            if level == len(answer):
                answer.append(root.val)
            for child in [root.right, root.left]:   # this is how we can check if a node has children if yes proceede
                if child:
                    dfs(child, level+1)
            
        
        dfs(root, 0)
        return answer
