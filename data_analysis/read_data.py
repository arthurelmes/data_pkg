from pathlib import Path
import os.path as op
from csv import reader
import sys

# take in the basename (ie no path) of the data file
# the path is handled by the commands below
data_file_name = sys.argv[1]

# get the dir of this python file
this_dir = Path(__file__).parent

# get the parent dir
parent_dir = this_dir.parent

# define the data dir
data_dir = op.join(parent_dir, "data")


with open(op.join(data_dir, data_file_name), "r") as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        print(row)

