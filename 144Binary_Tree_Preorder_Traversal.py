class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = TreeNode(11)
node1 = TreeNode(18)
node2 = TreeNode(21)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(53)
root.left = node1
root.right = node2
node2.right = node3
node2.left = node4
node4.left = node5
class Solution:
    def inorderTraversal(self, root):
        ans = []

        def dfs(root):

            if root is None:
                return

            ans.append(root.val)
            dfs(root.left)


            dfs(root.right)

        dfs(root)

        return ans
print(Solution().inorderTraversal(root))