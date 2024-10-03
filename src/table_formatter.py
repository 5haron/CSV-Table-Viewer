'''
Table Display Module
This module formats and displays tables based on cleaned CSV data.
Also contains various options such as sorting, filtering, and limiting the 
number of rows displayed.
'''

from tabulate import tabulate
import pandas as pd
import sys

# Display a nicely formatted table with specified columns and number of rows
def pretty_print(data, cols, num_rows):
    # case for -n single row, gets rid of empty row
    if num_rows is None and cols is None and len(data) == 1:
        data = data[:1]
        headers = []
        print(tabulate(data, headers=headers, tablefmt='fancy_grid',
                  showindex=False))
        return
 
    if num_rows is not None:
        # case for -m single row, gets rid of empty row
        if num_rows == 1 and len(data) >= 2 and cols is None:
            headers = []
            data = data[1:2]
            print(tabulate(data, headers=headers, tablefmt='fancy_grid',
                  showindex=False))
            return
        if num_rows <= 0:
            sys.exit(f"Error: Number of rows to display must be positive.")
        elif num_rows > len(data) - 1:
            sys.exit(f"Error: Can only display up to {len(data) - 1} row(s).")
        elif num_rows == 1:
            data = data[1:2]
        else:
            data = data[1:num_rows+1]

    if cols is not None:
        headers = [data[0][col_idx] for col_idx in cols]
        data = filter_columns(data[1:], cols) 
    else:
        headers = 'firstrow'

    print(tabulate(data, headers=headers, tablefmt='fancy_grid', 
                   showindex=False))

# Print only the specified columns of the table
def print_columns(data, cols):
    if cols is None:
        table = [data[0]]
    else:
        table = filter_columns(data, cols)

    print(tabulate(table, tablefmt='fancy_grid'))

# Filter the specified columns from the data
def filter_columns(data, cols):
    return [[row[col_idx] for col_idx in cols] for row in data]

# Custom sorting function to handle case-insensitive
def custom_sort(col):
    return col.apply(lambda x: x.lower() if isinstance(x, str) else x)

# Sort the data by the specified column in ascending order
def sort_by_column_up(labels, data, col_name):
    try:
        df = pd.DataFrame(data, columns=labels)
        df[col_name] = pd.to_numeric(df[col_name], errors='ignore')

        # case-insensitive sorting
        df_sorted = df.sort_values(col_name, key=custom_sort)

        return df_sorted.values.tolist()
    except Exception as e:
        print(f"Error: Unable to sort by '{col_name}' in ascending order: {e}.")
        return data

# Sort the data by the specified column in descending order
def sort_by_column_down(labels, data, col_name):
    try:
        df = pd.DataFrame(data, columns=labels)
        df[col_name] = pd.to_numeric(df[col_name], errors='ignore')

        # case-insensitive sorting
        df_sorted = df.sort_values(col_name, ascending=False, key=custom_sort)

        return df_sorted.values.tolist()
    except Exception as e:
        print(f"Error: Unable to sort by '{col_name}' in descending order: {e}")
        return data

if __name__ == "__main__":
    pass