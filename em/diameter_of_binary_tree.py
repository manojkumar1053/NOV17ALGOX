class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binary_tree_diameter(tree):
    return get_tree_info(tree).diameter


def get_tree_info(tree):
    if tree is None:
        return Tree_Info(0, 0)

    left_tree_data = get_tree_info(tree.left)
    right_tree_data = get_tree_info(tree.right)

    longest_path_through_root = left_tree_data.height + right_tree_data.height
    max_diameter_so_far = max(left_tree_data.diameter, right_tree_data.diameter)
    current_diameter = max(longest_path_through_root, max_diameter_so_far)
    current_height = 1 + max(left_tree_data.height, right_tree_data.height)

    return Tree_Info(current_diameter, current_height)


class Tree_Info:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height

root = BinaryTree(1)
root.left =BinaryTree(3)
root.left.left = BinaryTree(7)
root.left.left.left =BinaryTree(8)
root.left.left.left.left = BinaryTree(9)
root.left.right = BinaryTree(4)
root.left.right.right = BinaryTree(5)
root.left.right.right.right = BinaryTree(6)
root.right = BinaryTree(2)

print(root.left.value)

print(binary_tree_diameter(root))
