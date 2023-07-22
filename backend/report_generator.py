import argparse
import csv
from collections import defaultdict

#This script uses the argparse module to parse command-line arguments. The script takes two required arguments: input, which is the path to the input CSV file containing the codes and their frequencies; and output, which is the path to the output CSV file where the report will be written.

#The script reads the input CSV file into a dictionary using the csv module, with the keys of the dictionary being the codes, and the values being dictionaries mapping keywords to their frequencies.

#The script calculates the total frequency of each code by summing the frequencies of all of its keywords, and stores the totals in a separate dictionary.

#The script then writes the codes, their corresponding keywords, their frequencies, their total frequency, and the percentage of the total frequency that each keyword represents to the output CSV file using the csv module.

#Note that this implementation assumes that the input CSV file has a specific format with four columns: Code, Keyword, Count, and Total. If your CSV file has a different format, you will need to modify the code accordingly.

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Generate a report of codes and their frequencies.')
    parser.add_argument('input', help='path to the input CSV file')
    parser.add_argument('output', help='path to the output CSV file')
    args = parser.parse_args()

    # Read the input CSV file into a dictionary
    codes = defaultdict(dict)
    with open(args.input, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            code = row[0]
            keyword = row[1]
            count = int(row[2])
            codes[code][keyword] = count

    # Calculate the total frequency of each code
    totals = {}
    for code, keyword_counts in codes.items():
        total = sum(keyword_counts.values())
        totals[code] = total

    # Write the codes and their frequencies to the output CSV file
    with open(args.output, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Code', 'Keyword', 'Count', 'Total', 'Percentage'])
        for code, keyword_counts in codes.items():
            total = totals[code]
            for keyword, count in keyword_counts.items():
                percentage = count / total * 100 if total > 0 else 0
                writer.writerow([code, keyword, count, total, percentage])
