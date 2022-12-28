"""Use a stack to check if brackets match correctly in a string."""

from lib.stack import Stack


def brackets_match(string):
    """Check if all brackets in the string are correctly matched.

    Return True if they are, otherwise False.
    Only consider round and square brackets, i.e. () and []. For example:

    >>> brackets_match("No brackets is fine")
    True
    >>> brackets_match("After ( and [ comes ] and )")
    True
    >>> brackets_match("After ( and [ it cannot be ) and ]")
    False
    >>> brackets_match("A ( without closing bracket")
    False
    >>> brackets_match("A ] without opening bracket")
    False
    >>> brackets_match("Snarks are rarely seen (according to Smith (1999)).")
    True
    """
    expected = Stack()
    for character in string:
        if character == "(":
            expected.push(")")
        elif character == "[":
            expected.push("]")
        elif character in ")]":
            if expected and character == expected.top():
                expected.pop()
            else:
                return False
    return expected.is_empty()


# If this file is imported, do nothing.
# If it is run as a script, execute the app.
if __name__ == "__main__":
    print("Type some text followed by ENTER to check if the brackets match.")
    print("Press only ENTER to terminate the program.")
    text = input("Text:")
    while text:
        if brackets_match(text):
            print("The brackets match.")
        else:
            print("The brackets don't match.")
        text = input("Text:")

# Exercises
# ---------
# - If only one type of brackets has to be checked, is a stack needed?
#   If not, write and test a `parentheses_match` function.
# - Extend and test the `brackets_match` function to handle { and }.
# - Write and test a function that returns the position
#   of the first wrong bracket, e.g. it should return 0 for `"( not closed"`.
#   Decide what position to return if the brackets are matched.
#   Then rewrite `brackets_match` to use the new function instead.
# - In many code editors, when the cursors is on a bracket,
#   the matching bracket is highlighted.
#   Write and test a function that, given a text and a position in that text,
#   returns the position of the matching bracket.
#   Decide what to return if there is no bracket at the given position
#   or if it has no matching bracket.
#   Think when the matching bracket comes before and when it comes after
#   the given position.
# - Write a function that returns the input string if the brackets match,
#   otherwise returns a corrected string.
#   For example, for the input `"(["` it may return `"([])"`.
#   You may wish to use the `in` operator to check if a matching bracket
#   comes further down in the stack.
