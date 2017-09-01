all: doc/*.html clean

doc/%.html: lib/%.py
# Check for syntax errors. Compile as module to add this directory to path.
	python -m lib.$*
# Run the corresponding tests.
	python -m tests.$*
# Fix any spacing issues.
	autopep8 --in-place --aggressive $<
# Check the code.
	pylint $<
	flake8 $<
# Check the docstrings.
	pydocstyle $<				
# Write the help text to an HTML file in this directory.
	pydoc -w lib.$*
# Edit the file in place without doing a backup.
	sed -e 's|<font.*mw.*/font>||' -i '' lib.$*.html
	mv lib.$*.html help/$*.html
# Generate the side-by-side view of code and comments.
	pycco -d doc $< 				
	
rebuild: 
	for f in lib/*py; do make doc/`basename $$f .py`.html; done
	
clean:
	rm -r lib/__pycache__ tests/__pycache__

