import argparse
import csv
import re
from collections import Counter
from pathlib import Path
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

#This script uses the argparse module to parse command-line arguments. The script takes three required arguments: corpus, which is the path to the corpus folder containing the text files to be processed; keywords, which is the path to a CSV file containing a list of keywords to be used for code extraction; and output, which is the path to the output CSV file where the codes and their frequencies will be written. The script also takes an optional argument --stop-words, which is the path to a file containing a list of stop words to be used during code extraction.

#The script loads the keywords from the CSV file using the csv module, creates a stemmer using the Porter stemmer from NLTK, and loads the stop words from the given file or NLTK. The script then iterates over each file in the corpus, preprocesses the text by replacing newlines and other white space with spaces, tokenizing the text into words using the word_tokenize function from NLTK, removing stop words and punctuation, and stemming the remaining words using the stemmer. The script then extracts codes from the words using the keywords, and appends the codes and their corresponding keywords to a list.

#The script counts the frequency of each code using the Counter class from the collections module, and writes the codes, their corresponding keywords, and their frequencies to the output CSV file using the csv module.

#Note that this implementation assumes that the keywords are stored in a CSV file with a single column containing the keywords in the first row. If your CSV file has a different format, you will need to modify the code accordingly.

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Extract codes from a corpus of text files.')
    parser.add_argument('corpus', help='path to the corpus folder')
    parser.add_argument('keywords', help='path to the CSV file containing the list of keywords')
    parser.add_argument('output', help='path to the output CSV file')
    parser.add_argument('--stop-words', help='path to the stop words file')
    args = parser.parse_args()

    # Load the keywords from the CSV file
    with open(args.keywords, 'r') as f:
        reader = csv.reader(f)
        keywords = [row[0] for row in reader]

    # Create a stemmer
    stemmer = PorterStemmer()

    # Load the stop words
    if args.stop_words is not None:
        with open(args.stop_words, 'r') as f:
            stop_words = set(f.read().splitlines())
    else:
        stop_words = set(stopwords.words('english'))

    # Extract codes from each file in the corpus
    codes = []
    for file_path in Path(args.corpus).glob('*.txt'):
        with open(file_path, 'r') as f:
            text = f.read()

        # Replace newlines and other white space with spaces
        text = re.sub(r'\s+', ' ', text)

        # Tokenize the text into words
        tokens = word_tokenize(text)

        # Remove stop words and punctuation, and stem the remaining words
        words = []
        for token in tokens:
            if token.lower() not in stop_words and token.isalpha():
                words.append(stemmer.stem(token.lower()))

        # Extract codes from the words using the keywords
        for keyword in keywords:
            if keyword in words:
                code = file_path.stem
                codes.append((code, keyword))

    # Count the frequency of each code
    code_counts = Counter(codes)

    # Write the codes and their frequencies to the output CSV file
    with open(args.output, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Code', 'Keyword', 'Count'])
        for code, keyword in code_counts:
            count = code_counts[(code, keyword)]
            writer.writerow([code, keyword, count])
