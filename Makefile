PWD :=$(shell pwd)
PYTHON=python
REQU= requests pyinstaller

.PHONY: zkNet.exe
zkNet.exe: venv
	source venv/bin/activate && \
	python make.py


.PHONY: run
run: venv
	source venv/bin/activate && \
	python gui.py


venv:
	mkdir venv	&& \
	$(PYTHON) -m venv venv/ && \
	source venv/bin/activate && \
	pip install $(REQU)


.PHONY: clean
clean: 
	rm -rf ./build ./dist *.spec __pycache__ ./venv
