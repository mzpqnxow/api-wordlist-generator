#!/bin/bash
#
# Example usage as a wordlist generator from a Python project source tree
# Zope2 is used in this example
#
# (C) 2018 copyright@mzpqnxow.com BSD 3-Caluse License
#
PYTHON_APP_PATH=~/Zope/src
for x in $(find $PYTHON_APP_PATH -name \*.py)
do
  ./parse.py -i "$x"
done
