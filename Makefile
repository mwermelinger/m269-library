all: doc/*.html

doc/%.html: %.py
# Compile the file and run included tests
	python $<					
# Check the code against PEP8
	pycodestyle $<				
# Generate the help page
	pydoc -w $(basename $<)		
	sed 's|<font.*mw.*/font>||' $(basename $<).html > help/$(basename $<).html
# Generate the side-by-side view of code and its documentation
	pycco -d doc $< 				
	
clean:
	rm -r __pycache__

