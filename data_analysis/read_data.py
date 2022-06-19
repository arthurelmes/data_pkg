import pkg_resources
import pandas as pd
import sys


def read_csv_0(csv_name=None):
    if not csv_name:
        # set default file name to be used when this file is imported rather 
        # than run as a script
        csv_name = pkg_resources.resource_stream(__name__, 'data/data_0.csv')
        print(csv_name)

    # use pandas to read the csv
    data = pd.read_csv(csv_name, encoding='latin-1')

    # look at the data
    for index, row in data.iterrows():
        print(row)


if __name__ == "__main__":
    # take in the basename (ie no path) of the data file
    # the path is handled by the commands below
    data_file_name = sys.argv[1]
    read_csv_0(data_file_name)


    

