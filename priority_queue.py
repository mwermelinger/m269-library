"""An implementation of a priority queue (min binary heap)."""

# The following constants make the code more readable.

_KEY = 0    # pylint: disable=invalid-name
_VALUE = 1  # pylint: disable=invalid-name


class PriorityQueue:
    """A collection of priority-item pairs.

    Items are accessed and removed from highest to lowest priority.
    Priorities can be represented by any data type with the `<` operator.
    A **smaller** value means a **higher** priority, e.g.
    priority 1 is higher than priority 2,
    priority 'A' is higher than priority 'B'.
    """

    # Representation
    # --------------
    # The priority queue is implemented as a min binary heap,
    # which is a complete binary tree where:
    # each node is a key-value pair;
    # keys are comparable but don't have to be unique;
    # each node's key is smaller than or equal to its children's keys.
    # The heap is represented as a list starting at position 1.
    # Because the tree is binary and complete, if a node is at position n
    # then its children (if they exist), must be at positions 2n and 2n+1.
    # Conversely, if a node is at position n, its parent is at n // 2.
    #
    # Each heap node is a list of length 2 (key and value).
    #
    # For a priority queue the key is the priority and the value is the item.
    # The method signatures and docstrings refer to
    # the public view (a queue with items and priorities),
    # but the code and comments refer to
    # the internal view (a heap with key-value nodes).

    # Creator
    # -------

    def __init__(self, pairs=None):
        """Initialise the queue with a list of priority-item pairs.

        If no pairs are given, the queue starts empty.
        """
        # Position 0 is just a filler to start the heap at position 1.
        self._nodes = [None]
        if pairs is not None:
            self._nodes = self._nodes + pairs
        # The leaves have no children, so they obey the ordering property.
        # Therefore start with the last non-leaf node,
        # and go up to the root, putting each node in its correct position.
        for current in range(self.size() // 2, 0, -1):
            self._bubble_down(current)

    # Inspectors
    # ----------

    def size(self):
        """Return the number of items in the queue."""
        return len(self._nodes) - 1

    def is_empty(self):
        """Return True if the queue is empty, otherwise False."""
        return self.size() == 0

    def front(self):
        """Return the item at the front of the queue, with highest priority.

        Assume the queue is not empty.
        """
        assert not self.is_empty()
        # In a min heap, a smallest key (= highest priority) is in the root.
        return self._nodes[1][_VALUE]

    # The following inspectors are for internal use.

    def _exists(self, position):
        # Check if the position is valid.
        return 1 <= position <= self.size()

    def _less(self, position1, position2):
        # Check if position1 has a smaller key than position2.
        return self._nodes[position1][_KEY] < self._nodes[position2][_KEY]

    # Modifiers
    # ---------

    # The following modifiers are for internal use.

    def _exchange(self, position1, position2):
        # Exchange the nodes at the two positions.
        temporary = self._nodes[position1]
        self._nodes[position1] = self._nodes[position2]
        self._nodes[position2] = temporary

    # The following are called bubble up/down because they swap
    # 'adjacent' (i.e. parent-child) nodes, similarly to Bubble Sort.
    # Other names typically used are percolate up/down and sift up/down.

    def _bubble_up(self, current):
        # Move the node at the current position upwards to its correct place.
        parent = current // 2
        # If the node has a parent that has a larger key,
        if self._exists(parent) and self._less(current, parent):
            # swap it with the parent
            self._exchange(current, parent)
            # and continue to move it further up.
            self._bubble_up(parent)

    def _bubble_down(self, current):
        # Move the node at the current position downwards to its correct place.
        left = current * 2
        # If the node is not a leaf,
        if self._exists(left):
            # compute its smallest child.
            right = left + 1
            if self._exists(right) and self._less(right, left):
                smallest = right
            else:
                smallest = left
            # If the child is smaller than the node,
            if self._less(smallest, current):
                # swap it with that child
                self._exchange(smallest, current)
                # and continue to move it down.
                self._bubble_down(smallest)

    # The following modifiers are for public use.

    def enqueue(self, item, priority):
        """Add the item with the given priority to the queue.

        Return nothing.
        """
        # Add the node as the last leaf of the heap.
        self._nodes.append([priority, item])
        # Move it up the heap to its proper place.
        self._bubble_up(self.size())

    def dequeue(self):
        """Remove and return the item with the highest priority.

        Assume the heap is not empty.
        """
        assert self.size() > 0
        item = self.front()
        # Replace the root by the last leaf.
        self._nodes[1] = self._nodes[-1]
        self._nodes.pop()
        # Move it down the heap to its proper place.
        self._bubble_down(1)
        return item

    def set_priority(self, item, priority):
        """Change the item's priority to the new value. Return nothing.

        Do nothing if the item isn't in the queue.
        Assume items are unique.
        """
        # Do a linear search to find the node with the item.
        for index in range(1, len(self._nodes)):
            if self._nodes[index][_VALUE] == item:
                key = self._nodes[index][_KEY]
                self._nodes[index][_KEY] = priority
                # If the key has increased, move the node down, otherwise up.
                if key < priority:
                    self._bubble_down(index)
                else:
                    self._bubble_up(index)
                # Stop the search.
                break
