"""A double-ended queue."""

# This is part of the [M269 Library](http://tiny.cc/m269-library).

# The following constants make the code more readable.
# pylint: disable=invalid-name

_PREVIOUS = 0
_ITEM = 1
_NEXT = 2


class Deque:
    """Provide a sequence of items that are accessed from the start and end.

    A deque (pronounced: deck) is a queue where items
    can be added and removed from either end.
    """

    # Representation
    # --------------
    # The queue is represented as a doubly linked list of nodes.
    # Each node has one item and points to the next and previous nodes.
    # The next node of the last node is `None`,
    # and so is the previous node of the first node.
    # A node is represented by a Python list of size 3:
    # position 0 has the item, position 1 has the next node,
    # position 2 has the previous node.
    # Hence the constants above.
    #
    # The deque is a pair of pointers, to the first and last nodes.
    # This allows direct access to the front and back of the queue,
    # to quickly add and remove items.
    # If the queue is empty, the first and last nodes are `None`.

    # Creator
    # -------

    def __init__(self):
        """Initialise the queue to be empty."""
        self._first = None
        self._last = None
        self._length = 0

    # Inspectors
    # ----------

    def is_empty(self):
        """Return True if the queue is empty, otherwise False."""
        return self._first is None

    def __len__(self):
        """Implement the `len` function for queues.

        Return the number of items in the queue.
        """
        return self._length

    def front(self):
        """Return the item at the front of the queue.

        Assume the queue is not empty.
        """
        assert not self.is_empty()
        return self._first[_ITEM]

    def rear(self):
        """Return the item at the back of the queue.

        Assume the queue is not empty.
        """
        assert not self.is_empty()
        return self._last[_ITEM]

    def __contains__(self, item):
        """Implement the `in` operator for queues.

        Return True if the queue has the item, otherwise False.
        """
        node = self._first
        while node is not None and node[_ITEM] != item:
            node = node[_NEXT]
        return node is not None

    def __str__(self):
        """Return a string representation of the deque."""
        string = "["
        node = self._first
        while node is not None:
            string += str(node[_ITEM])
            node = node[_NEXT]
        return string + "]"

    # Modifiers
    # ---------

    def add_front(self, item):
        """Add the item to the front of the queue. Return nothing."""
        node = [None, item, self._first]
        if self.is_empty():
            self._first = node
            self._last = node
        else:
            self._first[_PREVIOUS] = node
            self._first = node
        self._length += 1

    def add_rear(self, item):
        """Add the item to the back of the queue. Return nothing."""
        node = [self._last, item, None]
        if self.is_empty():
            self._first = node
            self._last = node
        else:
            self._last[_NEXT] = node
            self._last = node
        self._length += 1

    def remove_front(self):
        """Remove and return the item at the front of the queue.

        Assume the queue is not empty.
        """
        assert not self.is_empty()
        item = self.front()
        self._first = self._first[_NEXT]
        if self._first is None:
            self._last = None
        else:
            self._first[_PREVIOUS] = None
        self._length -= 1
        return item

    def remove_rear(self):
        """Remove and return the item at the back of the queue.

        Assume the queue is not empty.
        """
        assert not self.is_empty()
        item = self.rear()
        self._last = self._last[_PREVIOUS]
        if self._last is None:
            self._first = None
        else:
            self._last[_NEXT] = None
        self._length -= 1
        return item

# Exercises
# ---------
# - Add methods `index_front` and `index_rear` that return
#   the first (resp. last) position of a given item.
#   Positions start at 0 from the front of the deque.
#   Decide what to do if the item doesn't exist in the deque.
