"""Unit tests for the Queue class."""

import unittest

from lib.queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        # Create queues for the tests to use
        self.new = Queue()
        self.empty = Queue()
        self.empty.enqueue("hi")
        self.empty.dequeue()
        # Don't add in ascending or descending order
        self.non_empty = Queue()
        self.non_empty.enqueue(5)
        self.non_empty.enqueue(2)
        self.non_empty.enqueue(7)
        self.non_empty.enqueue(2)

    def test_length(self):
        self.assertEqual(len(self.new), 0)
        self.assertEqual(len(self.empty), 0)
        self.assertEqual(len(self.non_empty), 4)

    def test_is_empty(self):
        self.assertTrue(self.new.is_empty())
        self.assertTrue(self.empty.is_empty())
        self.assertFalse(self.non_empty.is_empty())

    def test_fifo_order(self):
        self.assertEqual(self.non_empty.dequeue(), 5)
        self.assertEqual(self.non_empty.dequeue(), 2)
        self.assertEqual(self.non_empty.dequeue(), 7)
        self.assertEqual(self.non_empty.dequeue(), 2)

    def test_access_to_empty(self):
        with self.assertRaises(AssertionError):
            self.new.front()
        with self.assertRaises(AssertionError):
            self.empty.front()
        with self.assertRaises(AssertionError):
            self.new.dequeue()
        with self.assertRaises(AssertionError):
            self.empty.dequeue()

    def test_membership(self):
        self.assertFalse(2 in self.new)
        self.assertFalse(2 in self.empty)
        self.assertTrue(2 in self.non_empty)
        self.assertTrue(5 in self.non_empty)
        self.assertTrue(7 in self.non_empty)
