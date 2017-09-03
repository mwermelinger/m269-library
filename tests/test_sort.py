"""Unit tests for the sort module."""

import unittest

from lib.sort import bubble_sort, selection_sort, insertion_sort
from lib.sort import merge_sorted, quick_sorted, heap_sorted
from lib.sort import nth_smallest

class TestSort(unittest.TestCase):

    def setUp(self):
        # Create lists for the tests to use
        # Each list has different values so that if a test fails,
        # it is clear from unittest's output which example failed.
        self.examples = (
            # base cases
            [],
            [3],
            # already in ascending or descending order
            [-1, 1, 4],
            [7, 2, 0],
            # sorting strings
            ['hi', 'Jane'],
            # duplicate values
            ['ho', 'ho', 'ho'],
            [30, 20, 10, 10, 20, 30]
        )

    def test_sorted(self):
        for example in self.examples:
            # Check each algorithm against the built-in sort.
            expected = sorted(example)
            self.assertEqual(merge_sorted(example), expected)
            self.assertEqual(quick_sorted(example), expected)
            self.assertEqual(heap_sorted(example), expected)

    # The examples are set up anew before each test. Hence each algorithm
    # can modify each list without affecting other tests.
    
    def test_bubble_sort(self):
        for example in self.examples:
            expected = sorted(example)
            bubble_sort(example)
            self.assertEqual(example, expected)

    def test_selection_sort(self):
        for example in self.examples:
            expected = sorted(example)
            selection_sort(example)
            self.assertEqual(example, expected)

    def test_insertion_sort(self):
        for example in self.examples:
            expected = sorted(example)
            insertion_sort(example)
            self.assertEqual(example, expected)

    def test_quickselect(self):
        for example in self.examples:
            n = len(example)
            if n > 0:
                self.assertEqual(nth_smallest(example, 1), min(example))
                self.assertEqual(nth_smallest(example, n), max(example))
            if n > 1:
                middle = n // 2
                expected = sorted(example)[middle - 1]
                self.assertEqual(nth_smallest(example, middle), expected)
 
# Exercises
# ---------
# - For each of the `...sort` tests, the expected output is needed only once.
#   Why is the code not simply `self.assertEqual(example, sorted(example))`?
# - Explain what the quickselect test is doing and why. For example,
#   why is it comparing n against 0 and 1, and why `middle-1` and not `middle`?