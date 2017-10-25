import csv
from os import walk
import os

path = os.getcwd()

# Read all the files of current directory
files = []
for subdir, dirs, files in os.walk('./data'):
    for file in files:
      print file


#with open()