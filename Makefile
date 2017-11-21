OS = Linux

VERSION = 0.0.1

CURDIR = $(shell pwd)
SOURCEDIR = $(CURDIR)
PYTHON = python

ECHO = echo

test:
	./test.sh

help:
	@$(ECHO) "test    - perform all test"
