"""An implementation of hash tables."""

# The following constants make the code more readable.

_KEY = 0    # pylint: disable=invalid-name
_VALUE = 1  # pylint: disable=invalid-name


class HashTable:
    """Provide a collection of key-value pairs with unique keys.

    Implement a closed hash table that doesn't grow.
    Use linear probing for collision resolution.
    Use the built-in hashing function.
    """

    # Representation
    # --------------
    # A hash table is represented by a fixed size list,
    # each item being a key-value pair, represented by a list of length 2.
    # An empty slot in the hash table is represented by the pair None-None,
    # whereas a deleted item is represented by a pair key-None.

    # Creator
    # -------

    def __init__(self, number_of_buckets):
        """Initialise the table with the given number_of_buckets.

        Assume that the number_of_buckets is positive.
        """
        assert number_of_buckets > 0
        self._buckets = [[None, None]] * number_of_buckets

    # Inspectors
    # ----------

    def __len__(self):
        """Implement the `len` function for hash tables.

        Return the number of key-value pairs in the hash table.
        """
        total = 0
        for bucket in self._buckets:
            if bucket[_VALUE] is not None:
                total += 1
        return total

    def value(self, the_key):
        """If the table has the_key, return the associated value.

        Otherwise return None.
        """
        # Remember the first bucket tried.
        start_index = hash(the_key) % len(self._buckets)
        index = start_index
        # Keep going until we know whether the key exists or not.
        while True:
            bucket = self._buckets[index]
            # If the bucket is empty, the item doesn't exist.
            if bucket[_KEY] is None:
                return None
            # If the bucket has the key, return the value.
            if bucket[_KEY] == the_key:
                return bucket[_VALUE]
            # Otherwise try the next bucket.
            index = (index + 1) % len(self._buckets)
            # If the search 'wrapped around', the item doesn't exist.
            if index == start_index:
                return None

    def __contains__(self, the_key):
        """Implement the `in` operator for hash tables.

        Return True if the table has the_key, otherwise False.
        """
        return self.value(the_key) is not None

    # Modifiers
    # ---------

    def add(self, the_key, the_value):
        """Add an item to the table and return if the operation succeeded.

        If there is an item with the_key, replace its value by the_value,
        otherwise try to add a new item with the_key and the_value.
        Return True if the item was added.
        Return False if the_value is None or the table is full.
        """
        if the_value is None:
            return False
        start_index = hash(the_key) % len(self._buckets)
        index = start_index
        while True:
            bucket = self._buckets[index]
            # If the bucket is empty or has the_key, store the item there.
            if bucket[_KEY] is None or bucket[_KEY] == the_key:
                self._buckets[index] = [the_key, the_value]
                return True
            index = (index + 1) % len(self._buckets)
            # If the search 'wrapped around', the table is full.
            if index == start_index:
                return False

    def remove(self, the_key):
        """Remove the item with the_key from the table. Return nothing.

        Do nothing if there's no item with the_key.
        """
        start_index = hash(the_key) % len(self._buckets)
        index = start_index
        while True:
            bucket = self._buckets[index]
            # If the bucket is empty, the item doesn't exist.
            if bucket[_KEY] is None:
                return
            # If the bucket has the key, mark it as deleted.
            if bucket[_KEY] == the_key:
                bucket[_VALUE] = None
                return
            index = (index + 1) % len(self._buckets)
            if index == start_index:
                return

# Exercises
# ---------
# - Change the implementation to use quadratic probing.
# - Write a method that calculates the load factor of a table.
