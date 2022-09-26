class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def isSameTree(p, q):
    # if both the current node value are null, then they are the same ==> return true
    if not p and not q:
        return True
    # if not both of them are null, but one of them is null
    elif not p or not q:
        return False
    # Neither values are null, so check if the two value are the same
    # If they are not, return false, if they are, then proceed to the next recursive call
    elif p.val != q.val:
        return False

    # Reursive call
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    root1 = TreeNode(12)
    root1.left = TreeNode(7)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(9)
    root1.right.left = TreeNode(10)
    root1.right.right = TreeNode(5)
    print(isSameTree(root, root1))


main()

