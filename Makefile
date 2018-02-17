TESTFILE=$(CURDIR)/testfiles/testfile.exe
.PHONY: run
run:
	python3 pereader.py $(TESTFILE)
