'''
Show Table Main File
A a command-line utility for displaying and manipulating data from a CSV file.
It uses several helper functions to parse command-line arguments, read and 
clean data from a file, format and sort data, and print data to the console.
'''

import argparse
import sys
import os
import string
from cmd_parser import parse_arguments
from data_reader import read_data, clean_data, filter_rows_by_string
from table_formatter import (pretty_print, print_columns,
                             sort_by_column_up, sort_by_column_down)

def main(args):
    sep = args.separator

    # checking the separator
    if sep is None:
        sep = ","

    if len(sep) != 1:
        sys.exit("Separator must be a single character")
    
    if sep not in string.printable:
        sys.exit("Separator must be a printable character")

    if type(sep) != str:
        sys.exit("Separator must be a character")

    file = args.files[0]

    # checking input files
    if len(args.files) > 1:
        sys.exit("Error: Only one input file is allowed.")

    if not os.path.exists(file):
        sys.exit(f"Error: The file '{file}' does not exist.")

    if os.path.getsize(file) == 0:
        sys.exit(f"Error: The file '{file}' is empty.")

    data = read_data(file, sep)

    # case: csv file has no data
    if len(data) == 1 and \
                     (args.separator or args.u or args.d or args.m or args.n):
        sys.exit("Error: Cannot use -s, -u, -d, -m, or -n options with a"
                " table containing only column headers.")

    data = clean_data(data)

    # case: csv file has no data
    if len(data) == 1:
        print("Warning: The CSV file only contains column headers and no data."
             " Command options are limited to -l and -o.")

    # check for separator conflicts in column names and cell values
    for row in data:
        for cell in row:
            if sep in cell:
                sys.exit(f"Error: The separator '{sep}' conflicts with"
                         f"characters in column names or cell values.")

    # check for column in table
    if args.o:
        labels = data[0]
        cols = []
        for col_name in args.o:
            try:
                cols.append(labels.index(col_name))
            except ValueError:
                sys.exit(f"Error: Column '{col_name}' not found in the data." 
                         f"Available columns: {', '.join(labels)}")
    else:
        cols = None

    # sort data by specified column in ascending order if requested
    sort_up = args.u
    if sort_up is not None:
        try:
            labels = data[0]
            if sort_up not in labels:
                raise ValueError()

            data = sort_by_column_up(labels, data[1:], sort_up)
            data.insert(0, labels)
        except ValueError:
            sys.exit(f"Error: Column '{sort_up}' not found in the data." 
                    f"Available columns: {', '.join(labels)}")

    # sort data by specified column in descending order if requested
    sort_down = args.d
    if sort_down is not None:
        try:
            labels = data[0]
            if sort_down not in labels:
                raise ValueError()

            data = sort_by_column_down(labels, data[1:], sort_down)
            data.insert(0, labels)
        except ValueError:
            sys.exit(f"Error: Column '{sort_down}' not found in the data." 
                    f"Available columns: {', '.join(labels)}")


    # check if two flags are used
    if args.u and args.d:
        sys.exit("Error: Both sortUp (-u) and sortDown (-d) options"
                 "cannot bse used together.")

    num_rows = args.n

    if args.m:
        filtered_data = filter_rows_by_string(data, [args.m], include_header=False)
        if len(filtered_data) == 0:
            print(f"No rows found with '{args.m}'")
            return
        else:
            data = filtered_data


    if not args.l:
        pretty_print(data, cols, num_rows)
    else:
        print_columns(data, cols)

if __name__ == '__main__':
    args = parse_arguments()
    main(args)

