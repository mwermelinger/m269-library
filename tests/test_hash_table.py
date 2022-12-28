"""Unit tests for binary search tables."""

import unittest

from lib.hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self):
        # The keys are unique house numbers in a street.
        # The values are the names of inhabitants.
        self.houses = list(range(31, 36))
        self.people = ["Jane", "John", "Ann", "Bob", "John"]
        # Create tables for the tests to use.
        # A brand new table.
        self.new = HashTable(5)
        # An empty table. Tests removal of single entry.
        self.empty = HashTable(5)
        self.empty.add(self.houses[0], self.people[0])
        self.empty.remove(self.houses[0])
        # A table with a single entry, with highest key.
        self.single = HashTable(5)
        self.single.add(self.houses[-1], self.people[-1])
        # A table with keys added in ascending order.
        self.ascending = HashTable(5)
        for house, person in zip(self.houses, self.people):
            self.ascending.add(house, person)
        # A table with keys added in descending order.
        self.descending = HashTable(5)
        for house, person in zip(reversed(self.houses), reversed(self.people)):
            self.descending.add(house, person)

    def test_len(self):
        self.assertEqual(len(self.new), 0)
        self.assertEqual(len(self.empty), 0)
        self.assertEqual(len(self.single), 1)
        self.assertEqual(len(self.ascending), 5)
        self.assertEqual(len(self.descending), 5)

    def test_value(self):
        for key, value in zip(self.houses, self.people):
            self.assertEqual(self.new.value(key), None)
            self.assertEqual(self.empty.value(key), None)
            if key == self.houses[-1]:
                self.assertEqual(self.single.value(key), value)
            else:
                self.assertEqual(self.single.value(key), None)
            self.assertEqual(self.ascending.value(key), value)
            self.assertEqual(self.descending.value(key), value)

    def test_value_change(self):
        # The previous tests with setUp already test adding new entries.
        # This test checks the change of value for an existing key.
        # Swap the values of the lowest and highest keys.
        self.people[0], self.people[-1] = self.people[-1], self.people[0]
        # Update the affected tables.
        self.single.add(self.houses[-1], self.people[-1])
        self.ascending.add(self.houses[0], self.people[0])
        self.ascending.add(self.houses[-1], self.people[-1])
        self.descending.add(self.houses[0], self.people[0])
        self.descending.add(self.houses[-1], self.people[-1])
        # Test retrieval of the new values.
        self.test_value()

    def test_remove_and_contains(self):
        # Get the middle key: it doesn't exist in the single-entry table.
        index = len(self.houses) // 2
        key = self.houses[index]
        # Remove it from each table and confirm it's not found anymore.
        # This also tests that removing an unknown key doesn't change a table.
        self.new.remove(key)
        self.assertFalse(key in self.new)
        self.empty.remove(key)
        self.assertFalse(key in self.empty)
        self.single.remove(key)
        self.assertFalse(key in self.single)
        self.ascending.remove(key)
        self.assertFalse(key in self.ascending)
        self.descending.remove(key)
        self.assertFalse(key in self.descending)
        # Remove from the inputs. Test retrieval for the other keys.
        self.houses.pop(index)
        self.people.pop(index)
        self.test_value()

    def test_replacement(self):
        # Remove all entries.
        for key in self.houses:
            self.ascending.remove(key)
        # Re-insert keys in descending order with different values.
        for key, value in zip(reversed(self.houses), self.people):
            self.ascending.add(key, value)
        # Check they're found.
        for key, value in zip(self.houses, reversed(self.people)):
            self.assertEqual(self.ascending.value(key), value)

    def test_capacity(self):
        # Remove all entries.
        for key in self.houses:
            self.ascending.remove(key)
        # Try to add a new one.
        self.assertEqual(self.ascending.add(30, "me"), False)
