#!/bin/bash

SHELL := /bin/bash

setup:
	pip3 install --user twine cookiecutter

build: clean
	python3 tasks.py build

clean:
	python3 tasks.py clean

test:
	python3 tasks.py test
