"""Examples of using a binary search tree."""

from bst import BinarySearchTree

# A simple reverse lookup phone directory can be implemented as a BST:
# the keys are the unique phone numbers, the values are the names of people.
# The phone numbers are represented as strings to include leading zeros.


def test_presence(the_directory, the_phone, the_owner):
    """Test that the_owner is associated to the_phone in the_directory.

    If it is, do nothing, otherwise print an error message.
    """
    owner = the_directory.value(the_phone)
    if owner is None:
        print()
        print('Directory should have', the_phone)
    elif owner != the_owner:
        print()
        print('Expected owner', the_owner, 'but obtained', owner)


def test_absence(the_directory, the_phone):
    """Test that the_directory does not include the_phone.

    If it does, print an error message, otherwise do nothing.
    """
    if the_directory.has(the_phone):
        print()
        print('Directory should not have', the_phone)


def test_traversal(traversal, actual_order, expected_order):
    """Test if the actual_order matches the expected_order.

    If it does, do nothing, otherwise print an error message.
    Assume both traversals are lists of keys.
    """
    if actual_order != expected_order:
        print()
        print(traversal, 'should be', expected_order, ', not', actual_order)


def test_directory(the_directory):
    """Test that the_directory is working correctly.

    Add and remove entries from the_directory and search the directory,
    to confirm the operations work as expected.
    If they don't, print error messages.
    """
    phone1 = '00441908123456'
    owner1 = 'John Smith'
    the_directory.add(phone1, owner1)
    phone2 = '00441234567890'
    owner2 = 'ACME Corp.'
    the_directory.add(phone2, owner2)
    phone3 = '09876543210'
    the_directory.add(phone3, owner1)  # different key, same value
    # Get entries in different order than they were added
    test_presence(the_directory, phone2, owner2)
    test_presence(the_directory, phone3, owner1)
    test_presence(the_directory, phone1, owner1)
    # Test a similar but non-existent key
    test_absence(the_directory, '09786543210')
    # Test entries are sorted
    test_traversal('inorder',
                   the_directory.in_order(),
                   [phone2, phone1, phone3])
    # Reassign a phone number
    owner2 = 'Wonka Industries'
    the_directory.add(phone2, owner2)
    test_presence(the_directory, phone2, owner2)
    # Test entries are still sorted
    test_traversal('inorder',
                   the_directory.in_order(),
                   [phone2, phone1, phone3])
    # Remove an entry
    the_directory.remove(phone1)
    test_absence(the_directory, phone1)
    # The others can still be found
    test_presence(the_directory, phone2, owner2)
    test_presence(the_directory, phone3, owner1)
    # and are sorted
    test_traversal('inorder',
                   the_directory.in_order(),
                   [phone2, phone3])


directory = BinarySearchTree()
test_directory(directory)
