"""A first in, first out collection of items."""

# This is part of the [M269 Library](http://tiny.cc/m269-library).

# The following constants make the code more readable.
# pylint: disable=invalid-name

_ITEM = 0
_NEXT = 1


class Queue:
    """Provide an ordered collection of items with FIFO access.

    Items can only be added at the end of the queue.
    Items can only be removed from the front of the queue.
    """

    # Representation
    # --------------
    # The queue is represented as a linked list of nodes.
    # Each node has one item and points to the next node.
    # The next node of the last node is `None`.
    # A node is represented by a Python list of size 2:
    # position 0 has the item, position 1 has the next node.
    # Hence the constants above.
    #
    # The queue is a pair of pointers, to the first and last nodes.
    # This allows direct access to the front and back of the queue,
    # to quickly add and remove items.
    # If the queue is empty, the first and last nodes are `None`.

    # Creator
    # -------

    def __init__(self):
        """Initialise the queue to be empty."""
        self._first = None
        self._last = None

    # Inspectors
    # ----------

    def is_empty(self):
        """Return True if the queue is empty, otherwise False."""
        return self._first is None

    def __len__(self):
        """Implement the `len` function for queues.

        Return the number of items in the queue.
        """
        length = 0
        node = self._first
        while node is not None:
            length = length + 1
            node = node[_NEXT]
        return length

    def front(self):
        """Return the item at the front of the queue.

        Assume the queue is not empty.
        """
        assert not self.is_empty()
        return self._first[_ITEM]

    def __contains__(self, item):
        """Implement the `in` operator for queues.

        Return True if the queue has the item, otherwise False.
        """
        node = self._first
        while node is not None and node[_ITEM] != item:
            node = node[_NEXT]
        return node is not None

    # Modifiers
    # ---------

    def enqueue(self, item):
        """Add item to the back of the queue. Return nothing."""
        node = [item, None]
        if self.is_empty():
            self._first = node
            self._last = node
        else:
            self._last[_NEXT] = node
            self._last = node

    def dequeue(self):
        """Remove and return the item at the front of the queue.

        Assume the queue is not empty.
        """
        assert not self.is_empty()
        item = self.front()
        self._first = self._first[_NEXT]
        if self._first is None:
            self._last = None
        return item

# - Why is there a method `is_empty`? Client code could easily just call
#   `len(items) == 0` instead.
