import csv
import os

#This module provides four utility functions:

#load_csv(file_path): This function takes a file path as input, reads the CSV file from the file, and returns a list of dictionaries, where each dictionary represents a row in the CSV file, with the keys of the dictionary being the column headers.

#write_csv(file_path, headers, data): This function takes a file path, a list of headers, and a list of dictionaries as input, and writes the list of dictionaries to the CSV file at the given file path, with the headers as the first row.

#make_directory(directory): This function takes a directory path as input, and creates the directory if it doesn't already exist.

#remove_directory(directory): This function takes a directory path as input, and removes the directory and all its contents if it exists.

#Note that these utility functions are general-purpose functions that can be used in a wide range of projects, and are not specific to the code extraction and analysis tasks described in the previous sections.

def load_csv(file_path):
    """Loads a CSV file into a list of dictionaries."""
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data

def write_csv(file_path, headers, data):
    """Writes a list of dictionaries to a CSV file."""
    with open(file_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def make_directory(directory):
    """Creates a directory if it doesn't already exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def remove_directory(directory):
    """Removes a directory and all its contents."""
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                remove_directory(file_path)
        os.rmdir(directory)
