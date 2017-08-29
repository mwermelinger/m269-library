all: doc/*.html

doc/%.html: %.py
# Compile the file and run included tests
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
	

