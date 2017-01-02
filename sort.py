"""Pedagogical implementations of some sorting algorithms.

"""

# Bubblesort
# ----------
# The key insight is to swap adjacent items that are in the wrong order,
# until no swaps are possible: at that point the items are sorted.
# The following implementation uses a while-loop because
# Python has no repeat-until loop.


def bubble_sort(items):
    """Sort the list of items in place, in ascending order."""
    swapped = True
    # Keep going while at least one swap was done.
    while swapped:
        # Go through the whole list.
        swapped = False
        for current in range(0, len(items) - 1):
            # Swap current and next item if they're in the wrong order.
            if items[current] > items[current + 1]:
                temporary = items[current]
                items[current] = items[current + 1]
                items[current + 1] = temporary
                swapped = True


# Selection sort
# --------------
# The key insight is to see the list has having two parts,
# those already sorted in the left part (initially empty)
# and those still unsorted in the right part (initially the whole list).
# In each pass, select the smallest item of the unsorted part
# and put it at then end of the sorted part.


def selection_sort(items):
    """Sort the list of items in place, in ascending order."""
    # The border between the sorted and unsorted part moves up in each pass.
    for border in range(0, len(items) - 1):
        # Find the position of the smallest item from the border onwards.
        minimum = border
        for current in range(border, len(items)):
            if items[current] < items[minimum]:
                minimum = current
        # Swap that item with the one at the border.
        temporary = items[border]
        items[border] = items[minimum]
        items[minimum] = temporary


# Insertion sort
# --------------
# Like selection sort, the list has a sorted part that grows
# and an unsorted part that shrinks in each pass.
# In each pass, the next unsorted item is inserted into its correct
# position in the sorted part.


def insertion_sort(items):
    """Sort the list of items in place, in ascending order."""
    # The sorted part starts with the item that is in the first position.
    for border in range(1, len(items)):
        # The item at the border is the next item to sort.
        to_sort = items[border]
        # Find the position where to insert it.
        # If it is larger than all sorted items, it will stay at the border.
        position = border
        # Shift to the right all sorted items larger than the one to sort.
        while position > 0 and items[position - 1] > to_sort:
            items[position] = items[position - 1]
            position = position - 1
        # Put the item to sort at the found position.
        items[position] = to_sort

# Merge sort
# ----------
# The key insight is to split the unsorted list in two halves, sort each one,
# and then merge the sorted halves together by repeatedly taking the smallest
# item of both halves.


def merge_sort(unsorted):
    """Return a list of all items in list unsorted, in ascending order."""
    # Base cases: lists with zero or one items are already sorted.
    if len(unsorted) < 2:
        return unsorted
    # Reduction step: split the list in two halves
    middle = len(unsorted) // 2
    left_unsorted = unsorted[:middle]
    right_unsorted = unsorted[middle:]
    # Recursive step: sort each half.
    left_sorted = merge_sort(left_unsorted)
    right_sorted = merge_sort(right_unsorted)
    # Inductive step: merge the sorted halves.
    merged = []
    # While neither half is empty, move the smallest item
    # from its half to the merged list.
    while left_sorted != [] and right_sorted != []:
        if left_sorted[0] <= right_sorted[0]:
            merged.append(left_sorted[0])
            left_sorted = left_sorted[1:]
        else:
            merged.append(right_sorted[0])
            right_sorted = right_sorted[1:]
    # One or both halves are now empty. Add any remaining items.
    return merged + left_sorted + right_sorted


# Quicksort
# ---------
# This approach also splits the list in two, sorts each part,
# and puts the sorted parts together.
# Compared to mergesort, it puts more effort into the splitting,
# making the 'merging' trivial.
# The key insight is to pick an item and then split the list into those
# that are smaller or equal than the item and those that are larger.


def quicksort(unsorted):
    """
    Return a list of all items in list unsorted, in ascending order.
    """
    # Base case: the empty list is already sorted.
    if unsorted == []:
        return unsorted
    # Reduction step: take the first item (call it the pivot)
    # and put the remaining items in two partitions,
    # those smaller or equal than the pivot, and those greater.
    pivot = unsorted[0]
    left_unsorted = []
    right_unsorted = []
    for item in unsorted[1:]:
        if item <= pivot:
            left_unsorted.append(item)
        else:
            right_unsorted.append(item)
    # Recursive step: sort each of the partitions.
    left_sorted = quicksort(left_unsorted)
    right_sorted = quicksort(right_unsorted)
    # Inductive step: put the sorted partitions and the pivot
    # in the correct order.
    return left_sorted + [pivot] + right_sorted

# Tests
# -----
# A test is a pair made of an input and the corresponding expected output.
# Running a test is checking whether the actual and expected outputs match.
# All sorting algorithms do the same, so a single set of tests can be used.


def sort_tests():
    """Return a list of unsorted-sorted pairs to test a sorting algorithm."""
    return [
        # Test the base cases.
        [[], []],
        [[5], [5]],
        # Test an already sorted list.
        [[0, 1, 2, 3], [0, 1, 2, 3]],
        # Test a reversed list.
        [[3, 2, 1, 0], [0, 1, 2, 3]],
        # Test a list with duplicates.
        [[1, 2, 0, 2, 0], [0, 0, 1, 2, 2]],
        # Test a list with another type of items.
        [["hi", "Bob"], ["Bob", "hi"]]
    ]


def test_sort(sort, unsorted, expected):
    """
    Print an error message if sort(unsorted) is not the same as expected,
    otherwise do nothing.
    """
    if sort == quicksort or sort == merge_sort:
        result = sort(unsorted)
    else:
        # Make a copy of the input before sorting it in-place.
        result = unsorted[:]
        sort(result)
    if result != expected:
        if sort == bubble_sort:
            name = "Bubble sort"
        elif sort == selection_sort:
            name = "Selection sort"
        elif sort == insertion_sort:
            name = "Insertion sort"
        elif sort == merge_sort:
            name = "Merge sort"
        elif sort == quicksort:
            name = "Quicksort"
        print(name, "of", unsorted, "is", result, "instead of", expected)


# Run tests if this file is executed, instead of imported.
if __name__ == "__main__":
    for sort in [bubble_sort, selection_sort, insertion_sort,
                 merge_sort, quicksort]:
        for test in sort_tests():
            test_sort(sort, unsorted=test[0], expected=test[1])


# Exercises
# ---------
# - Why must a list of length 1 also be a base case for merge sort?
# - In quicksort, could the items equal to the pivot be added
#   to the right instead of the left partition?
# - What needs to change in each function to sort in descending order?
