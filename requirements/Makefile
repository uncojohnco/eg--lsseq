# https://jamescooke.info/a-successful-pip-tools-workflow-for-managing-python-package-requirements.html

.PHONY: all check clean

objects = $(wildcard *.in)
outputs := $(objects:.in=.txt)

all: $(outputs)

%.txt: %.in
	pip-compile -v --output-file $@ $<

test.txt: base.txt
dev.txt: test.txt

check:
	@which pip-compile > /dev/null

clean: check
	- rm *.txt
