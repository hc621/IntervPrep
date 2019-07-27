class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


elements=[1,2,2,3,4,4,3]
root = TreeNode(elements[0])

class Solution:
    def ismirror(self,p,q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        else:
            a = (p.val == q.val)
        return self.ismirror(p.left, q.right) and a and self.ismirror(p.right, q.left)
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None or (root.left == None and root.right == None):
            return True
        return self.ismirror(root.left, root.right)

