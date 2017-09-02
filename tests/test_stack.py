"""Unit tests for the Stack class."""

import unittest

from lib.stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        # Create stacks for the tests to use
        self.new = Stack()
        self.empty = Stack()
        self.empty.push('hi')
        self.empty.pop()
        # Don't add in ascending or descending order
        self.non_empty = Stack()
        self.non_empty.push(5)
        self.non_empty.push(2)
        self.non_empty.push(7)
        self.non_empty.push(2)

    def test_length(self):
        self.assertEqual(len(self.new), 0)
        self.assertEqual(len(self.empty), 0)
        self.assertEqual(len(self.non_empty), 4)

    def test_is_empty(self):
        self.assertTrue(self.new.is_empty())
        self.assertTrue(self.empty.is_empty())
        self.assertFalse(self.non_empty.is_empty())

    def test_lifo_order(self):
        self.assertEqual(self.non_empty.pop(), 2)
        self.assertEqual(self.non_empty.pop(), 7)
        self.assertEqual(self.non_empty.pop(), 2)
        self.assertEqual(self.non_empty.pop(), 5)

    def test_access_to_empty(self):
        with self.assertRaises(AssertionError):
            self.new.top()
        with self.assertRaises(AssertionError):
            self.empty.top()
        with self.assertRaises(AssertionError):
            self.new.pop()
        with self.assertRaises(AssertionError):
            self.empty.pop()

    def test_membership(self):
        self.assertFalse(2 in self.new)
        self.assertFalse(2 in self.empty)
        self.assertTrue(2 in self.non_empty)
        self.assertTrue(5 in self.non_empty)
        self.assertTrue(7 in self.non_empty)
        