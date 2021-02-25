#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution( object ):
    def getTargetCopy(self , original , cloned , target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        self.dfs(cloned, target)

    def dfs(self, tree, val):
        if tree is None:
            return None
        if tree.val == val:
            return tree
        left_search= self.dfs(tree.left, val)
        if left_search:
            return left_search
        else:
            right_search= self.dfs(tree.right, val)
            if (right_search):
                return right_search
            else:
                return None
    def bfs(self, tree, val):
        queue = [tree]
        while queue:
            next = queue.pop(0)
            if next is None:
                continue
            if next.val == val:
                return next
            else:
                queue.extend([next.left, next.right])
            print([item.val if item else item for item in queue] )