import glob
import gzip
import os
import re

counter = 0
search_string_list = ['example']

for file in os.listdir():
    filename = os.fsdecode(file)
    if filename.endswith(".gz"):
        zipped = glob.glob(os.fsencode(filename))
        for log in zipped:
            with gzip.open(log, 'rt') as f:
                for line in f:
                    if any(map(line.__contains__, search_string_list)):
                        counter = counter + 1
            if counter > 0:
                print(str(log) + " has " + str(counter) + " occurrences of " + str(search_string_list) + ".")
                counter = 0

#navigate into /log directory before opening terminal or supply os.listdir() with correct path

