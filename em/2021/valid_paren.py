class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        left_ht = self.get_depth(root.left)
        right_ht = self.get_depth(root.right)
        diff = abs(left_ht - right_ht)
        return diff <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_depth(self, root):
        if not root:
            return 0
        return 1 + max(self.get_depth(root.left), self.get_depth(root.right))
