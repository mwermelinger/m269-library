"""A binary tree ordered by key."""


class BinarySearchTree:
    """
    Provide a collection of key-value pairs with unique and comparable keys.

    A binary tree is either empty or consists of a node (called the root)
    and two subtrees (called the left and right subtree).

    A Binary Search Tree (BST) is a binary tree in which
    - every node is a key-value pair,
    - every key in the left subtree is smaller than the root's key,
    - every key in the right subtree is larger than the root's key.
    """

    # Creator
    # -------

    def __init__(self):
        """Initialise the tree to be empty."""
        # An empty tree has neither a root nor subtrees.
        self._key = None
        self._value = None
        self._left = None
        self._right = None

    # Inspectors
    # ----------

    def is_empty(self):
        """Return True if the tree is empty, otherwise False."""
        return self._key is None

    def value(self, the_key):
        """Return the value associated to the_key in the tree.

        Return None if the tree hasn't the_key.
        """
        # Base case: the tree is empty.
        if self.is_empty():
            return None
        # Base case: the key is in the root.
        if the_key == self._key:
            return self._value
        # Reduction step: choose the appropriate subtree.
        # Recursive step: get the value in that subtree.
        # Inductive step: not needed.
        if the_key < self._key:
            return self._left.value(the_key)
        return self._right.value(the_key)

    def __contains__(self, the_key):
        """Implement the `in` operator for binary search trees.

        Return True if the tree has the_key, otherwise False.
        """
        return self.value(the_key) is not None

    def height(self):
        """Return the height of the tree.

        Follow the definition in M269:
        The height is the maximum number of edges from the root to any leaf.
        The height of the empty tree is -1.
        """
        # Base case: the empty tree.
        if self.is_empty():
            return -1
        # Reduction step: consider both subtrees.
        # Recursive step: find their height.
        left_height = self._left.height()
        right_height = self._right.height()
        # Inductive step: take the maximal height, add 1 edge from the root.
        return max(left_height, right_height) + 1

    def in_order(self):
        """Do an in-order traversal of the tree.

        Return a list of the keys in the tree, in the order visited.
        """
        # Base case: the empty tree.
        if self.is_empty():
            return []
        # Reduction step: consider each subtree.
        # Recursive step: traverse each subtree.
        left_keys = self._left.in_order()
        right_keys = self._right.in_order()
        # Inductive step: put the keys in the right order
        return left_keys + [self._key] + right_keys

    def pre_order(self):
        """Do a pre-order traversal of the tree.

        Return a list of the keys in the tree, in the order visited.
        """
        if self.is_empty():
            return []
        left_keys = self._left.pre_order()
        right_keys = self._right.pre_order()
        return [self._key] + left_keys + right_keys

    def post_order(self):
        """Do a post-order traversal of the tree.

        Return a list of the keys in the tree, in the order visited.
        """
        if self.is_empty():
            return []
        left_keys = self._left.post_order()
        right_keys = self._right.post_order()
        return left_keys + right_keys + [self._key]

    def smallest_key(self):
        """Return the smallest key in the tree.

        Return None if the tree is empty.
        """
        # Base case: the empty tree.
        if self.is_empty():
            return None
        # Base case: the smallest key is in the root.
        if self._left.is_empty():
            return self._key
        # Reduction step: only consider the left subtree.
        # Recursive step: find the smallest node there.
        # Inductive step: not needed.
        return self._left.smallest_key()

    # Modifiers
    # ---------

    def add(self, the_key, the_value):
        """Associate the_value to the_key in the tree. Return nothing.

        Assume the_value is not None.
        If the tree has the_key, replace its associated value by the_value.
        If it hasn't, add a new node with the_key and the_value.
        """
        assert the_value is not None
        # Base case: if the tree is empty, create one with the key-value pair.
        if self.is_empty():
            self._key = the_key
            self._value = the_value
            self._left = BinarySearchTree()
            self._right = BinarySearchTree()
        else:
            # Base case: if the key is in the root, replace the value.
            if the_key == self._key:
                self._value = the_value
            # Reduction step: choose the appropriate subtree.
            # Recursive step: add/replace the key-value pair there.
            # Inductive step: nothing to do
            elif the_key < self._key:
                self._left.add(the_key, the_value)
            else:
                self._right.add(the_key, the_value)

    def remove(self, the_key):
        """Remove the node with the_key from the tree. Return nothing.

        Do nothing if the tree hasn't the_key.
        """
        # Base case: the tree is empty.
        if self.is_empty():
            return
        # pylint: disable=protected-access
        left_tree = self._left
        right_tree = self._right
        # Base case: the key is in the root node.
        if the_key == self._key:
            # If both subtrees are empty, removing the root empties the tree.
            if left_tree.is_empty() and right_tree.is_empty():
                self._key = None
                self._value = None
                self._left = None
                self._right = None
            # If the tree has only one subtree, that's the new tree.
            elif left_tree.is_empty():
                self._key = right_tree._key
                self._value = right_tree._value
                self._left = right_tree._left
                self._right = right_tree._right
            elif right_tree.is_empty():
                self._key = left_tree._key
                self._value = left_tree._value
                self._left = left_tree._left
                self._right = left_tree._right
            # If the tree has two non-empty subtrees,
            # replace the root by its successor, with the next higher key,
            # which is the smallest node in the right subtree.
            else:
                self._key = right_tree.smallest_key()
                self._value = right_tree.value(self._key)
                right_tree.remove(self._key)
        # Reduction step: choose the appropriate subtree.
        # Recursive step: delete the node from that subtree.
        # Inductive step: nothing to do.
        elif the_key < self._key:
            left_tree.remove(the_key)
        else:
            right_tree.remove(the_key)


# Exercises
# ---------
# - Write `smallest_key()` in an iterative way.
# - Add a method `__len__` that returns the number of nodes.
