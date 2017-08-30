"""Examples of sorting lists."""

from sort import bubble_sort, selection_sort, insertion_sort
from sort import merge_sorted, quick_sorted

# In Python, functions can take other functions as arguments.
# Here we pass a sorting function to the test functions.


def test_new_list(algorithm, name, items):
    """Test a sorting algorithm (a function) that returns a new list."""
    # Check against Python's sorting algorithm.
    expected = sorted(items)
    actual = algorithm(items)  # call the function on the list of items
    if actual != expected:
        print(name, 'FAILED:', actual, 'instead of', expected)


def test_in_place(algorithm, name, items):
    """Test a sorting algorithm (a function) that sorts in place."""
    expected = sorted(items)
    algorithm(items)
    if items != expected:
        print(name, 'FAILED:', items, 'instead of', expected)


examples = (
    # base cases
    [],
    [3],
    # already in ascending or descending order
    [-1, 3, 4],
    [4, 3, -1],
    # sorting strings
    ['hi', 'Jane']
)

for example in examples:
    test_new_list(quick_sorted, 'Quick sort', example)
    test_new_list(merge_sorted, 'Merge sort', example)
    # Make a copy of the example before sorting in-place
    test_in_place(bubble_sort, 'Bubble sort', example[:])
    test_in_place(selection_sort, 'Selection sort', example[:])
    test_in_place(insertion_sort, 'Insertion sort', example[:])
