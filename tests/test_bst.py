"""Unit tests for binary search trees."""

import unittest

from lib.bst import BinarySearchTree

class TestBST(unittest.TestCase):

    def setUp(self):
        # The keys are unique house numbers in a street.
        # The values are the names of inhabitants.
        self.houses = [number for number in range(31, 36)]
        self.people = ['Jane', 'John', 'Ann', 'Bob', 'John']
        # Create trees for the tests to use.
        # A brand new tree.
        self.new = BinarySearchTree()
        # An empty tree. Tests removal of single node.
        self.empty = BinarySearchTree()
        self.empty.add(self.houses[0], self.people[0])
        self.empty.remove(self.houses[0])
        # Tree with a single node, with highest key.
        self.root = BinarySearchTree()
        self.root.add(self.houses[-1], self.people[-1])
        # Unbalanced tree: add the keys in ascending order.
        self.linear = BinarySearchTree()
        for house, person in zip(self.houses, self.people):
            self.linear.add(house, person)
        # Balanced tree: first add the median key.
        self.balanced = BinarySearchTree()
        self.balanced.add(33, 'Ann')
        self.balanced.add(34, 'Bob')
        self.balanced.add(35, 'John')
        self.balanced.add(32, 'John')
        self.balanced.add(31, 'Jane')

    def test_is_empty(self):
        self.assertTrue(self.new.is_empty())
        self.assertTrue(self.empty.is_empty())
        self.assertFalse(self.root.is_empty())   
        self.assertFalse(self.linear.is_empty())
        self.assertFalse(self.balanced.is_empty())

    def test_height(self):
        self.assertEqual(self.new.height(), -1)
        self.assertEqual(self.empty.height(), -1)
        self.assertEqual(self.root.height(), 0)   
        self.assertEqual(self.linear.height(), 4)
        self.assertEqual(self.balanced.height(), 2)
        
    def test_smallest_key(self):
        self.assertEqual(self.new.smallest_key(), None)
        self.assertEqual(self.empty.smallest_key(), None)
        self.assertEqual(self.root.smallest_key(), self.houses[-1])   
        self.assertEqual(self.linear.smallest_key(), self.houses[0])
        self.assertEqual(self.balanced.smallest_key(), self.houses[0])

    def test_in_order(self):
        self.assertEqual(self.new.in_order(), [])
        self.assertEqual(self.empty.in_order(), [])
        self.assertEqual(self.root.in_order(), [self.houses[-1]])   
        self.assertEqual(self.linear.in_order(), self.houses)
        self.assertEqual(self.balanced.in_order(), self.houses)
        
    def test_value(self):
        self.assertEqual(self.new.value(), [])
        self.assertEqual(self.empty.value(), [])
        self.assertEqual(self.root.value(), [self.houses[-1]])   
        self.assertEqual(self.linear.value(), self.houses)
        self.assertEqual(self.balanced.value(), [key, 32, 31, 34, 35])
        
    def test_post_order(self):
        self.assertEqual(self.new.post_order(), [])
        self.assertEqual(self.empty.post_order(), [])
        self.assertEqual(self.root.post_order(), [self.houses[-1]])   
        self.assertEqual(self.linear.post_order(), [35, 34, 33, 32, 31])
        self.assertEqual(self.balanced.post_order(), [31, 32, 35, 34, 33])

    def test_value(self):
        for key, value in zip(self.houses, self.people):
            self.assertEqual(self.new.value(key), None)
            self.assertEqual(self.empty.value(key), None)
            if key == self.houses[-1]:
                self.assertEqual(self.root.value(key), value)
            else:
                self.assertEqual(self.root.value(key), None)                
            self.assertEqual(self.linear.value(key), value)
            self.assertEqual(self.balanced.value(key), value)
            
    def test_value_change(self):
        # The previous tests with setUp already test adding new nodes.
        # This test checks the change of value for an existing key.
        # Swap the values of the lowest and highest keys.
        self.people[0], self.people[-1] = self.people[-1], self.people[0]
        # Update the affected trees.
        self.root.add(self.houses[-1], self.people[-1])
        self.linear.add(self.houses[0], self.people[0])
        self.linear.add(self.houses[-1], self.people[-1])
        self.balanced.add(self.houses[0], self.people[0])
        self.balanced.add(self.houses[-1], self.people[-1])
        # Test retrieval of the new values.
        self.test_value()
        
    def test_remove_and_contains(self):
        # Get the middle key: it's the root of the balanced tree,
        # and doesn't exist in the single-node tree.
        index = len(self.houses) // 2
        key = self.houses[index]
        # Remove it from each tree and confirm it's not found anymore.
        # This also tests that removing an unknown key doesn't change a tree.
        self.new.remove(key)
        self.assertFalse(key in self.new)
        self.empty.remove(key)
        self.assertFalse(key in self.empty)
        self.root.remove(key)
        self.assertFalse(key in self.root)
        self.linear.remove(key)
        self.assertFalse(key in self.linear)
        self.balanced.remove(key)
        self.assertFalse(key in self.balanced)
        # Remove from the inputs. Test retrieval for the other keys.
        self.houses.pop(index)
        self.people.pop(index)
        self.test_value()
