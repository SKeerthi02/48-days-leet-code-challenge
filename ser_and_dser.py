# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node, answer):
            
            if not node:
                answer.append("None")
            else:
                answer.append(str(node.val))
                dfs(node.left, answer)
                dfs(node.right, answer)
            return answer
                
        return dfs(root, [])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        def dfs(data):
            if data[0] == 'None':
                data.pop(0)
                return None
            root = TreeNode(data[0])
            data.pop(0)
            root.left = dfs(data)
            root.right = dfs(data)
            return root
        node = dfs(data)
        return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
