"""Examples of sorting lists."""

from lib.sort import bubble_sort, selection_sort, insertion_sort
from lib.sort import merge_sorted, quick_sorted, heap_sorted
from lib.sort import nth_smallest

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

def test_quickselect(n, expected, actual):
    """Check that the nth-smallest item is the same as the expected one."""
    if actual != expected:
        print('FAILED:', n, 'smallest', actual, 'instead of', expected)
                

examples = (
    # base cases
    [],
    [3],
    # already in ascending or descending order
    [-1, 3, 4],
    [4, 3, -1],
    # sorting strings
    ['hi', 'Jane'],
    # duplicate values
    ['ho', 'ho', 'ho'],
    [3, 2, 1, 1, 2, 3]
)

for example in examples:
    test_new_list(quick_sorted, 'Quick sort', example)
    test_new_list(merge_sorted, 'Merge sort', example)
    test_new_list(heap_sorted, 'Heap sort', example)
    # Make a copy of the example before sorting in-place
    test_in_place(bubble_sort, 'Bubble sort', example[:])
    test_in_place(selection_sort, 'Selection sort', example[:])
    test_in_place(insertion_sort, 'Insertion sort', example[:])
    n = len(example)
    # if n > 0:
    #     test_quickselect(1, nth_smallest(example, 1), min(example))
    #     test_quickselect(n, nth_smallest(example, n), max(example))
    if n > 1:
        half = n // 2
        test_quickselect(half, nth_smallest(example, half), sorted(example)[half - 1])
        