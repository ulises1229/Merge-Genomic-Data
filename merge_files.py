#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ulises Olivares - uolivares@gmail.com'

import csv
import os
from collections import defaultdict



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
        # Read colors file
        if "COLORS" in file:
            count = 0
            with open(dataPath + file) as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if count != 0: # Ignore first Line
                        colorRegisters[row[0]] = defaultdict(list)
                        print row[3]
                        for i in range(): # Iterate over test seqs and replace it for the long names
                            #print i
                            anotName = findElement(annotations, i)
                            if anotName != 'not found':
                                #print str(i)+ ": " + str(anotName)
                                colorRegisters[row[0]][row[1]].append(anotName)
                        count = count +1
                        break
                    else:  # Just increment count for the first line
                        count = count + 1


                '''if row[0][0] == 'G':  # Read only valid rows
                                    if len(row) > 3:
                                        colorRegisters[row[0]] = defaultdict(list)
                                        for i in range (2,len(row)):
                                            print str (count +1) + " Element to search: " + row[i]

                                        # description = findElement(row[i])
                                        # colorRegisters[row[0]][row[0]].append(description)
                                        # first identify the sample and then save it

                                        # colorRegisters[row[0]][row[1]].appen()


                                    else:
                                        print "Error, There is something strange in this row, please clean your data" + row
                                        print "Please, check register: " + str(count + 1)


                                        # if "GO-ID" in row[0]:
                                        #   print row'''


        # Read annot file
        elif "ANNOT" in file:
            with open(dataPath + file) as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    for i in row[1]:
                        annotations[i] = row[3] # Store test seqs as key and name as value

if __name__ == "__main__":
    main()