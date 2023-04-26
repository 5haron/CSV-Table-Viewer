# CSV Table Viewer - README

## Table of Contents
1. [Overview](#overview)
   * [Description](#description)
   * [Modules](#modules)
2. [Getting Started](#getting-started)
   * [Prerequisites](#prerequisites)
   * [Installing Required Libraries](#installing-required-libraries)
3. [Running the Code](#running-the-code)
   * [Command-line Options](#command-line-options)
4. [Usage Examples](#usage-examples)

## Overview
### Description
The CSV Table Viewer program is a command-line application designed to read, display, and manipulate data from CSV (Comma Separated Values) files. The program provides various options for customizing the table output, such as specifying the column separator, displaying specific columns, sorting rows based on a given column, filtering rows by a search string, and limiting the number of displayed rows.

With its simple and intuitive command-line interface, the CSV Table Viewer program provides a convenient tool for users who need to quickly view and manipulate data stored in CSV files.

### Modules

The program consists of four main modules:

* `showTable.py`: The main script that ties together the other modules, parses command-line arguments, and executes the specified operations.
* `cmd_parser.py`: A module responsible for parsing command-line arguments and returning them in a structured format.
* `data_reader.py`: A module responsible for reading and cleaning the input CSV data, ensuring it is formatted correctly for further processing.
* `table_formatter.py`: A module that handles the formatting and display of the table data, including sorting, filtering, and creating a visually appealing output.


## Getting Started
Follow these steps to set up and run the CSV Table Viewer program on your local machine:

### Prerequisites

Ensure that you have the following installed on your system:

- Python 3.6 or higher
- `pandas` library
- `tabulate` library

### Installing Required Libraries

To install the required libraries, open a terminal and run the following command:

```bash
pip install pandas tabulate
```

## Running the Code

To run the ShowTable utility, open a terminal and navigate to the directory containing the ShowTable files. Then, run the following command:

```bash
python3 showTable.py [options] <data_file>
```

where `[options]` are optional command-line arguments and `data_file` is the path to the input CSV file.

### Command-line Options

- `-s <character>`: specifies the separator of the fields (default is ',')
- `-l`: outputs only the list of column headers
- `-o <column>`: includes only the specified column; can be used repeatedly to include more columns; order matters; (default: lists all columns)
- `-u <column>`: sort the table by ordering the specified column in ascending order (default: no sort)
- `-d <column>`: sort the table by ordering the specified column in descending order (default: no sort)
- `-m <string>`: lists only the rows having at least one element containing the string; multiple appearances are joined by
- `-n <number>`: displays only the first specified number of rows of the table

## Usage Examples

1. Display the table with default settings:
```bash
python3 showTable.py example.csv
```

2. Use a different column separator:
```bash
python3 showTable.py -s "|" example.csv
```

3. Display only column headers:
```bash
python3 showTable.py -l example.csv
```

4. Display the two following columns:
```bash
python3 showTable.py example.csv -o Phone Name 
```

5. Sort rows by the Name column in ascending order:
```bash
python3 showTable.py -u Name example.csv
```

6. Sort rows by the Name column in descending order:
```bash
python3 showTable.py -d Name example.csv
```

7. Filter rows based on the string "on":
```bash
python3 showTable.py -m "on" example.csv
```

8. Display the first 10 rows of the table:
```bash
python3 showTable.py -n 10 example.csv
```
