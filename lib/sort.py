"""Implementations of some algorithms related to sorting.

Each algorithm assumes a list of comparable items.
Functions ending in `_sort` change the list in place.
Functions ending in `_sorted` don't change the unsorted list,
and return a new sorted list.
This matches the Python built-in functions:
`items.sort()` sorts the list in-place, `sorted(items)` returns a new list.
"""

from .priority_queue import PriorityQueue  # needed for heapsort


def binary_search(items, item):
    """Return True if items includes the item, otherwise False.

    Assume the items are in non-decreasing order.
    Assume item and items are all of the same type.
    """
    first = 0
    last = len(items) - 1
    while first <= last:
        # Base case: the item is in the middle.
        middle = (first + last) // 2
        if items[middle] == item:
            return True
        # Reduction step: find the half where the item should be.
        elif items[middle] < item:
            # The item must be above the middle position.
            first = middle + 1
        else:
            # The item must be below the middle position.
            last = middle - 1
    # Base case: the search space is empty.
    return False

# Bubblesort
# ----------
# The key insight is to swap adjacent items that are in the wrong order,
# until no swaps are possible: at that point the items are sorted.
#
# The algorithm divides a list of items into
# a left part (initially all items) of still unsorted items,
# and a right part (initially empty) of already sorted items.
# In each iteration, the algorithm goes through the unsorted part and
# swaps adjacent items that are in the wrong order.
# This 'bubbles' the largest item up to the sorted part.


def bubble_sort(items):
    """Sort the list of items in place, in non-decreasing order.

    Use the bubble sort algorithm.
    """
    # To sort n items at most n-1 iterations are needed.
    for iteration in range(1, len(items)):
        swapped = False
        # Each iteration shrinks the unsorted part by one.
        # Go through the unsorted part.
        for current in range(0, len(items) - iteration):
            # Swap current and next item if they're in the wrong order.
            this_item = items[current]
            next_item = items[current + 1]
            if this_item > next_item:
                items[current] = next_item
                items[current + 1] = this_item
                swapped = True
        # If no swaps were necessary, the items are sorted.
        if not swapped:
            return


# Selection sort
# --------------
# This algorithm divides the items the other way round:
# a left part (initially empty) of already sorted items, and
# a right part (initially all items) of still unsorted items.
# In each iteration, it selects the smallest item in the unsorted part
# and adds it to the end of the sorted part.


def selection_sort(items):
    """Sort the list of items in place, in non-decreasing order.

    Use the selection sort algorithm.
    """
    # Initially the sorted part is empty.
    # So, the border between the sorted and unsorted parts
    # starts at 0. In each iteration, the border goes up,
    # as the sorted part grows and the unsorted one shrinks.
    for border in range(0, len(items) - 1):
        # Find the position of the smallest item from the border onwards.
        minimum = border
        for current in range(border + 1, len(items)):
            if items[current] < items[minimum]:
                minimum = current
        # Swap that item with the one at the border.
        temporary = items[border]
        items[border] = items[minimum]
        items[minimum] = temporary


# Insertion sort
# --------------
# Like selection sort, the list has a left sorted part that grows
# and a right unsorted part that shrinks.
# In each iteration, the next unsorted item is inserted into its correct
# position in the sorted part.


def insertion_sort(items):
    """Sort the list of items in place, in non-decreasing order.

    Use the insertion sort algorithm.
    """
    # Initially the sorted sublist has the first item (in position 0).
    # So, the border between the sorted and unsorted sublists
    # starts at 1. In each iteration, the border goes up,
    # as the sorted part grows and the unsorted one shrinks.
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


def merge_sorted(items):
    """Return a new list of all items, in non-decreasing order.

    Use the merge sort algorithm.
    """
    # Base cases: lists with zero or one items are already sorted.
    if len(items) < 2:
        return items[:]  # return a copy to keep the original untouched
    # Reduction step: split the list in two halves
    middle = len(items) // 2
    left_unsorted = items[:middle]
    right_unsorted = items[middle:]
    # Recursive step: sort each half.
    left_sorted = merge_sorted(left_unsorted)
    right_sorted = merge_sorted(right_unsorted)
    # Inductive step: merge the sorted halves.
    merged = []
    # While neither half is empty, move the smallest item
    # from its half to the merged list.
    while left_sorted and right_sorted:
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


def quick_sorted(items):
    """Return a list of all items, in non-decreasing order."""
    # Base case: the empty list is already sorted.
    if items == []:
        return []
    # Reduction step: take the first item (call it the pivot)
    # and put the remaining items in two partitions,
    # those smaller or equal than the pivot, and those greater.
    pivot = items[0]
    left_unsorted = []
    right_unsorted = []
    for index in range(1, len(items)):
        if items[index] <= pivot:
            left_unsorted.append(items[index])
        else:
            right_unsorted.append(items[index])
    # Recursive step: sort each of the partitions.
    left_sorted = quick_sorted(left_unsorted)
    right_sorted = quick_sorted(right_unsorted)
    # Inductive step: put the sorted partitions and the pivot
    # in the correct order.
    return left_sorted + [pivot] + right_sorted

# Heapsort
# --------
# This algorithm transforms the list of items into a min binary heap
# and then keeps taking the smallest item from the heap.


def heap_sorted(items):
    """Return a list of all items, in non-decreasing order."""
    result = []
    queue = PriorityQueue()
    for item in items:
        # Items are ordered by priority, so each item is its own priority.
        queue.enqueue(item, item)
    while not queue.is_empty():
        result.append(queue.dequeue())
    return result

# Quickselect
# -----------


def nth_smallest(items, n):
    """Return the n-th smallest of the items.

    For example, return the minimum if n is 1
    and the maximum if n is len(items).
    Don't change the order of the items.
    Assume n is an integer from 1 to len(items).
    """
    assert 1 <= n <= len(items)
    # Reduction step: take the first item (call it the pivot)
    # and put the remaining items in two partitions,
    # those smaller or equal than the pivot, and those greater.
    pivot = items[0]
    left_unsorted = []
    right_unsorted = []
    for index in range(1, len(items)):
        item = items[index]
        if item <= pivot:
            left_unsorted.append(item)
        else:
            right_unsorted.append(item)
    smaller_equal = len(left_unsorted)
    # Base case: the pivot is the n-th smallest number
    # if there are exactly n-1 items smaller or equal than the pivot.
    if smaller_equal == n - 1:
        return pivot
    # Recursive step:
    # If there are n or more items smaller or equal than the pivot,
    # the n-th smallest must be among them.
    if smaller_equal >= n:
        return nth_smallest(left_unsorted, n)
    # Recursive step:
    # Otherwise it's among the numbers larger than the pivot.
    # Discount the numbers up to and including the pivot.
    return nth_smallest(right_unsorted, n - (smaller_equal + 1))
    # Inductive step: none.

# Exercises
# ---------
# - Why must a list of length 1 also be a base case for merge sort?
# - In quicksort, could the items equal to the pivot be added
#   to the right instead of the left partition?
# - What needs to change in each function to sort in descending order?
# - Why doesn't the quickselect algorithm check for the typical base cases
#   (list with 0 or 1 item)?
