import csv
from os import walk
import os

path = os.getcwd()

# Read all the files of current directory
for subdir, dirs, files in os.walk('./data'):
    print "All the data files are: " + str(files)



#with open()