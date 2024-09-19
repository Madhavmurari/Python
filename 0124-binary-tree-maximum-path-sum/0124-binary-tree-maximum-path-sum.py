# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]

        def DFS(root):
            if not root:
                return 0
            # Recursive calculation for left and right subtrees
            # Ensure that negative values are not considered (max(DFS(...), 0))
            leftMax=max(0,DFS(root.left))
            rightMax=max(0,DFS(root.right))


            # Compute max Path sum with Split
            res[0]=max(res[0],root.val+leftMax + rightMax)

            # Return the maximum path sum that starts from the current node
            return root.val + max(leftMax,rightMax)            

        DFS(root)

        return res[0]





       