# check a library file

# adapted from https://stackoverflow.com/questions/18568706
if [[ $# -ne 1 ]]; then
    echo "usage: ./check.sh <module>" >&2
    echo "For example ./check.sh bst to check lib/bst.py" >&2
    exit 2
fi

set -e                          # stop after the first check that fails
python -m lib.$1                # check for syntax errors
                                # compile as module to add this folder to path
pytest -q tests/test_$1.py      # run tests to check functionality
mypy --strict lib/$1.py         # check the types
isort lib/$1.py                 # put import statements in the right order
black lib/$1.py                 # format the code
pylint lib/$1.py                # check the code style
flake8 lib/$1.py                # further checks
pydocstyle lib/$1.py            # check the docstrings
