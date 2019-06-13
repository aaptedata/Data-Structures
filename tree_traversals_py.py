# Tree traversal
# also called tree search

# a process of visiting each node exactly once
# in the tree-like data structure
# e.g. for checking or updating a node


# Unlike arrays or linked lists, trees can be traversed in two main ways.
# They can be traversed in breadth-first or depth-first order.

# The breadth-first order is also called level-order.
# There are three common ways to do depth-first traversal:
# - preorder
# - inorder
# - postorder

# The time complexity of the tree traversal algorithm:
# O(n)


# Binary tree node class
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.value}'

# Example tree used for visualization:

#         5
#       /   \
#     3      8
#    / \    /  \
#   1   4  7    9


root = Node(5)
node1 = Node(3)
node2 = Node(1)
node3 = Node(4)
node4 = Node(8)
node5 = Node(7)
node6 = Node(9)

root.left = node1
root.right = node4
node1.left = node2
node1.right = node3
node4.left = node5
node4.right = node6


# Preorder traversal

# 0. if the tree is empty, do nothing
# otherwise:
# 1. check the root
# 2. recursively check the left subtree using preorder traversal
# 3. recursively check the right subtree using preorder traversal

def preorder(node):
    if node == None:
        return
    print(node)
    preorder(node.left)
    preorder(node.right)

# Example tree:

#         5
#       /   \
#     3      8
#    / \    /  \
#   1   4  7    9


# Order of checks of nodes
# 5 3 1 4 8 7 9
print("Preorder traversal:")
preorder(root)
print()


# inorder traversal

# 0. if the tree is empty, do nothing
# otherwise:
# 1. recursively check the left subtree using inorder traversal
# 2. check the root
# 3. recursively check the right subtree using inorder traversal

def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node)
    inorder(node.right)

# Example tree:

#         5
#       /   \
#     3      8
#    / \    /  \
#   1   4  7    9


# Order of checks of nodes
# 1 3 4 5 7 8 9
print("Inorder traversal:")
inorder(root)
print()


# postorder traversal

# 0. if the tree is empty, do nothing
# otherwise:
# 1. recursively check the left subtree using postorder traversal
# 2. recursively check the right subtree using postorder traversal
# 3. check the root

def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node)

# Example tree:

#         5
#       /   \
#     3      8
#    / \    /  \
#   1   4  7    9


# Order of checks of nodes
# 1 4 3 7 9 8 5
print("Postorder traversal:")
postorder(root)
print()
