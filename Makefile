all: doc/*.html clean

doc/%.html: %.py
# Fix any spacing issues
	autopep8 --in-place $<
# Compile the file to check for syntax errors and run any tests
	python $<					
# Check the code with various tools
	pylint -rn --const-rgx='[a-z_][a-z0-9_]{2,30}' $<
	flake8 $<
	pydocstyle $<				
# Generate the help page
	pydoc -w $(basename $<)		
	sed 's|<font.*mw.*/font>||' $(basename $<).html > help/$(basename $<).html
# Generate the side-by-side view of code and its documentation
	pycco -d doc $< 				
	
clean:
	rm -r *html __pycache__
	

