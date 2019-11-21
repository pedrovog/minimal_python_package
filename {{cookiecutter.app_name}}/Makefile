#!/bin/bash

SHELL := /bin/bash

setup:
	echo "make setup NOT IMPLEMENTED"

build:
	python3 setup.py sdist bdist_wheel

install:
	python3 setup.py install

release: test
	twine upload -r internal dist/*

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . | grep -E "__pycache__|.pyc|.DS_Store$$" | xargs rm -rf

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

uninstall:
	echo "make uninstall NOT IMPLEMENTED"

test:
	pytest

requirements:
	pip freeze > requirements.txt

docker-run:
	echo "make docker-run NOT IMPLEMENTED"

docker-build:
	echo "make docker-build NOT IMPLEMENTED"

docker-push:
	echo "make docker-push NOT IMPLEMENTED"
