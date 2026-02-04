import yaml
from .node import Node

def dict_to_tree(data):

    if data is None:
        return None

    node = Node(data["value"])

    node.left = dict_to_tree(data.get("left"))
    node.right = dict_to_tree(data.get("right"))

    return node


def build_tree_from_yaml(file_path):

    with open(file_path, "r") as f:
        data = yaml.safe_load(f)

    return dict_to_tree(data)


def tree_to_dict(node):

    if node is None:
        return None

    return {
        "value": node.value,
        "left": tree_to_dict(node.left),
        "right": tree_to_dict(node.right)
    }


def write_tree_to_yaml(root, file_path):

    with open(file_path, "w") as f:
        yaml.dump(tree_to_dict(root), f)
