''' 
Data Input File Reading and Cleaning Module
This module reads, cleans, and filters CSV data from a file. 
Also checks for duplicate column names and handles errors related to 
file format and reading.
''' 

import re
import sys
import os

# Read data from a CSV file and split lines using the specified separator.
def read_data(file, sep):
    # check if input file has valid format i.e. CSV
    valid_extensions = ['.csv']
    _, ext = os.path.splitext(file)
    if ext not in valid_extensions:
        sys.exit(f"Error: The file '{file}' has an unsupported format."
                 f"Supported formats: {', '.join(valid_extensions)}.")

    data = []
    total_lines = 0
    discarded_lines = 0
    inconsistent_column_lines = 0

    try:
        # read the file and store its contents as a list of lines
        with open(file, 'r') as f:
            lines = f.readlines()
        
        first_row = lines[0].strip().split(sep)
        data.append(first_row)
        lines = lines[1:]

        num_cols = len(data[0])

        # split lines using specified separator
        for line in lines:
            total_lines += 1
            split = line.strip().split(sep)
            
            # check if the number of columns is consistent across rows
            if len(split) != num_cols:
                discarded_lines += 1
                print(f"Warning: Inconsistent number of columns in"
                      f"line: {line.strip()}.")
                continue

            try:
                data.append(split)
            except Exception as e:
                print(f"Warning: Error occurred while splitting a line: {e}.")

    # handle file I/O and other exceptions
    except IOError as e:
        sys.exit(f"Error: Unable to open the file '{file}': {e}.")
    except Exception as e:
        sys.exit(f"Error: An unexpected error occurred while reading the file." 
                 f"'{file}': {e}")

    print(f"Total lines: {total_lines}")
    # print(f"Discarded lines due to inconsistent columns: {discarded_lines}")
    print(f"Total discarded lines: {discarded_lines}")

    return data

# Clean each field of each row in the data
def clean_data(data):
    cleaned_data = []
    for row in data:
        try:
            cleaned_row = [clean_field(field) for field in row]
            cleaned_data.append(cleaned_row)
        except Exception as e:
            print(f"Warning: Error occurred while cleaning row in data: {e}.")
    return cleaned_data

# Remove disallowed characters from the field and truncate if necessary
def clean_field(field):
    try:
        allowed_characters = r'[^ -~]' 
        cleaned_field = re.sub(allowed_characters, '', field)
        max_field_length = 100
        return cleaned_field[:max_field_length]
    except Exception as e:
        print(f"Warning: An error occurred while cleaning a field: {e}.")
        return field

# Filters input data by rows containing the specified strings in any cell
def filter_rows_by_string(data, strs, include_header=True):
    if strs is None:
        return data

    filtered_data = []
    if include_header:
        filtered_data.append(data[0])

    for row in data[1:]:
        for s in strs:
            if any(s in cell for cell in row):
                filtered_data.append(row)
                break

    return filtered_data
    
# Check for duplicate column names and raise an error if found
def check_duplicate_columns(column_names):
    seen = set()
    for col_name in column_names:
        if col_name in seen:
            sys.exit(f"Error: Duplicate column name '{col_name}' found." 
                     f"Column names must be unique.")
        seen.add(col_name)

if __name__ == "__main__":
    pass
