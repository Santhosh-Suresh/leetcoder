# Definition for a binary tree node.
import pandas as pd

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution( object ):

    def bfs(self, root):
        """
        :param root: TreeNode
        :return: ans: Dict
        """
        if root== None:
            return {}
        ans = {root.val: root}
        ans.update(self.bfs(root.left))
        ans.update(self.bfs(root.right))
        return ans


    def bstToGst(self , root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        tree_dict = self.bfs(root)
        keys = pd.DataFrame( data = sorted( tree_dict , reverse = True ) , columns = ["key"] )
        keys["GST_val"] = keys.cumsum()
        keys= keys.set_index["key"]
        for key, node in tree_dict.items():
            node.val = keys.loc[key,"GST_val"]
        return root