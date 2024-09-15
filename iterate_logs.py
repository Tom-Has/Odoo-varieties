import glob
import gzip
import os
import re

counter = 0
#search_string = '154.54.249.214'
search_string_list = ['@eu-central-1.amazonses.com']

for file in os.listdir():
    filename = os.fsdecode(file)
    if filename.endswith(".gz"):
        zipped = glob.glob(os.fsencode(filename))
        for log in zipped:
            with gzip.open(log, 'rt') as f:
                for line in f:
                    #if search_string in line:
                    if any(map(line.__contains__, search_string_list)):
                        counter = counter + 1
            if counter > 0:
                print(str(log) + " has " + str(counter) + " occurrences of " + str(search_string_list) + ".")
                counter = 0

#navigate into /log directory before opening terminal or supply os.listdir() with correct path

"""
"""

counter = 0
with open('odoo.log', 'rt') as log:
    for line in log:
        if any(map(line.__contains__, search_string_list)):
            counter = counter + 1
print(str(log) + " has " + str(counter) + " occurrences of " + str(search_string_list) + ".")
