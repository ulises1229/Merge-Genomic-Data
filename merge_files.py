import csv
import os
from collections import defaultdict

path = os.getcwd()

# Read all the files of current directory
for subdir, dirs, files in os.walk('./data'):
    print "All the data files are: " + str(files)

dataPath = path + "/data/"
columns = defaultdict(list)

# Define a list of lists for storing each element

registers = {}
for file in files:
    # Read colors file
    if "COLORS" in file:
        with open(dataPath + file) as csvfile:
             spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
             for row in spamreader:
                 #print(', '.join(row))
                 if row[0][0] == 'G': # Read only valid rows(
                     if 'TR' in row[3]:
                         print "error"
                         print row[3][0:4]

                     #if "GO-ID" in row[0]:
                      #   print row




    # Read annot file
    elif "ANNOT" in file:
        print "Anot"
        #with open()