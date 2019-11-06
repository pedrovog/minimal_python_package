#!/bin/bash

SHELL := /bin/bash

build:
	echo "make build NOT IMPLEMENTED"

push:
	echo "make push NOT IMPLEMENTED"

install:
	python setup.py install

release:
	echo "make release NOT IMPLEMENTED"

clean:
    find . -name '*.pyc' -exec rm --force {} +
    find . -name '*.pyo' -exec rm --force {} +
    find . | grep -E "__pycache__|.pyc|.DS_Store$$" | xargs rm -rf

clean-build:
    rm --force --recursive build/
    rm --force --recursive dist/
    rm --force --recursive *.egg-info

clean-build:
	echo "make clean-build NOT IMPLEMENTED"

uninstall:
	echo "make uninstall NOT IMPLEMENTED"

test:
	echo "make test NOT IMPLEMENTED"

requirements:
	pip freeze > requirements.txt

docker-run:
	echo "make docker-run NOT IMPLEMENTED"

docker-build:
	echo "make docker-build NOT IMPLEMENTED"

docker-push:
	echo "make docker-push NOT IMPLEMENTED"
