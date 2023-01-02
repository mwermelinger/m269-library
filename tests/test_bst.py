"""Unit tests for binary search trees."""

from lib.bst import BinarySearchTree


class TestBST:
    def setup_method(self):
        # The keys are unique house numbers in a street.
        # The values are the names of inhabitants.
        self.houses = list(range(31, 36))
        self.people = ["Jane", "John", "Ann", "Bob", "John"]
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
        self.balanced.add(33, "Ann")
        self.balanced.add(34, "Bob")
        self.balanced.add(35, "John")
        self.balanced.add(32, "John")
        self.balanced.add(31, "Jane")

    def test_is_empty(self):
        assert self.new.is_empty()
        assert self.empty.is_empty()
        assert not self.root.is_empty()
        assert not self.linear.is_empty()
        assert not self.balanced.is_empty()

    def test_height(self):
        assert self.new.height() == 0
        assert self.empty.height() == 0
        assert self.root.height() == 1
        assert self.linear.height() == 5
        assert self.balanced.height() == 3

    def test_smallest_key(self):
        assert self.new.smallest_key() is None
        assert self.empty.smallest_key() is None
        assert self.root.smallest_key() == self.houses[-1]
        assert self.linear.smallest_key() == self.houses[0]
        assert self.balanced.smallest_key() == self.houses[0]

    def test_in_order(self):
        assert self.new.in_order() == []
        assert self.empty.in_order() == []
        assert self.root.in_order() == [self.houses[-1]]
        assert self.linear.in_order() == self.houses
        assert self.balanced.in_order() == self.houses

    def test_post_order(self):
        assert self.new.post_order() == []
        assert self.empty.post_order() == []
        assert self.root.post_order() == [self.houses[-1]]
        assert self.linear.post_order() == [35, 34, 33, 32, 31]
        assert self.balanced.post_order() == [31, 32, 35, 34, 33]

    def test_value(self):
        for key, value in zip(self.houses, self.people):
            assert self.new.value(key) is None
            assert self.empty.value(key) is None
            if key == self.houses[-1]:
                assert self.root.value(key) == value
            else:
                assert self.root.value(key) is None
            assert self.linear.value(key) == value
            assert self.balanced.value(key) == value

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
        assert not key in self.new
        self.empty.remove(key)
        assert not key in self.empty
        self.root.remove(key)
        assert not key in self.root
        self.linear.remove(key)
        assert not key in self.linear
        self.balanced.remove(key)
        assert not key in self.balanced
        # Remove from the inputs. Test retrieval for the other keys.
        self.houses.pop(index)
        self.people.pop(index)
        self.test_value()
