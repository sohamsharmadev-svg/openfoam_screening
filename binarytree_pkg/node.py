class Node:
    """
    Represents a node in a binary tree.
    Each node stores a value and references to left and right children.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"
