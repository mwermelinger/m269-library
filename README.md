# The M269 Library

This repository provides Python implementations of some
commonly taught algorithms and data structures:
binary search, quicksort, binary search trees, graphs, etc.

This library was created for M269, the Open University's
module on [Algorithms, Data Structures and Computability](http://www.open.ac.uk/courses/modules/m269),
but is not specific to M269.

The code provided here aims to be pedagogical: simple, readable and documented.
It is meant to complement (not replace) the code given in M269 and its textbook,
to emphasise that there are many ways of implementing
the same algorithms and data structures.

The code aims to follow the official Python coding style,
defined in [PEP8](https://www.python.org/dev/peps/pep-0008/)
and [PEP257](https://www.python.org/dev/peps/pep-0257/).
The code was checked with [pycodestyle](https://pycodestyle.readthedocs.io/en/latest/)
which only covers some of the guidelines.
In addition, the code only uses full English words in identifiers, 
i.e. no abbreviations or single letters.

The `doc` folder contains, for each source file, an HTML file that
shows the code side by side with the comments. 
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

There are some suggested exercises at the end of code files.
You're welcome to discuss them in the M269 forums and tutorials,
unless they are used in the assignments.

## License

MIT License

Copyright (c) 2017 Michel Wermelinger

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
