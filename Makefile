PWD :=$(shell pwd)
PYTHON=python
PIP=pip
REQU= requests pyinstaller customtkinter

.PHONY: zkNet.exe
zkNet.exe:
	pyinstaller -F -w gui.py -n zkNet-oldGui.exe
	pyinstaller -F -w newGui.py -n zkNet.exe

.PHONY: run
run:
	$(PYTHON) newGui.py


.PHONY: runOldGui
runOldGui:
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