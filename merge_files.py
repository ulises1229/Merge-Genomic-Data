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


def main():
    path = os.getcwd()



    dataPath = path + "/data/"
    columns = defaultdict(list)

    # Define a list of lists for storing each element

    colorRegisters = defaultdict(list)

    # FIXME: ALWAYS READ FIRST ANNOT FILE
    for file in files:
        # Read colors file
        if "COLORS" in file:
            with open(dataPath + file) as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in spamreader:
                    # print(', '.join(row))
                    if row[0][0] == 'G':  # Read only valid rows(
                        if len(row) > 3:

                        else:
                            print "Error, There is something strange in this row" + row


                            # if "GO-ID" in row[0]:
                            #   print row




        # Read annot file
        elif "ANNOT" in file:
            print "Anot"
            # with open()

if __name__ == "__main__":
    main()