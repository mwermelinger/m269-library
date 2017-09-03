# The M269 Library

This repository provides Python implementations of some
commonly taught algorithms and data structures:
binary search, quicksort, binary search trees, graphs, etc.

This library was created for M269, the Open University's
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

## Installation

Click on the download icon (a cloud with a downward arrow) 
on the left sidebar, then click on the link shown.
This will download all files as a single zip file.
Create a new empty working folder and extract the zip file there.
This will create these subfolders:

- `lib` contains the M269 Library
- `help` contains the documentation in HTML format
- `doc` shows the code side by side with the comments
- `tests` contains the test code.


## Usage

Your Python programs in the working folder can simply start with
`from lib.stack import Stack` to use the stack data structure,
or `from lib.sort import bubble_sort` to use the bubble sort algorithm.

To see what algorithms and data structures are available,
open the HTML files in the `help` folder.
You can get the same documentation in the Python shell, 
by typing for example
```
>>> import lib.stack
>>> help(lib.stack)
```

There are some suggested exercises at the end of code files.
You're welcome to discuss them in the M269 forums and tutorials,
unless they are used in the assignments.
Please don't post solutions on any public site.

## Development

This library was developed with Anaconda3 4.4.0 (Python 3.6) on Mac OS X.
It should work on other platforms and with earlier Python versions,
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

The files in the `help` folder were generated with 
Python's built-in documentation generator
[pydoc](https://docs.python.org/3/library/pydoc.html).

The files in the `doc` folder were generated with
[Pycco](https://pycco-docs.github.io/pycco/).

The code was checked with
[pylint](http://pylint.org) 1.6.4 
(using the configuration file `pylintrc`),
[flake8](http://flake8.pycqa.org/) 3.3.0 and
[pydocstyle](http://www.pydocstyle.org/) 2.0.0.
