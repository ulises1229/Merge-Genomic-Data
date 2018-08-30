#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ulises Olivares - uolivares@enesmorelia.unam.mx'

import csv
import os
from collections import defaultdict

# Import for preprocessing files
import xlrd
import csv



def readFiles():
    '''
    This function reads all the files contained in the data directory and returns
    :return:
    '''
    files = []
    for subdir, dirs, filenames in os.walk('./data'):
        files.extend(filenames)
    return files;

def findElement(annotations, element):
    '''
    This method searchs an element in a list of annotated elements ant returns the name
    :param annotationStructure:
    :param element:
    :return:
    '''
    element = element.strip()
    if element in annotations.keys():
        return annotations[element]
    else:
        return "not found"

def readAnnotFile(dataPath, file):
    annotations = {}
    with open(dataPath + file) as csvfile:
        reader = csv.reader(csvfile)
        count = 0
        for row in reader:
            if row[1][0] == 'T':  # FIXME: CHECK IF THIS IS VALID FOR ALL
                element = ''
                if ',' in row[1]: # Detect if there exist more than one element
                    for i in row[1]:
                        if i != ',':
                            element = element + i
                        else:
                            annotations[element] = row[3].strip()  # Store test seqs as key and name as value
                            element = ''
                else: # Only one element is in the cell
                    annotations[row[1]] = row[3].strip()
            else:
                print "error no valid register on line"
    #print annotations
    return annotations


def main():

    path = os.getcwd()
    dataPath = path + "/data/"

    files = readFiles()

    #columns = defaultdict(list)

    # Structure for saving all the data
    colorRegisters = {}
    annotations = {}

    # FIXME: ALWAYS READ FIRST ANNOT FILE
    for file in files:
        # FIXME: PUT THIS INTO A METHOD
        # Read colors file
        if "COLORS" in file:
            count = 0
            with open(dataPath + file) as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if count != 0: # Ignore first Line
                        colorRegisters[row[0]] = defaultdict(list)
                        element = ''
                        for i in row[2]: # Iterate over test seqs and replace it for the long names
                            if i != ',': # split the line once a comma is detected
                                element = element + i
                            else:
                                element = element.strip() # Remove spaces at the beginning and at the end
                                anotName = findElement(annotations, element)
                                if anotName != 'not found':
                                    #print str(i)+ ": " + str(anotName)
                                    colorRegisters[row[0]][row[1]].append(anotName)
                                    # TODO: write the information in a CSV file
                                else:
                                    print "Register " + element + " not found"
                                    #print element
                                element = '' # reset element to an empty
                        count = count + 1
                        break
                    else:  # Just increment count for the first line
                        count = count + 1


        # Read annot file
        elif "ANNOT" in file:
            annotations = readAnnotFile(dataPath, file)



if __name__ == "__main__":
    main()
