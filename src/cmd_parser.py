'''
Command Line Parsing Module
This module provides functions to parse and validate command line arguments.
'''

import argparse
import sys

# Checks if a given value is a positive integer and returns it as an integer
def check_positive(value):
    try:
        ivalue = int(value)
        if ivalue <= 0:
            raise ValueError()
    except ValueError:
        raise argparse.ArgumentTypeError(
            "%s is an invalid positive int value" % value)
    return ivalue

# Defines and parses command line arguments using the argparse module
def parse_arguments():
    parser = argparse.ArgumentParser(allow_abbrev=False, 
                description='A command-line utility for displaying' 
                ' and manipulating data from a CSV file.')

    # specifies the separator of the fields; default: comma;
    parser.add_argument(
        "-s", "--separator", type=str,
        help="Specify the column separator character (default is ',')")

    # outputs the list of column names in the csv file instead of the table
    parser.add_argument(
        "-l", action='store_true',
        help="Display only column headers")

    # includes only the specified column; can be used repeatedly to 
    # include more columns; order matters; default: list all columns;
    parser.add_argument(
        "-o",nargs='+', type=str,
        help="Specify the columns to display by name")

    # sort the table by ordering up the specified column; default: no sort;
    parser.add_argument(
        "-u", type=str,
        help="Sort rows by the specified column name in ascending order")

    # sort the table by ordering down the specified column; default: no sort;
    parser.add_argument(
        "-d", type=str,
        help="Sort rows by the specified column name in descending order")


    # lists only the rows having at least one element containing the string;
    parser.add_argument(
        "-m", type=str,
        help="Filter rows based on the specified string")

    # displays only the first specified number of rows of the table
    parser.add_argument(
        "-n",type=check_positive,
        help="Display the first N rows of the table")

    parser.add_argument("files", type=str, nargs='+', help="Path to input file")

    try:
        args = parser.parse_args()
    except Exception as e:
        sys.exit(f"Error: Unable to parse arguments: {e}")


    return args

if __name__ == "__main__":
    pass
