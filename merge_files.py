#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ulises Olivares - uolivares@gmail.com'

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
    if element in annotations.keys():
        return annotations[element]
    else:
        return "not found"


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
                        elementList = []
                        for i in row[2]: # Iterate over test seqs and replace it for the long names
                            if i != ',': # split the line once a comma is detected
                                element = element + i
                            else:
                                anotName = findElement(annotations, element)
                                if anotName != 'not found':
                                    #print str(i)+ ": " + str(anotName)
                                    colorRegisters[row[0]][row[1]].append(anotName)
                                    # TODO: write the information in a CSV file
                                else:
                                    print "Register " + element + " not found"
                                element = '' # reset element to an empty
                        count = count +1
                        break
                    else:  # Just increment count for the first line
                        count = count + 1


        #FIXME: PUT THIS INTO A METHOD
        # Read annot file
        elif "ANNOT" in file:
            with open(dataPath + file) as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row[1][0] == 'T': #FIXME: CHECK IF THIS IS VALID FOR ALL
                        #print len(row)
                        #if row[0][0] != '':
                        element = ''
                        for i in row[1]:
                            # TODO: COMPLETE THIS PART
                            annotations[i] = row[3] # Store test seqs as key and name as value
                    else:
                        print "error"


if __name__ == "__main__":
    main()