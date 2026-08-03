

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
root=TreeNode(1)
node2=TreeNode(2)
node3=TreeNode(3)
root.left=node2
root.right=node3


class Solution:
    def postorderTraversal(self, root):
        ans = []

        def dfs(root):

            if root is None:
                return

            dfs(root.left)


            dfs(root.right)
            ans.append(root.val)

        dfs(root)

        return ans
        
print(Solution().postorderTraversal(root))