# M269

This repository provides Python implementations of some of the 
algorithms and data structures taught in M269, the Open University's
module on [Algorithms, Data Structures and Computability](http://www.open.ac.uk/courses/modules/m269).

The code provided here aims to be pedagogical: simple, readable and documented.
It is meant to complement (not replace) the code given in M269 and its textbook,
to emphasise that there are many ways of implementing
the same algorithms and data structures.

The goal is to illustrate the main ideas behind the algorithms and data 
structures, not to provide the most efficient implementation. 
For example, code was often simplified by returning a new data structure 
(using additional memory) instead of modifying the given structure in-place. 
Also in the name of simplicity, 
most of the code is procedural instead of object-oriented. 

The `doc` folder contains, for each source file, one HTML file that
shows the code side by side with the documentation. 
The HTML files were generated with [Pycco](https://pycco-docs.github.io/pycco/).

The `help` folder contains the help files generated with 
[pydoc](https://docs.python.org/3/library/pydoc.html).
You can get the same documentation in the Python shell, by typing for example
```
>>> import sort
>>> help(sort)
```

To download all files as a single zip file, 
first click on the download icon (a cloud with a downward arrow) 
on the left sidebar, and then click on the link shown.

All the code was checked with
[pycodestyle](https://pycodestyle.readthedocs.io/en/latest/) against part of 
[PEP8](https://www.python.org/dev/peps/pep-0008/).

Contrary to M269, the code here uses underscores instead of camel case.

There are some suggested optional exercises at the end of code files.
You're welcome to discuss them in the M269 forums and tutorials.

(c) Copyright 2017 Michel Wermelinger. All Rights Reserved. 