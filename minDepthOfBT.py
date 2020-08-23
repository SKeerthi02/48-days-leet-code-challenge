class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        else:
            node_q = deque([(1, root), ])
        while node_q:
            depth, root = node_q.popleft()
            
            children = [root.left, root.right]
            if not any(children):
                return depth
            
            for c in children:
                if c:
                    node_q.append((depth+1, c))
            
