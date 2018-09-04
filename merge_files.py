#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Ulises Olivares - uolivares@enesmorelia.unam.mx

import os
from collections import defaultdict
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

    orig = element

    # Find the | char to just obtain the first part of the ID
    pos = element.find("|")
    pos2 = element.find(" ")



    if pos2 < pos and pos2 != -1:
        element = element[0:pos2]
        # Remove empty spaces
        element = element.replace(" ", "")
    else:
        # Cut string when the char | is present
        element = element[0:pos]
        # Remove empty spaces
        element = element.replace(" ", "")



    test = next((s for s in annotations.keys() if element in s), None)  # returns 'abc123'

    if test == None:
        print "Early Not found "

    if element in annotations.keys():
        return annotations[element]
    else:
        return "not found"

def readAnnotFile(dataPath, file):
    '''

    :param dataPath:
    :param file:
    :return:
    '''

    annotations = {}
    with open(dataPath + file) as csvfile:
        reader = csv.reader(csvfile)
        count = 0
        for row in reader:
            if row[1][0] == 'T':  # FIXME: CHECK IF THIS IS VALID FOR ALL ELEMENTS
                element = ''
                if ',' in row[1]: # Detect if there is more than one element
                    for i in row[1]:
                        if i != ',':
                            element = element + i
                        else:
                            annotations[element] = row[3].strip()  # Store test seqs as key and name as value
                            element = ''
                else: # Only one element is in the cell

                    # FIXME: MAKE THIS A METHOD IT IS USED MORE THAN ONCE
                    # Remove empty spaces
                    key =  row[1].replace(" ","")

                    # Find the | char to just obtain the first part of the ID
                    pos = key.find("|")

                    # Cut string when the char | is present
                    key = key[0:pos]

                    # Cut find the

                    annotations[key] = row[3].replace(" ","")
            else:
                print "error, not a valid register" + row[0]
    #print annotations
    return annotations

def readColorsFile(dataPath, file, annotations):
    '''

    :param dataPath:
    :param file:
    :param annotations:
    :return:
    '''
    colorRegisters = {}

    with open(dataPath + file) as csvfile:
        reader = csv.reader(csvfile)
        count = 0
        annotatedFile = file[0:file.find(".csv")] + "_ANNOT.csv"
        with open(dataPath + annotatedFile, 'wb') as csvfile:
            writer = csv.writer(csvfile)
            for row in reader:
                if count != 0:  # Ignore first Line
                    colorRegisters[row[0]] = defaultdict(list)
                    element = ''
                    # Write new file with annotations
                    csvRow = list()
                    # Append first row
                    csvRow.append(row[0])
                    # Append second row
                    csvRow.append(row[1])

                    for i in row[2]:  # Iterate over test seqs and replace it for the long names
                        if i != ',':  # split the line once a comma is detected
                            element = element + i
                        else:
                            element = element.strip()  # Remove spaces at the beginning and at the end
                            anotName = findElement(annotations, element)
                            if anotName != 'not found':
                                if anotName == '#NAME?':
                                    print element
                                print anotName
                                # print str(i)+ ": " + str(anotName)
                                colorRegisters[row[0]][row[1]].append(anotName)
                                # TODO: write the information in a CSV file
                                csvRow.append(anotName)
                                #print "element found"
                            else:
                                print "Register " + element + " not found"
                                # print element
                            element = ''  # reset element to an empty value
                        count = count + 1
                        #break
                    writer.writerow(csvRow)
                else:  # Just increment count for the first line
                    count = count + 1
        csvfile.close()
    return colorRegisters


def main():
    '''

    :return:
    '''

    path = os.getcwd()
    dataPath = path + "/data/"

    files = readFiles()

    #columns = defaultdict(list)

    # Structures for saving all data
    colorRegisters = {}
    annotations = {}


    # SORT all files to read first the ANOTT file
    files.sort()
    for file in files:
        # Read colors file
        if "COLORS" in file:
            colorsRegisters = readColorsFile(dataPath, file, annotations)


        # Read annot file
        elif "ANNOT" in file:
            annotations = readAnnotFile(dataPath, file)



if __name__ == "__main__":
    main()
