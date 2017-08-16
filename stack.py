class Stack:
    """An ordered collection of items, organised in a pile.

    Items are added to the top of the pile.
    Only the last item added can be accessed or removed.
    """

    # Creator
    # -------

    def __init__(self):
        """Initialise the stack to be empty."""
        self.items = []

    # Inspectors
    # ----------

    def is_empty(self):
        """Return True if the stack is empty, otherwise False."""
        return self.items == []

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def top(self):
        """Return the item on top of the stack.

        Assume the stack is not empty.
        """
        return self.items[-1]

    # Modifiers
    # ---------

    def push(self, the_item):
        """Add the_item to the top of the stack. Return nothing."""
        self.items.append(the_item)

    def pop(self):
        """Remove and return the item on top of the stack.

        Assume the stack is not empty.
        """
        return self.items.pop()


# Exercises
# ---------

# - What is the run-time complexity of each operation?
