import csv
import os
from collections import defaultdict

path = os.getcwd()

# Read all the files of current directory
for subdir, dirs, files in os.walk('./data'):
    print "All the data files are: " + str(files)

columns = defaultdict(list)

for file in files:
    with open(path+"/data/"+file) as f:
        reader = csv.DictReader(f)  # read rows into a dictionary format
        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            for (k, v) in row.items():  # go over each column name and value
                columns[k].append(v)  # append the value into the appropriate list
                print columns[k]
                # based on column name k
#with open()