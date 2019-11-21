#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import shutil
import subprocess

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, 'cookiecutter.json')) as cookiecutter_template:
    cookiecutter = json.load(cookiecutter_template)

COOKIE = os.path.join(HERE, cookiecutter['app_name'])
REQUIREMENTS = os.path.join(COOKIE, 'requirements', 'dev.txt')

def build():
    '''
        Creates a python project based on cookiecutter.json template.
    '''
    os.system('cookiecutter {0} --no-input'.format(HERE))

def clean():
    '''
        Delete the folder structure created by the build process.
    '''
    if os.path.exists(COOKIE):
        shutil.rmtree(COOKIE)
        print('Removed {0}'.format(COOKIE))
    else:
        print('App directory does not exist. Skipping.')

if __name__ == '__main__':

    if len(sys.argv) != 2:        
        raise SystemExit('''How to use:
    tasks.py [build | clean | test]''')
    
    if sys.argv[1] == 'build':
        build()
        sys.exit(0)
    
    if sys.argv[1] == 'clean':
        clean()
        sys.exit(0)
