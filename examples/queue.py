"""Use a queue to solve the Josephus problem.

Some people are standing in a circle, numbered from 1 to n.
Starting from 1, k people are skipped and the next one is eliminated.
This process continues, always with the same k,
starting from the person after the eliminated one.
What is the initial position of the last person standing?

More details of the problem and its mathematical solution are on Wikipedia.
This program solves the problem by simulation.
"""

from lib.queue import Queue


def eliminated(people, skip):
    """Return a list of the positions of people as they are eliminated.

    The position of the last person standing is at the end of the list.
    Assume people is a positive integer.
    Assume skip is a non-negative integer.
    For example:

    >>> eliminated(3, 0)
    [1, 2, 3]
    >>> eliminated(3, 1)
    [2, 1, 3]
    >>> eliminated(3, 4)
    [2, 3, 1]
    """
    assert people > 0
    assert skip >= 0
    circle = Queue()
    for position in range(1, people + 1):
        circle.enqueue(position)
    positions = []
    while circle:
        for _skipped in range(skip):
            circle.enqueue(circle.dequeue())
        positions.append(circle.dequeue())
    return positions


# If this file is imported, do nothing.
# If it is run as a script, execute the app.
if __name__ == "__main__":
    circle_size = int(input("How many people in the circle? "))
    to_skip = int(input("How many people to skip? "))
    last = eliminated(circle_size, to_skip)[-1]
    print("The last person standing is", last)
