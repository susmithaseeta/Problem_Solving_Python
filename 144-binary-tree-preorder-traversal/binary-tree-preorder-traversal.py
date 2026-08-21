# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root,res):
        if root == None:
            return
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

    def preorderTraversal(self, root):
        res = []
        self.preorder(root, res)
        return res