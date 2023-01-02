# Style guide

This document describes the code and documentation guidelines for this project.

## Code style

The code largely follows the
[Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
except that

- we write `dict()` instead of `{}` to avoid confusion with sets.

We use tools to automatically enforce or check most guidelines.

## Tests

For each file `lib/X.py` with
```python
class SomeClass:
    def method1(...) -> ...:
        ...

def function1(...) -> ...:
    ...
```
there's a corresponding `tests/test_X.py` file with
```python
class TestSomeClass:
    def test_method1(...):
        ...

def test_function1(...) -> ...:
```
Every test class is named `Test...` and every test method or function
is named `test_...` so that the testing framework can automatically
find and run all tests.

Test classes may have a `setup_method` method that creates the necessary
instance variables before each test is run.