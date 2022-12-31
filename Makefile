.SILENT:

all: test docs/html/*.html examples/*.py clean

usage:
	echo "make clean	remove unnecessary files"
	echo "make test		run all unit tests in ./tests"
	echo "make new		process new source files in ./lib"
	echo "make -n		show what commands would be executed"

docs/html/lib/lib.%.html: lib/%.py
# Check for syntax errors. Compile as module to add this directory to path.
	python -m lib.$*
	mypy $<
# Format the code.
	isort $<
	black $<
# Check the code.
	pylint $<
	flake8 $<
# Check the docstrings.
	pydocstyle $<

test:
# Discover and run all unit and docstring tests. Report their coverage.
	pytest -q --doctest-modules --cov=lib

# Run the examples from the current folder to find the lib module.
examples/%.py: export PYTHONPATH = .
examples/%.py: FORCE
# Check the example compiles and works.
	python -B $@
	mypy $@
# Format the code
	isort $@
	black $@
# Check the coding and commenting style.
	pylint $@
	flake8 $@
	pydocstyle $@

FORCE:

new:
	for f in lib/*py; do make docs/code/`basename $$f .py`.html; done

clean:
	rm -rf lib/__pycache__ tests/__pycache__ examples/__pycache__
