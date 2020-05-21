#!/usr/bin/env python3
# Asis A Sotelo
# April 27, 2020

# search.py

import sys
from lxml import etree 
import json
import argparse

# Create an argparser object to handle command line arguments

parser = argparse.ArgumentParser()
parser.add_argument("arguments", nargs=2, help= "Enter key word")
args = parser.parse_args()
argArray = args.arguments

# Create a tree search class in order to search xml file created by the 
# invert.py

class Searcher:

    # Create an instance constructor, since the searcher will only have 
    # to search one file at a time
    
    def __init__(self, fileName):
        self.fileName=fileName
        self.tree=[]
    
    # Create a parser method using the lxml.etree method

    def parseXml(self):
        with open(self.fileName) as xmlFile:
            self.tree=etree.parse(xmlFile)
    
    # The following xpath selects the postings element and all of its childrend
    # with the predicate that the child "name" of "postings" contains the name 
    # the keyword. Since all of the name children are single words the keyword should
    # match if it exists. This will then print out all of the inumbers.

    # Added functionality for keyword that returns nothing.

    def search(self, keyword):
        print(type(self.tree.xpath("//postings[contains(name,{})]/inumber".format(keyword))))
        print(len(self.tree.xpath("//postings[contains(name,{})]/inumber".format(keyword))))

        i=0
        

        for element in self.tree.xpath("//postings[contains(name, '{}')]/inumber".format(keyword)):
            print(element.tag,element.text)
            i=1+i
        if i==0:
            print("Keyword Not in Index")
            
     
        
           
            


    




def main():

    print(argArray[0])
    print(argArray[1])
    searcher = Searcher(argArray[0])
    searcher.parseXml()
    searcher.search(argArray[1])


if __name__ == "__main__":
    main()