"""Unit tests for the Deque class."""

import unittest

from lib.deque import Deque

class TestDeque(unittest.TestCase):

    def setUp(self):
        # Create queues for the tests to use
        self.new = Deque()
        # Test combination of add/remove
        self.empty = Deque()
        self.empty.add_front('hi')
        self.empty.remove_rear()
        # Don't add in ascending or descending order
        self.from_front = Deque()
        self.from_front.add_front(5)
        self.from_front.add_front(2)
        self.from_front.add_front(7)
        self.from_front.add_front(2)
        # Same the other way round
        self.from_rear = Deque()
        self.from_rear.add_rear(2)
        self.from_rear.add_rear(7)
        self.from_rear.add_rear(2)
        self.from_rear.add_rear(5)
        
    def test_length(self):
        self.assertEqual(len(self.new), 0)
        self.assertEqual(len(self.empty), 0)
        self.assertEqual(len(self.from_front), 4)

    def test_is_empty(self):
        self.assertTrue(self.new.is_empty())
        self.assertTrue(self.empty.is_empty())
        self.assertFalse(self.from_front.is_empty())
        
    def test_str(self):
        self.assertEqual(str(self.new), str(self.empty))
        self.assertEqual(str(self.from_front), str(self.from_rear))

    def test_fifo_order(self):
        self.assertEqual(self.from_front.remove_rear(), 5)
        self.assertEqual(self.from_front.remove_rear(), 2)
        self.assertEqual(self.from_front.remove_rear(), 7)
        self.assertEqual(self.from_front.remove_rear(), 2)
        # FIFO is opposite order in other deque
        self.assertEqual(self.from_rear.remove_front(), 2)
        self.assertEqual(self.from_rear.remove_front(), 7)
        self.assertEqual(self.from_rear.remove_front(), 2)
        self.assertEqual(self.from_rear.remove_front(), 5)

    def test_lifo_order(self):
        self.assertEqual(self.from_front.remove_front(), 2)
        self.assertEqual(self.from_front.remove_front(), 7)
        self.assertEqual(self.from_front.remove_front(), 2)
        self.assertEqual(self.from_front.remove_front(), 5)
        # LIFO is opposite order in other deque
        self.assertEqual(self.from_rear.remove_rear(), 5)
        self.assertEqual(self.from_rear.remove_rear(), 2)
        self.assertEqual(self.from_rear.remove_rear(), 7)
        self.assertEqual(self.from_rear.remove_rear(), 2)
        
    def test_access_to_empty(self):
        with self.assertRaises(AssertionError):
            self.new.front()
        with self.assertRaises(AssertionError):
            self.empty.rear()
        with self.assertRaises(AssertionError):
            self.new.remove_rear()
        with self.assertRaises(AssertionError):
            self.empty.remove_front()

    def test_membership(self):
        self.assertFalse(2 in self.new)
        self.assertFalse('hi' in self.empty)
        self.assertTrue(2 in self.from_front)
        self.assertTrue(5 in self.from_front)
        self.assertTrue(7 in self.from_front)
        self.assertFalse(3 in self.from_front)
        