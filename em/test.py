import em.diameter_of_binary_tree
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = em.diameter_of_binary_tree.BinaryTree(1)
        root.left = em.diameter_of_binary_tree.BinaryTree(3)
        root.left.left = em.diameter_of_binary_tree.BinaryTree(7)
        root.left.left.left = em.diameter_of_binary_tree.BinaryTree(8)
        root.left.left.left.left = em.diameter_of_binary_tree.BinaryTree(9)
        root.left.right = em.diameter_of_binary_tree.BinaryTree(4)
        root.left.right.right = em.diameter_of_binary_tree.BinaryTree(5)
        root.left.right.right.right = em.diameter_of_binary_tree.BinaryTree(6)
        root.right = em.diameter_of_binary_tree.BinaryTree(2)
        expected = 6
        actual = em.diameter_of_binary_tree.binary_tree_parameter(root)
        print(actual)
        self.assertEqual(actual, expected)
