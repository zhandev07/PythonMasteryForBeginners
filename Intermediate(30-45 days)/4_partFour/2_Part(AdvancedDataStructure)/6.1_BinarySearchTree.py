class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(value, node.right)