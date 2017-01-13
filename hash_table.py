"""A pedagogical implementation of hash tables.

This implements a closed hash table that doesn't grow and that
uses linear probing for collision resolution.
"""

# Representation
# --------------
# A hash table is represented by a fixed size list,
# each item being a key-value pair, represented by a list of length 2.
# An empty slot in the hash table is represented by the item None,
# whereas a deleted item is represented by a pair key-None.

# The following auxiliary functions make the rest of the code more readable.


def key(item):
    """Return the key of the item."""
    return item[0]


def value(item):
    """Return the value of the item."""
    return item[1]


def is_empty(item):
    """Return True if the item is empty, otherwise False."""
    return item is None


def deleted(item):
    """Return True if the item was previously deleted, otherwise False."""
    if is_empty(item):
        return False
    else:
        return value(item) is None


# Hashing
# -------
# The following are examples of hashing functions.
# They are written independently of the hash table size.


def hash_string(the_key):
    """Return a hash value for the string the_key."""
    sum = 0
    for character in the_key:
        # Convert each character to its ordinal number with a Python function.
        sum = sum + ord(character)
    return sum


# The following function returns a hash value in the range 0 to 999.
# It has to be modified if the table size is greater than 1000.


def mid_square(the_key):
    """
    Square the integer the_key and return its 3 middle digits.
    """
    # Square the number and convert to a string with a Python function.
    square = str(the_key * the_key)
    digits = len(square)
    # If the square has up to 3 digits, use them all.
    if digits <= 3:
        middle = square
    # Otherwise use the 3 digits from before to after the middle.
    else:
        middle = square[digits // 2 - 1:digits // 2 + 2]
    # Convert the string back to an integer with a Python function.
    return int(middle)


# The following functions are used internally by the hash table operations.
# Python already has a `hash()` function, so we must use a different name.


def hash_value(the_key):
    """Return a hash value for the_key."""
    # Convert the_key to a string and hash it.
    # This allows to handle keys of any type.
    return hash_string(str(the_key))


def rehash_value(hash_value, n):
    """
    Return the n-th rehash value for the original hash_value.
    If n is 0, return the hash_value.
    Currently implements linear probing.
    """
    return hash_value + n


# Creator
# -------


def empty(size):
    """Return an empty hash table of the given size."""
    table = []
    for n in range(size):
        table.append(None)
    return table


# Inspectors
# ----------


def get(table, the_key):
    """
    If table has the_key, return the associated value, otherwise return None.
    """
    # Remember the first slot tried.
    start_slot = hash_value(the_key) % len(table)
    # The 'zero-th' attempt is the start_slot.
    attempt = 0
    slot = start_slot
    # Keep going until we know whether the key exists or not.
    while True:
        item = table[slot]
        # If the slot is empty, the key doesn't exist.
        if is_empty(item):
            return None
        # If the slot has the key, return the associated value.
        if key(item) == the_key:
            return value(item)
        # Otherwise try the next slot.
        attempt = attempt + 1
        slot = rehash_value(start_slot, attempt) % len(table)
        # If the search 'wrapped around', the key doesn't exist.
        if slot == start_slot:
            return None


# Modifiers
# ---------


def put(table, the_key, the_value):
    """
    If table has the_key, replace its associated value by the_value.
    If it hasn't, add a new item with the_key and the_value.
    Return True if the operation succeeded, otherwise False (e.g. full table).
    Raise a ValueError if the_value is None.
    """
    # None can't be used as a normal value because it marks deleted items.
    if the_value is None:
        raise ValueError("can't put None in hash table")
    # Remember the first slot tried.
    start_slot = hash_value(the_key) % len(table)
    # The 'zero-th' attempt is the start_slot.
    attempt = 0
    slot = start_slot
    # Keep trying until the operation succeeds or fails.
    while True:
        # If the slot is empty, deleted or has the_key, store the item there.
        item = table[slot]
        if is_empty(item) or deleted(item) or key(item) == the_key:
            table[slot] = [the_key, the_value]
            return True
        # Otherwise try the next slot.
        attempt = attempt + 1
        slot = rehash_value(start_slot, attempt) % len(table)
        # If the search 'wrapped around', the operation failed.
        if slot == start_slot:
            return False


def delete(table, the_key):
    """Delete the item with the_key, if there is one, otherwise do nothing."""
    # Remember the first slot tried.
    start_slot = hash_value(the_key) % len(table)
    # The 'zero-th' attempt is the start_slot.
    attempt = 0
    slot = start_slot
    # Keep going until we know whether the key exists or not.
    while True:
        item = table[slot]
        # If the slot is empty, the key doesn't exist, so do nothing.
        if is_empty(item):
            return
        # If the slot has the key, mark it as deleted and stop.
        if key(item) == the_key:
            table[slot] = [the_key, None]
            return
        # Otherwise try the next slot.
        attempt = attempt + 1
        slot = rehash_value(start_slot, attempt) % len(table)
        # If the search 'wrapped around', the key doesn't exist, we can stop.
        if slot == start_slot:
            return


# Tests
# -----
# Run tests if this file is executed, instead of imported.
# The tests need to be modified if the (re)hashing functions change.

if __name__ == "__main__":
    table = empty(3)
    # Fill the table.
    # Due to the particular hash function, all keys collide in slot 1.
    # Due to linear probing, this means that
    # Mary ends up in slot 1, iris in slot 2, Baloo in slot 0.
    keys = ["Mary", "iris", "Baloo"]
    values = ["person", "flower", "bear"]
    for index in range(len(keys)):
        put(table, keys[index], values[index])
    # Try to get each value back.
    for index in range(len(keys)):
        result = get(table, keys[index])
        if result != values[index]:
            print("get(", table, ",", keys[index], ") is",
                  result, "instead of", values[index])
    # The table is full, so another addition has to fail.
    if put(table, "Nemo", "fish"):
        print("Adding another item to", table, "should have failed.")
    # Removing iris from slot 2 should still allow to find Baloo in slot 0.
    delete(table, "iris")
    result = get(table, keys[2])
    if result != values[2]:
        print("get(", table, ",", keys[2], ") is",
              result, "instead of", values[2])
    # Retry adding Nemo.
    if not put(table, "Nemo", "fish"):
        print("Adding Nemo to", table, "should have succeeded.")
    if get(table, "Nemo") != "fish":
        print("Can't find Nemo in", table)
    # Deleting an item and adding it back should keep it in the same slot.
    item = table[0]
    the_key = key(item)
    the_value = value(item)
    delete(table, the_key)
    if get(table, the_key) == the_value:
        print(the_key, "wasn't deleted from", table)
    if not put(table, the_key, the_value):
        print("Adding", the_key, "to", table, "should have succeeded.")
    if key(table[0]) != the_key:
        print(the_key, "should be in slot 0 of", table)

# Exercise
# --------
# - If quadratic probing is used,
#   after putting Mary and iris in the empty table,
#   putting Baloo will fail. Why?
# - Implement quadratic probing and modify the tests.
# - Write a function that calculates the load factor of a table.
