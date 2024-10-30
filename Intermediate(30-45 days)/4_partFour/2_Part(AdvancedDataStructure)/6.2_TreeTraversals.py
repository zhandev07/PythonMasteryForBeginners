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
                
class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)
    
    # In-Order Traversal
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.value, end=' ')
            self.in_order(node.right)

# Creating a binary search tree and adding elements
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)

# In-order traversal
bst.in_order(bst.root)  # Output: 2 5 7 10 15
