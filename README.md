[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![imports: isort](https://img.shields.io/badge/imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![code style: black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)
![license: MIT](https://img.shields.io/github/license/mwermelinger/m269-library)

This library provides Python implementations of some
commonly taught algorithms and data structures (see the sidebar).
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

## Installation

Make sure you have Python version 3.9 or higher.

Go to the [code repository](https://github.com/mwermelinger/m269-library) and
click on the green 'Code' button to download all files as a single compressed archive.
Once downloaded, double-click the archive to extract the files,
if your web browser hasn't done so automatically.
This will create the M269 Library folder with these subfolders:

- `lib` contains the M269 Library
- `examples` contains simple applications that use the library
- `docs` contains this documentation in HTML format
- `tests` contains the test code.

## Usage

Put your Python file in the M269 Library folder,
i.e. 'above' the `lib` subfolder.
Start your program with, for example,
`from lib.stack import Stack` to use the stack data structure,
or `from lib.sort import bubble_sort` to use the bubble sort algorithm.

You can browse this documentation on your computer by opening file `docs/index.html`.
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
Due to the type annotations, the library requires at least Python 3.9.
The library should work on other platforms but they weren't tested.

For each class `ADT` in file `lib/adt.py` there is (or will be)
a class `TestADT` in file `tests/test_adt.py`.
The `TestADT` class has one method `setUp` and
one or more methods `test_...`, following the
[unittest](https://docs.python.org/3/library/unittest.html) framework.
The `setUp` method creates the inputs used by the tests,
and each test method tests one method of the `ADT` class.
The `setUp` method is run before _each_ test method,
so that each test can change the inputs without influencing other tests.

For the example apps, tests follow the
[doctest](https://docs.python.org/3/library/doctest.html) framework.
Both unit and doc tests are run with [pytest](https://docs.pytest.org).

The documentation is generated with [sphinx](http://sphinx-doc.org),
using the `sphinx-apidoc` script to generate an initial set of pages,
one per library or example file, in the `docsrc` folder.
The `sphinx-build` script then generates the HTML files in the `docs` folder,
which is rendered with [GitHub Pages](https://docs.github.com/en/pages/quickstart).

The code was formatted with [black](https://black.readthedocs.io/en/stable/)
and [isort](https://pycqa.github.io/isort/) and checked with
[pylint](http://pylint.org), [flake8](http://flake8.pycqa.org/) and
[pydocstyle](http://www.pydocstyle.org/).
File `pyproject.toml` configures the tools.
