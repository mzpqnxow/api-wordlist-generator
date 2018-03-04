#!/bin/bash
#
# Extract all method names from a directory containing Python code (deep search)
#
# Copyright 2018, 3-clause BSD license, copyright /at/ mzpqnxow.com
#
PATH_TO_PYTHON_CODE=venv/
find "$PATH_TO_PYTHON_CODE" -name \*.py -exec grep -Eo ' *def (.*) *\(' {} \; | sed -e 's/^ *def *//g' | cut -d '(' -f 1 | grep -v '^_' | grep -E -v '[=,\{}]' | sort -u > funcs.lst

