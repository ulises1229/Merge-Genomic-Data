import csv
import os
from collections import defaultdict

path = os.getcwd()

# Read all the files of current directory
for subdir, dirs, files in os.walk('./data'):
    print "All the data files are: " + str(files)

dataPath = path + "/data/"
columns = defaultdict(list)

for file in files:
    with open(dataPath + file) as csvfile:
         spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
         for row in spamreader:
             #print(', '.join(row))

             if row[0][0] != 'G': #detect invalid rows
                 print row
    #with open()