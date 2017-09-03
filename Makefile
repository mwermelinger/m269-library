.SILENT:
	
all: doc/*.html examples/*.py test clean

usage:
	echo "make clean	remove unnecessary files"
	echo "make test		run all unit tests in ./tests"
	echo "make new		process new source files in ./lib"
	echo "make -n		show what commands would be executed"

doc/%.html: lib/%.py
# Check for syntax errors. Compile as module to add this directory to path.
	python -m lib.$*
# Run the corresponding tests if they exist.
	if [ -f tests/$*.py ]; then python -m tests.$*; fi
# Fix any spacing issues.
	autopep8 --in-place --aggressive $<
# Check the code.
	pylint $<
	flake8 $<
# Check the docstrings.
	pydocstyle $<				
# Write the help text to an HTML file in this directory.
	pydoc -w lib.$*
# Remove my local path of the generated file.
# Edit the file in place without doing a backup.
	sed -e 's|<font.*file:.*/font>||' -i '' lib.$*.html
	mv lib.$*.html help/$*.html
# Generate the side-by-side view of code and comments.
	pycco -d doc $< 				

test:
# Discover and run all unit tests in the tests folder.
# Don't generate binaries.
# Unclear why the tests package has to be specified explicitly.
	python -B -m unittest discover tests

examples/%.py: FORCE
# Check the example compiles and works.
	export PYTHONPATH=.
	python -B $@
# Test the example using the docstring.
	python -B -m doctest $@
# Check the coding and commenting style.
	autopep8 --in-place --aggressive $@
	pylint $@
	flake8 $@
	pydocstyle $@

FORCE:

new:
	for f in lib/*py; do make doc/`basename $$f .py`.html; done
		
clean:
	rm -r lib/__pycache__

