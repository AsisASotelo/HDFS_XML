#!/usr/bin/env python3
# Asis A Sotelo
# April 27, 2020

# index.py

import sys
from lxml import etree
import json
import argparse



# Argument Parser for Command Line Input takes in FSIMAGE
# file name and INDEX file output file name

parser = argparse.ArgumentParser()
parser.add_argument("filenames", nargs = "*",  help = "file path of first comma seperated file")
args = parser.parse_args()
argArray= args.filenames


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

# Utility function to flatten a list of list

flatten = lambda l: [item for sublist in l for item in sublist]

class Inverter:

    

    def __init__(self, fileName):
        self.fileName = fileName
        self.flatTokenList = []
        self.tree = []

    def parseXml(self):
        with open(self.fileName) as xmlFile:
            self.tree= etree.parse(xmlFile)
    
    def tokenCreator(self):
        elem_list=[]
        for element in self.tree.xpath("//INodeSection/inode/name"):
            if(element.text):
                elem_list.append(element.text.replace(".txt","").replace(".xml",""))
        token_list = [sub.replace('-',' ').split(' ') for sub in elem_list]
        self.flatTokenList = set(flatten(token_list))
                
    def xmlWriter(self):
        i=0
        index_root=etree.Element("index")
        for token in self.flatTokenList:
            postings = index_root.append(etree.Element("postings"))
            postings = index_root[i]
            etree.SubElement(postings, "name").text = token
            i = i+1
            j=0
            for element in self.tree.xpath("//INodeSection/inode[contains(name,'{}')]/id".format(token)):
                etree.SubElement(postings, "inumber").text = element.text
        
        with open("Inverted-{}".format(self.fileName), 'wb') as doc:
            doc.write(etree.tostring(index_root, pretty_print = True))
    

def main():

    for entry in argArray:
        inverter = Inverter(entry)
        inverter.parseXml()
        inverter.tokenCreator()
        inverter.xmlWriter()



if __name__ == "__main__":
    main()
