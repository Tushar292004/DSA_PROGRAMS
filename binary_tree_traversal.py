class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def preorder_traversal(root):
    if root is None:
        return
    print(root.val, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.val, end=" ")
    inorder_traversal(root.right)

def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.val, end=" ")

def bfs_traversal(root):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

root = Node(8)
root.left = Node(9)
root.right = Node(10)
root.left.left = Node(11)
root.left.right = Node(12)
root.right.left = Node(13)
root.right.right = Node(14)

print("Preorder Traversal: ", end="")
preorder_traversal(root)
print()

print("Inorder Traversal: ", end="")
inorder_traversal(root)
print()

print("Postorder Traversal: ", end="")
postorder_traversal(root)
print()

print("BFS Traversal: ", end="")
bfs_traversal(root)
print()

# OUTPUT 1
# Preorder Traversal: 1 2 4 5 3 6 7 
# Inorder Traversal: 4 2 5 1 6 3 7
# Postorder Traversal: 4 5 2 6 7 3 1
# BFS Traversal: 1 2 3 4 5 6 7

#OUTPUT 2
# Preorder Traversal: 8 9 11 12 10 13 14 
# Inorder Traversal: 11 9 12 8 13 10 14
# Postorder Traversal: 11 12 9 13 14 10 8
# BFS Traversal: 8 9 10 11 12 13 14
