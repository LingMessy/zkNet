PWD :=$(shell pwd)
PYTHON=python
PIP=pip
REQU= requests pyinstaller

.PHONY: zkNet.exe
zkNet.exe:
	pyinstaller -F -w gui.py -n zkNet.exe

run:
	$(PYTHON) gui.py

.PHONY: getDevEnv
getDevEnv: 
	$(PIP) install $(REQU)


.PHONY: getDevEnv
cleanDevEnv: 
	$(PIP) remove $(REQU)


.PHONY: clean
clean: 
	rm -rf ./build ./dist zkNet.exe.spec __pycache__