from .node import Node


def create_tree(value):
    return Node(value)


def add_node_by_path(root, path, value):
    """
    Add a node using a path string.
    Example:
        L  -> left child
        R  -> right child
        LL -> left of left
    """

    current = root

    for direction in path[:-1]:

        if direction == "L":
            if current.left is None:
                current.left = Node(None)
            current = current.left

        elif direction == "R":
            if current.right is None:
                current.right = Node(None)
            current = current.right

        else:
            raise ValueError("Path must contain only L or R")

    # place the new node
    if path[-1] == "L":
        current.left = Node(value)
    else:
        current.right = Node(value)


def print_tree(root, level=0, prefix="Root: "):
    """
    Pretty prints the binary tree.
    """

    if root is None:
        return

    print(" " * (level * 4) + prefix + str(root.value))

    print_tree(root.left, level + 1, "L--- ")
    print_tree(root.right, level + 1, "R--- ")


def edit_node(root, path, new_value):
    """
    Edit the value of a node using path.
    Example path: LL, LR, R
    """

    current = root

    for direction in path:
        if direction == "L":
            current = current.left
        elif direction == "R":
            current = current.right

        if current is None:
            raise ValueError("Node does not exist")

    current.value = new_value



def delete_node(root, path):
    """
    Delete a node using path.
    If path is empty -> delete entire tree.
    """

    if path == "":
        return None

    current = root

    for direction in path[:-1]:

        if direction == "L":
            current = current.left
        else:
            current = current.right

        if current is None:
            return root

    if path[-1] == "L":
        current.left = None
    else:
        current.right = None

    return root



def inorder(root):
    """
    Left -> Root -> Right
    """

    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

def preorder(root):
    """
    Root -> Left -> Right
    """

    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    """
    Left -> Right -> Root
    """

    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")


        
