all: 
	pip install PyQt5

pack:
	@echo TODO

clean:
	rmdir /Q /S __pycache__

test:
	python math_lib_test.py

doc:
	doxygen Doxyfile

run:
	python main.py

profile:
	python stddev.py <profiling_example_file.txt

help:	
	@echo make/ make all - install dependencies
	@echo pack           - pack needed files
	@echo make clean     - clean not needed files
	@echo make test      - start tests for math_library
	@echo make doc       - generate documentation wuth Doxygen
	@echo make run       - start program
	@echo make profile   - start code for standard deviation with example file
	@echo make help      - print make info for this program