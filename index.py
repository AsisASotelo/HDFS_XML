#!/usr/bin/env python3
# Asis A Sotelo
# April 27, 2020

# index.py

import sys
from lxml import etree
import json



# Argument Parser for Command Line Input takes in FSIMAGE
# file name and INDEX file output file name



# Production of index file for names of files and dir
# Strings are assumed to be tokenized by white spaces

# Helper Function

def printf(elems,mode = 'node'):
    if mode == 'node':
        for elem in elems:
            print (etree.tostring(elem).decode('utf-8'))
    if mode == 'text':
        for elem in elems:
            print(elem.text)

        

def main():


if __name__ == "__main__":
    main()
