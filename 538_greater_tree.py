# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class GreaterTreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        if right == None:
            self.sum = self.val
        else:
            self.sum= self.val + right.sum
        self.left = left
        self.right = right


class Solution( object ):
    def bstToGst(self , root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ans = self.bstToGTN(root)
        return self.gstToBst(ans)

    def gstToBst(self, root):
        """
        :type root: GreaterTreeNode
        :rtype: TreeNode with sum in the place of val
        """
        if root==None:
            return None
        return TreeNode(root.sum,self.gstToBst(root.left), self.gstToBst(root.right))

    def bstToGTN(self, root):
        """
        :type root: TreeNode
        :rtype: GreaterTreeNode
        """
        if root == None:
            return None
        return GreaterTreeNode(root.val, self.bstToGTN(root.left), self.bstToGTN(root.right))

