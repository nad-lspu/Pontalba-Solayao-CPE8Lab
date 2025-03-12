class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#In-0rder

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

#Post Order
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.left.left = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Inorder traversal")
inorder_traversal(root)
print("\nPre-order traversal")
preorder_traversal(root)
print("\nPost-order traversal")
postorder_traversal(root)