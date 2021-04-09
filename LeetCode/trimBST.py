# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        ans = TreeNode()
        if root is None:
            return None
        if low <= root.val <= high:
            ans.val = root.val
            ans.left = self.trimBST(root.left, low, high)
            ans.right = self.trimBST(root.right, low, high)
        elif root.val < low:
            ans = self.trimBST(root.right, low, high)
        else:
            ans = self.trimBST(root.left, low, high)

        return ans