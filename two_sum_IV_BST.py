# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        queue = [root]

        while queue:
            curr = queue.pop(0)
            if curr is not None:
                queue.extend([curr.left, curr.right])
                if self.findVal(root, k - curr.val) and (curr.val != k / 2):
                    return True
        else:
            return False

    def findVal(self, root: TreeNode, val: int) -> bool:

        if root.val == val:
            return True
        elif (root.val > val):
            if root.left is not None:
                return self.findVal(root.left, val)
            else:
                return False
        elif root.right is not None:
            return self.findVal(root.right, val)
        else:
            return False

""" A much faster solution that makes use of constant time search in sets"""


class Solution_2:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        contenders = set()

        def find_partner(node):
            if not node:
                return False
            if k - node.val in contenders:
                return True
            contenders.add(node.val)
            return find_partner(node.left) or find_partner(node.right)

        if root.val > k > 0:
            return find_partner(root.left)
        else:
            return find_partner(root)
