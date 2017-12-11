OS = Linux

VERSION = 0.0.1

CURDIR = $(shell pwd)
SOURCEDIR = $(CURDIR)
PYTHON = python

ECHO = echo

all: test build

test:
	./test.sh
build:
	python build.py

help:
	@$(ECHO) "test    - perform all test"
	@$(ECHO) "build   - build index.html for gh-pages branch"
