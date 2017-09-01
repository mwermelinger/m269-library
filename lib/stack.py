"""An implementation of unbounded stacks."""


class Stack:
    """An ordered collection of items, organised in a pile.

    Items are added to the top of the pile.
    Only the last item added can be accessed or removed.
    """

    # Creator
    # -------

    def __init__(self):
        """Initialise the stack to be empty."""
        self._items = []

    # Inspectors
    # ----------

    def is_empty(self):
        """Return True if the stack is empty, otherwise False."""
        return self._items == []

    def size(self):
        """Return the number of items in the stack."""
        return len(self._items)

    def top(self):
        """Return the item on top of the stack.

        Assume the stack is not empty.
        """
        assert not self.is_empty()
        return self._items[-1]

    # Modifiers
    # ---------

    def push(self, item):
        """Add the item to the top of the stack. Return nothing."""
        self._items.append(item)

    def pop(self):
        """Remove and return the item on top of the stack.

        Assume the stack is not empty.
        """
        assert not self.is_empty()
        return self._items.pop()


# Exercises
# ---------

# - What is the run-time complexity of each operation?
