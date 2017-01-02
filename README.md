# M269

This repository provides Python implementations of some of the 
algorithms and data structures taught in M269, the Open University's
module on [Algorithms, Data Structures and Computability](http://www.open.ac.uk/courses/modules/m269).

These implementations aim to be pedagogical: simple, readable and documented.
The goal is to illustrate the main ideas behind the algorithms and data structures, not to provide the most efficient way
of implementing them. For example, code was often simplified by returning a new data structure (thus using additional memory) instead of modifying in-place the given structure. 
Also in the name of simplicity, most of the code is procedural instead of object-oriented. 

For each source code file, there is a corresponding HTML file that
shows the code side by side with the documentation. 
The HTML files were generated with [Pycco](https://pycco-docs.github.io/pycco/).

The `help` folder contains the help files generated with 
[pydoc](https://docs.python.org/3/library/pydoc.html).
You can get the same documentation in the Python shell, by typing for example
```
>>> import sort
>>> help(sort)
```

All the code was checked with
[pycodestyle](https://pycodestyle.readthedocs.io/en/latest/) against part of 
[PEP8](https://www.python.org/dev/peps/pep-0008/).

The contents of this repository is Copyright (c) 2017 Michel Wermelinger.