"""A pedagogical implementation of binary search trees (BSTs).

A BST is a binary tree in which every node is a key-value pair,
every key in the left subtree is smaller than the root's key,
and every key in the right subtree is larger than the root's key.

"""

# Representation
# --------------
# The empty BST is represented by the Python value `None`.
# A non-empty BST is represented by a list with 3 items:
# the root node, the left subtree, the right subtree.
# Each node is represented by a Python list with 2 items:
# the key and the value.
# For example, a BST with a single node
# with key `"Mary"` and value `"female"` is represented as
# `[["Mary", "female"], None, None]`.

# The following auxiliary functions make the rest of the code more readable.


def root(tree):
    """Return the root node of the non-empty tree."""
    return tree[0]


def left(tree):
    """Return the left subtree of the non-empty tree."""
    return tree[1]


def right(tree):
    """Return the right subtree of the non-empty tree."""
    return tree[2]


def key(node):
    """Return the key of the node."""
    return node[0]


def value(node):
    """Return the value of the node."""
    return node[1]

# Creator
# -------


def empty():
    """Return the empty binary search tree."""
    return None


# Inspectors
# ----------

# The following function is needed later, but can be useful on its own.
# It is the equivalent of findinding the minimum in a list.


def smallest(tree):
    """Return the node with the smallest key in the non-empty tree."""
    # Base case: if there's no left subtree, the smallest key is in the root.
    if left(tree) is empty():
        node = root(tree)
    else:
        # Reduction step: only consider the left subtree.
        # Recursive step: find the smallest key in the left subtree.
        # Inductive step: not needed.
        node = smallest(left(tree))
    return node


# For BSTs, only the inorder traversal makes sense.


def sorted_keys(tree):
    """Return a string with the keys in sorted order."""
    if tree is empty():
        return ""
    result = sorted_keys(left(tree))
    result = result + str(key(root(tree))) + " "
    result = result + sorted_keys(right(tree))
    return result


def get(tree, the_key):
    """
    If tree has the_key, return the associated value, otherwise return None.
    """
    # This is essentially a decision problem, that returns the value or None,
    # instead of True/False. There are two bases cases, one for each outcome.
    # Base case: if the tree is empty, the key wasn't found.
    if tree is empty():
        the_value = None
    # Base case: if the key is in the root, return associated value.
    elif the_key == key(root(tree)):
        the_value = value(root(tree))
    # Reduction step: choose the appropriate subtree.
    # Recursive step: get the value in that subtree.
    # Inductive step: not needed.
    elif the_key < key(root(tree)):
        the_value = get(left(tree), the_key)
    else:
        the_value = get(right(tree), the_key)
    return the_value


# Modifiers
# ---------


def put(tree, the_key, the_value):
    """
    If tree has the_key, replace its associated value by the_value.
    If it hasn't, add a new node with the_key and the_value.
    In either case, return the new tree.
    Raise a ValueError if the_value is None.
    """
    # None can't be used as a value because
    # it's used by `get()` to represent the absence of key.
    if the_value is None:
        raise ValueError("value can't be None")
    # Base case: if the tree is empty, create one with the key-value pair.
    if tree is empty():
        the_root = [the_key, the_value]
        left_tree = empty()
        right_tree = empty()
    else:
        the_root = root(tree)
        left_tree = left(tree)
        right_tree = right(tree)
        # Base case: if the key is in the root, replace the value.
        if the_key == key(the_root):
            the_root = (the_key, the_value)
        # Reduction step: choose the appropriate subtree.
        # Recursive step: add/replace the key-value pair in that subtree.
        elif the_key < key(the_root):
            left_tree = put(left_tree, the_key, the_value)
        else:
            right_tree = put(right_tree, the_key, the_value)
    # Inductive step: put the new tree together from its parts.
    return [the_root, left_tree, right_tree]


def delete(tree, the_key):
    """Delete the node with the_key from tree and return the modified tree."""
    # Base case: if the tree is empty (key not found), don't modify it.
    if tree is empty():
        return tree

    the_root = root(tree)
    left_tree = left(tree)
    right_tree = right(tree)
    if the_key == key(the_root):
        # Base case: found the key, delete the root node.
        # If the tree has only one subtree, that's the new tree.
        if left_tree is empty():
            return right_tree
        elif right_tree is empty():
            return left_tree
        else:
            # If root has two non-empty subtrees,
            # replace the root by its successor,
            # which is the smallest node in the right subtree.
            the_root = smallest(right_tree)
            right_tree = delete(right_tree, key(the_root))
    # Reduction step: choose the appropriate subtree.
    # Recursive step: delete the node from that subtree.
    elif the_key < key(the_root):
        left_tree = delete(left_tree, the_key)
    else:
        right_tree = delete(right_tree, the_key)
    # Inductive step: put the new tree together from its parts.
    return [the_root, left_tree, right_tree]


# Tests
# -----
# Run tests if this file is executed, instead of imported.
if __name__ == "__main__":
    # First scenario: string keys and values
    bst = empty()
    key1 = "Mary"
    value1 = "female"
    key2 = "John"
    value2 = "male"
    # Add the larger key first and try to get it back
    bst = put(bst, key1, value1)
    the_value = get(bst, key1)
    if the_value != value1:
        print("get(", bst, ",", key1, ") is", the_value, "instead of", value1)
    # Add the smaller key next and retrieve it with `smallest()`
    bst = put(bst, key2, value2)
    the_value = value(smallest(bst))
    if the_value != value2:
        print("value(smallest(", bst, ")) is", the_value, "instead of", value2)
    # Replace the values and retrieve them
    value1 = "sister"
    value2 = "brother"
    bst = put(bst, key1, value1)
    the_value = get(bst, key1)
    if the_value != value1:
        print("get(", bst, ",", key1, ") is", the_value, "instead of", value1)
    bst = put(bst, key2, value2)
    the_value = get(bst, key2)
    if the_value != value2:
        print("get(", bst, ",", key2, ") is", the_value, "instead of", value2)
    # Delete the smaller key. The smallest key is now the first one.
    bst = delete(bst, key2)
    the_value = value(smallest(bst))
    if the_value != value1:
        print("value(smallest(", bst, ")) is", the_value, "instead of", value1)
    # Delete the only node, the tree should be empty again.
    bst = delete(bst, key1)
    if bst is not empty():
        print("the bst is", bst, "instead of empty:", empty())

    # Another test, with numeric keys and irrelevant values.
    bst = empty()
    keys = [4, 2, 6, 0, 2, 4, 9]
    for the_key in keys:
        bst = put(bst, the_key, "")
    # Test if the keys are in the right order.
    expected = "0 2 4 6 9 "
    result = sorted_keys(bst)
    if result != expected:
        print("sorted_keys(", bst, ") is", result, "instead of", expected)
    # Test the value for existing and non-existing keys.
    for the_key in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        the_value = get(bst, the_key)
        if the_key in keys and the_value != "":
            print("get(", bst, ",", the_key, ") is",
                  the_value, "instead of ''")
        if the_key not in keys and the_value is not None:
            print("get(", bst, ",", the_key, ") is",
                  the_value, "instead of None")
    # Test the smallest key is found.
    the_key = key(smallest(bst))
    if the_key != min(keys):
        print("key(smallest(", bst, ")) is", the_key, "instead of", min(keys))
    # Delete a node without children, i.e. a leaf.
    bst = delete(bst, 0)
    the_value = get(bst, 0)
    if the_value is not None:
        print("get(", bst, ", 0) is", the_value, "instead of None")
    # Delete a node with one child
    bst = delete(bst, 6)
    the_value = get(bst, 6)
    if the_value is not None:
        print("get(", bst, ", 6) is", the_value, "instead of None")
    # The tree should now have root 4 with left child 2 and right child 9
    the_key = key(root(bst))
    if the_key != 4:
        print("root of", bst, "is", the_key, "instead of 4")
    the_key = key(root(left(bst)))
    if the_key != 2:
        print("left child of", bst, "is", the_key, "instead of 2")
    the_key = key(root(right(bst)))
    if the_key != 9:
        print("right child of", bst, "is", the_key, "instead of 9")
    # Delete a node with two children: its successor is new root
    bst = delete(bst, 4)
    the_key = key(root(bst))
    if the_key != 9:
        print("root of", bst, "is", the_key, "instead of 9")


# Exercises
# ---------
# - Write `smallest()` in an iterative way.
# - Write a function that returns the height of a BST.
# - Write a function that returns the size of a BST, i.e. the number of nodes.
