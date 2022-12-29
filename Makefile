.SILENT:

all: docs/code/*.html examples/*.py test clean

usage:
	echo "make clean	remove unnecessary files"
	echo "make test		run all unit tests in ./tests"
	echo "make new		process new source files in ./lib"
	echo "make -n		show what commands would be executed"

docs/code/%.html: lib/%.py
# Check for syntax errors. Compile as module to add this directory to path.
	python -m lib.$*
# Run the corresponding tests if they exist.
	if [ -f tests/$*.py ]; then python -m tests.$*; fi
# Format the code.
	isort $<
	black $<
# Fix any spacing issues.
	autopep8 --in-place --aggressive $<
# Check the code.
	pylint $<
	flake8 $<
# Check the docstrings.
	pydocstyle $<
# Write the help text to an HTML file in this directory.
	pydoc3 -w lib.$*
# Remove my local path of the generated file.
# Edit the file in place without doing a backup.
	sed -e 's|<font.*file:.*/font>||' -i '' lib.$*.html
	mv lib.$*.html docs/api/$*.html
# Generate the side-by-side view of code and comments.
	pycco -d docs/code $<

test:
# Discover and run all unit and doctests. Report their coverage.
	pytest -q --doctest-modules --cov=lib

# Run the examples from the current folder to find the lib module.
examples/%.py: export PYTHONPATH = .
examples/%.py: FORCE
# Check the example compiles and works.
	python -B $@
# Format the code
	isort $@
	black $@
# Check the coding and commenting style.
	autopep8 --in-place --aggressive $@
	pylint $@
	flake8 $@
	pydocstyle $@

FORCE:

new:
	for f in lib/*py; do make docs/code/`basename $$f .py`.html; done

clean:
	rm -rf lib/__pycache__ tests/__pycache__ examples/__pycache__
