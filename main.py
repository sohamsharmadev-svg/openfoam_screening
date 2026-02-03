from binarytree_pkg import *

if __name__ == "__main__":

    root = create_tree(10)

    add_node_by_path(root, "L", 5)
    add_node_by_path(root, "R", 15)
    add_node_by_path(root, "LL", 3)
    add_node_by_path(root, "LR", 7)

    print("\nTREE CREATED:\n")
    print_tree(root)

    # Write to YAML
    write_tree_to_yaml(root, "tree.yaml")

    print("\nTREE LOADED FROM YAML:\n")

    yaml_root = build_tree_from_yaml("tree.yaml")
    print_tree(yaml_root)


    edit_node(root, "LL", 99)

print("\nTREE AFTER EDIT:\n")
print_tree(root)


delete_node(root, "LR")

print("\nTREE AFTER DELETE:\n")
print_tree(root)


print("\nINORDER:")
inorder(root)

print("\n\nPREORDER:")
preorder(root)

print("\n\nPOSTORDER:")
postorder(root)



