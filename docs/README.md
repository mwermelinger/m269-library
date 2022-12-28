This library provides Python implementations of some
commonly taught algorithms and data structures (see below).
It was created for M269, the Open University's
module on [Algorithms, Data Structures and Computability](http://www.open.ac.uk/courses/modules/m269),
but is not specific to M269.

The library aims to be pedagogical: simple, readable and documented.
It is meant to complement (not replace) the code
given in M269 and its textbook,
to emphasise that there are many ways of implementing
the same algorithms and data structures.

The code aims to follow the official Python coding style,
defined in [PEP8](http://pep8.org)
and [PEP257](https://www.python.org/dev/peps/pep-0257/).
In addition, the code only uses full English words in identifiers,
i.e. no abbreviations or single letters.
The exceptions are: `n`, `x`, `y`, `z`.

## Contents

The library implements the following:

- bubble, insertion, selection, quick and merge sort ([documentation](http://mwermelinger.github.io/m269-library/api/sort.html), [commented code](http://mwermelinger.github.io/m269-library/code/sort.html))
- stack ([documentation](http://mwermelinger.github.io/m269-library/api/stack.html), [commented code](http://mwermelinger.github.io/m269-library/code/stack.html))
- queue ([documentation](http://mwermelinger.github.io/m269-library/api/queue.html), [commented code](http://mwermelinger.github.io/m269-library/code/queue.html))
- priority queue ([documentation](http://mwermelinger.github.io/m269-library/api/priority_queue.html), [commented code](http://mwermelinger.github.io/m269-library/code/priority_queue.html))
- deque (double-ended queue) ([documentation](http://mwermelinger.github.io/m269-library/api/deque.html), [commented code](http://mwermelinger.github.io/m269-library/code/deque.html))
- binary search trees ([documentation](http://mwermelinger.github.io/m269-library/api/bst.html), [commented code](http://mwermelinger.github.io/m269-library/code/bst.html))
- hash table ([documentation](http://mwermelinger.github.io/m269-library/api/hash_table.html), [commented code](http://mwermelinger.github.io/m269-library/code/hash_table.html))
- undirected graph (both weighted and unweighted) ([documentation](http://mwermelinger.github.io/m269-library/api/graph.html), [commented code](http://mwermelinger.github.io/m269-library/code/graph.html))
- directed graph (both weighted and unweighted) ([documentation](http://mwermelinger.github.io/m269-library/api/digraph.html), [commented code](http://mwermelinger.github.io/m269-library/code/digraph.html))

## Installation

Click on the button above to download all files as a single compressed archive.
Once on your disk, double-click it to extract the files,
if your web browser hasn't done so automatically.
This will create the M269 Library folder with these subfolders:

- `lib` contains the M269 Library
- `examples` contains simple 'apps' that use the library
- `docs/api` contains the documentation in HTML format
- `docs/code` shows the code side by side with the comments
- `tests` contains the test code.

## Usage

Put your Python file in the M269 Library folder,
i.e. 'above' the `lib` subfolder.
Start your program with, for example,
`from lib.stack import Stack` to use the stack data structure,
or `from lib.sort import bubble_sort` to use the bubble sort algorithm.

To see what algorithms and data structures are available,
open the HTML files in the `docs/api` subfolder.
You can get the same documentation in the Python shell
(if run from the M269 Library folder), by typing for example
```
>>> import lib.stack
>>> help(lib.stack)
```

There are some suggested exercises at the end of code files.
You're welcome to discuss them in the M269 forums and tutorials,
unless they are used in the assignments.
Please don't post solutions on any public site.

## Development

This library was created on Mac OS X with Python 3.6 (Anaconda distribution).
In December 2022 I created a virtual environment with the most recent versions:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```
The library should work on other platforms and with earlier Python versions,
but they weren't tested.

For each class `ADT` in file `lib/adt.py` there is (or will be)
a class `TestADT` in file `tests/test_adt.py`.
The `TestADT` class has one method `setUp` and
one or more methods `test_...`.
The `setUp` method creates the inputs used by the tests,
and each test method tests one method of the `ADT` class.

Python's built-in
[unittest](https://docs.python.org/3/library/unittest.html) framework
automatically runs each test method of each test class.
The `setUp` method is run before _each_ test method,
so that each test can change the inputs without influencing other tests.

For the example apps, tests are written in the docstrings
and checked with Python's built-in
[doctest](https://docs.python.org/3/library/doctest.html) framework.

The files in the `docs/api` folder were generated with
Python's built-in documentation generator
[pydoc](https://docs.python.org/3/library/pydoc.html).

The files in the `docs/code` folder were generated with
[Pycco](https://pycco-docs.github.io/pycco/).

The code was formatted with [black](https://black.readthedocs.io/en/stable/)
and checked with
[pylint](http://pylint.org) (using the configuration file `pylintrc`),
[flake8](http://flake8.pycqa.org/) and
[pydocstyle](http://www.pydocstyle.org/).
