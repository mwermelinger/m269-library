"""Use a stack to check if brackets match correctly in a string."""

from lib.stack import Stack


def brackets_match(the_text):
    """Check if all brackets in the_text (a string) are correctly matched.

    Return True if they are, otherwise False.
    Only consider round and square brackets, i.e. () and [].
    """
    open_brackets = Stack()
    for character in the_text:
        if character == '(' or character == '[':
            open_brackets.push(character)
        if character == ')' or character == ']':
            if open_brackets.is_empty():
                return False
            if character == ')' and open_brackets.top() != '(':
                return False
            if character == ']' and open_brackets.top() != '[':
                return False
            open_brackets.pop()
    return open_brackets.is_empty()


def test_brackets(the_text, expected):
    """Check if the_text's brackets match or not, as expected.

    Print a message stating if the test passed (result is as expected),
    or failed (result is different from expected).
    """
    if brackets_match(the_text) != expected:
        print('FAILED:', the_text)
    else:
        print('OK:', the_text)


test_brackets('No brackets is OK.', True)
test_brackets('After ( and [ comes ] and )', True)
test_brackets('After ( and [ it cannot be ) and ]', False)
test_brackets('This ( has no closing bracket.', False)
test_brackets('This ] has no opening bracket.', False)
test_brackets('Snarks are rarely seen (according to Smith (1999))', True)

# Exercises
# ---------
# - If only one type of brackets has to be checked, is a stack needed?
#   If not, write and test a `parentheses_match` function.
# - Extend and test the `brackets_match` function to handle { and }.
# - Write and test a function that returns the first position with an error.
#   For example, for the string `'( not closed'` it should return 0.
#   Decide what position to return if the brackets are matched.
#   Then rewrite `brackets_match` to use the new function instead.
# - Write a function that returns the input string if the brackets match,
#   otherwise returns a corrected string.
#   For example, for the input `'(['` it may return `'([])'`.
